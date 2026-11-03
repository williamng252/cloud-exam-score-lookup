import sys
import requests
import boto3
from urllib.parse import urlencode
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

# Endpoint API Gateway Stage dev
SCORE_API_URL = "https://j9edzd8hm7.execute-api.us-east-1.amazonaws.com/dev"

def call_api(sbd, unsigned=False):
    url = SCORE_API_URL.rstrip('/') + '/scores'
    params = {'sbd': sbd} if sbd != 'NONE' else {}
    if params:
        url += '?' + urlencode(params)
    
    req = AWSRequest(method='GET', url=url)
    
    # Thực hiện ký SigV4 nếu không truyền unsigned=True
    if not unsigned:
        creds = boto3.Session(region_name='us-east-1').get_credentials()
        SigV4Auth(creds.get_frozen_credentials(), 'execute-api', 'us-east-1').add_auth(req)
        
    res = requests.get(url, headers=dict(req.headers), timeout=10)
    print(f"SBD: [{sbd}] | Status: {res.status_code} | Response: {res.text[:120]}")

if __name__ == "__main__":
    print("=== KIỂM THỬ CHỨC NĂNG F401 - F406 ===")
    # F401-F403: Các SBD hợp lệ (Trả về 200)
    call_api("01000001", False)
    call_api("01050000", False)
    call_api("01100000", False)
    
    # F404: SBD không tồn tại (Trả về 404)
    call_api("99999999", False)
    
    # F405: SBD sai định dạng / Thiếu SBD (Trả về 400)
    call_api("abc", False)
    call_api("NONE", False)
    
    # F406: Request chưa ký SigV4 (Trả về 403)
    call_api("01000001", True)