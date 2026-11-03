"""Save the current temporary lab session outside the project folder."""
import json
import os
from getpass import getpass
from pathlib import Path

print('Chi nhap gia tri cua phien Learner Lab dang Start.')
print('Khong dan ca dong aws_access_key_id=; chi dan gia tri sau dau =.')
print('Khi dan se KHONG hien ky tu. Dan xong bam Enter.')
values = {}
for key, label in [
    ('aws_access_key_id', 'AWS access key ID'),
    ('aws_secret_access_key', 'AWS secret access key'),
    ('aws_session_token', 'AWS session token')
]:
    value = getpass(label + ': ').strip()
    if not value or any(x.isspace() for x in value) or value.startswith('aws_'):
        raise SystemExit('Gia tri trong/sai dinh dang. Chay lai va chi dan gia tri sau dau =.')
    values[key] = value
folder = Path.home() / '.cloud-exam-demo'
folder.mkdir(mode=0o700, parents=True, exist_ok=True)
path = folder / 'credentials.json'
fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
with os.fdopen(fd, 'w', encoding='utf-8') as stream:
    json.dump(values, stream)
print('Da luu phien lab tren may nay, ben ngoai thu muc ma nguon.')
print('Tiep theo chay: .\\.venv\\Scripts\\python.exe app.py')
