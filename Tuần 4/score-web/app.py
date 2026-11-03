import json
import os
import re
from pathlib import Path
from urllib.parse import urlencode

import boto3
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
API_URL = 'https://j9edzd8hm7.execute-api.us-east-1.amazonaws.com/dev/scores'
CREDENTIALS_FILE = Path.home() / '.cloud-exam-demo' / 'credentials.json'

@app.after_request
def no_cache(response):
    response.headers['Cache-Control'] = 'no-store'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.get('/')
def home():
    return render_template('index.html')

@app.get('/api/scores')
def scores():
    sbd = request.args.get('sbd', '').strip()
    if not re.fullmatch(r'[0-9]{8}', sbd):
        return jsonify(error='Vui lòng nhập đúng 8 chữ số của số báo danh.'), 400
    try:
        # Read again each time so a renewed lab session needs no code change.
        if not CREDENTIALS_FILE.exists():
            return jsonify(error='Chưa kết nối phiên lab. Chạy py configure_lab.py trong Terminal.'), 503
        values = json.loads(CREDENTIALS_FILE.read_text(encoding='utf-8'))
        session = boto3.Session(**values, region_name='us-east-1')
        credentials = session.get_credentials().get_frozen_credentials()
        url = API_URL + '?' + urlencode({'sbd': sbd})
        signed = AWSRequest(method='GET', url=url)
        SigV4Auth(credentials, 'execute-api', 'us-east-1').add_auth(signed)
        response = requests.get(url, headers=dict(signed.headers),
                                timeout=(5, 15), allow_redirects=False)
        print("AWS STATUS:", response.status_code, flush=True)
        print("AWS ERROR TYPE:", response.headers.get("x-amzn-ErrorType", "Không có"), flush=True)

        if response.status_code != 200:
            messages = {
                400: 'Yêu cầu không hợp lệ.',
                403: 'Phiên AWS hết hạn hoặc không có quyền gọi API. Cập nhật bằng configure_lab.py; kiểm tra IAM nếu vẫn lỗi.',
                404: 'Không tìm thấy thí sinh có số báo danh này.',
                429: 'Hệ thống đang nhận nhiều yêu cầu. Vui lòng thử lại sau vài giây.'
            }
            code = response.status_code
            return jsonify(error=messages.get(code, 'Dịch vụ AWS chưa xử lý được yêu cầu. Kiểm tra API và CloudWatch.'), upstream_status=code), code if code in messages else 502
        data = response.json()
        fields = ['sbd', 'ho_ten', 'toan', 'ngu_van', 'tieng_anh']
        if not isinstance(data, dict) or data.get('sbd') != sbd or not all(k in data for k in fields):
            return jsonify(error='API trả dữ liệu không đúng định dạng hoặc sai số báo danh. Kiểm tra cache key sbd.'), 502
        return jsonify({k: data[k] for k in fields})
    except requests.Timeout:
        return jsonify(error='Kết nối AWS quá thời gian chờ. Vui lòng thử lại.'), 504
    except requests.RequestException:
        return jsonify(error='Không kết nối được API AWS. Kiểm tra mạng và trạng thái lab.'), 502
    except (ValueError, KeyError, TypeError, OSError):
        return jsonify(error='Cấu hình phiên lab hoặc phản hồi API không hợp lệ. Chạy lại configure_lab.py.'), 502
    except Exception:
        # Never expose credential values or a debug traceback to the browser.
        return jsonify(error='Chưa đọc được phiên AWS. Kiểm tra cấu hình và thử lại.'), 503

if __name__ == '__main__':
    print('Mo trinh duyet: http://127.0.0.1:5000')
    app.run(host='127.0.0.1', port=5000, debug=False)
