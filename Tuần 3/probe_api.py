import argparse
import json
import urllib.request
import botocore.session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True)
parser.add_argument('--mode', default='single', choices=['single', 'burst', 'cache'])
parser.add_argument('--unsigned', action='store_true')
args = parser.parse_args()

def call(sbd="01000001"):
    url = f"{args.url}/scores?sbd={sbd}"
    headers = {}
    
    # Nếu không truyền --unsigned thì tự động ký SigV4 với AWS_IAM
    if not args.unsigned:
        session = botocore.session.get_session()
        credentials = session.get_credentials()
        request = AWSRequest(method='GET', url=url, headers=headers)
        SigV4Auth(credentials, 'execute-api', 'us-east-1').add_auth(request)
        headers = dict(request.headers)

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, r.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8')

# Xử lý theo chế độ chạy
if args.mode == 'single':
    status, body = call()
    print(f"MODE single SIGNED {not args.unsigned}")
    print(f"HTTP_COUNTS {{{status}: 1}}")
    print(f"FIRST {{\"status\": {status}, \"body\": {json.dumps(body)}}}")

elif args.mode == 'burst':
    # Gửi 120 request liên tục để kích hoạt Throttling và Concurrency Limit
    results = [call() for _ in range(120)]
    counts = {}
    for st, _ in results:
        counts[st] = counts.get(st, 0) + 1
    print(f"MODE burst SIGNED {not args.unsigned}")
    print(f"HTTP_COUNTS {counts}")

elif args.mode == 'cache':
    # Gọi 30 lần lặp lại 1 SBD để tạo Cache Hit
    results = [call("01000001") for _ in range(30)]
    print(f"MODE cache completed 30 requests")