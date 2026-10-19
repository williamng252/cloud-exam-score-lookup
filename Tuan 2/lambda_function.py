import json
import logging
import re
from decimal import Decimal

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

table = boto3.resource("dynamodb").Table("exam-scores")


def decimal_to_number(value):
    if isinstance(value, Decimal):
        return int(value) if value == int(value) else float(value)
    raise TypeError("Unsupported type")


def response(status, data):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json; charset=utf-8"},
        "body": json.dumps(
            data,
            ensure_ascii=False,
            default=decimal_to_number
        )
    }


def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    sbd = params.get("sbd")

    if not isinstance(sbd, str) or not sbd.strip():
        return response(400, {"message": "Vui lòng nhập số báo danh"})

    sbd = sbd.strip()

    if not re.fullmatch(r"[0-9]{8}", sbd):
        return response(400, {"message": "Số báo danh phải gồm 8 chữ số"})

    try:
        result = table.get_item(Key={"sbd": sbd})
        item = result.get("Item")

        if item is None:
            return response(404, {"message": "Không tìm thấy số báo danh"})

        logger.info("Tra cuu thanh cong request_id=%s", context.aws_request_id)
        return response(200, item)

    except Exception:
        logger.exception("Loi tra cuu DynamoDB")
        return response(500, {"message": "Lỗi hệ thống, vui lòng thử lại"})