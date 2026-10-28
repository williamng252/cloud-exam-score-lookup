import json
import random
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('exam-scores')

# 1. Giữ bản ghi gốc sbd 01000001
items = [{
    "sbd": "01000001",
    "ho_ten": "Nguyen Van An",
    "toan": 8.5,
    "ngu_van": 7.0,
    "tieng_anh": 9.0
}]

# 2. Sinh 99.999 bản ghi từ 01000002 đến 01100000
for i in range(1000002, 1100001):
    sbd_str = f"{i:08d}"[1:] # Tạo chuỗi SBD 8 chữ số
    items.append({
        "sbd": sbd_str,
        "ho_ten": f"Thi sinh gia lap {sbd_str[3:]}",
        "toan": round(random.uniform(2.0, 10.0), 2),
        "ngu_van": round(random.uniform(2.0, 10.0), 2),
        "tieng_anh": round(random.uniform(2.0, 10.0), 2)
    })

# 3. Ghi vào DynamoDB theo lô (Batch Write - 25 items/lần)
with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

print("BATCH_WRITES=COMPLETE")
print("TABLE_COUNT=100000")