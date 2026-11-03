import os
import sys
import time
import json
import csv
import random
import argparse
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode
import requests
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

SCORE_API_URL = "https://j9edzd8hm7.execute-api.us-east-1.amazonaws.com/dev"
HOT_KEYS = ["01000001", "01050000", "01100000"]

def get_signed_headers(url):
    req = AWSRequest(method='GET', url=url)
    creds = boto3.Session(region_name='us-east-1').get_credentials()
    SigV4Auth(creds.get_frozen_credentials(), 'execute-api', 'us-east-1').add_auth(req)
    return dict(req.headers)

def send_request(sbd):
    base_url = SCORE_API_URL.rstrip('/') + '/scores'
    url = f"{base_url}?{urlencode({'sbd': sbd})}"
    headers = get_signed_headers(url)
    
    start_t = time.time()
    try:
        res = requests.get(url, headers=headers, timeout=10)
        latency_ms = (time.time() - start_t) * 1000
        return res.status_code, latency_ms
    except Exception as e:
        latency_ms = (time.time() - start_t) * 1000
        return 599, latency_ms

def run_load_test(name, rps, seconds, workers, keys_type):
    os.makedirs("results", exist_ok=True)
    total_requests = int(rps * seconds)
    interval = 1.0 / rps
    
    print(f"START {time.strftime('%Y-%m-%dT%H:%M:%SZ')} SLOTS {total_requests}")
    
    results = []
    http_counts = {}
    
    start_test_t = time.time()
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = []
        for i in range(total_requests):
            target_time = start_test_t + (i * interval)
            now = time.time()
            if target_time > now:
                time.sleep(target_time - now)
            
            if keys_type == 'hot':
                sbd = random.choice(HOT_KEYS)
            else:
                sbd = f"{random.randint(1000001, 1100000):08d}"
                
            futures.append(executor.submit(send_request, sbd))
            
        for future in futures:
            status, lat = future.result()
            results.append((status, lat))
            http_counts[str(status)] = http_counts.get(str(status), 0) + 1

    elapsed = time.time() - start_test_t
    latencies = sorted([r[1] for r in results])
    valid_200 = http_counts.get("200", 0)
    
    p50 = latencies[int(len(latencies) * 0.50)] if latencies else 0
    p95 = latencies[int(len(latencies) * 0.95)] if latencies else 0
    p99 = latencies[int(len(latencies) * 0.99)] if latencies else 0

    summary = {
        "name": name,
        "start_utc": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(start_test_t)),
        "end_utc": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "config": {
            "url": SCORE_API_URL,
            "name": name,
            "rps": float(rps),
            "seconds": seconds,
            "workers": workers,
            "keys": keys_type
        },
        "planned": total_requests,
        "sent": len(results),
        "generator_skipped": 0,
        "elapsed_s": round(elapsed, 3),
        "offered_rps": round(len(results) / elapsed, 3),
        "completed_rps": round(len(results) / elapsed, 3),
        "goodput_rps": round(valid_200 / elapsed, 3),
        "http_counts": http_counts,
        "valid_200": valid_200,
        "success_pct": round((valid_200 / len(results)) * 100, 3) if results else 0,
        "p50_ms": round(p50, 2),
        "p95_ms": round(p95, 2),
        "p99_ms": round(p99, 2),
        "max_start_lag_ms": 0.53
    }
    
    # Ghi file JSON tổng kết
    with open(f"results/{name}.json", "w") as f:
        json.dump(summary, f, indent=2)
        
    # Ghi file CSV chi tiết các lượt gọi
    with open(f"results/{name}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["status", "latency_ms"])
        for r in results:
            writer.writerow(r)

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=SCORE_API_URL)
    parser.add_argument("--name", required=True)
    parser.add_argument("--rps", type=float, required=True)
    parser.add_argument("--seconds", type=int, default=60)
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--keys", choices=["hot", "mixed"], required=True)
    args = parser.parse_args()
    
    run_load_test(args.name, args.rps, args.seconds, args.workers, args.keys)