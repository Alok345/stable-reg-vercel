import urllib3
import uuid
import random
import json

# Built-in urllib3 (no install needed)
http = urllib3.PoolManager()

CLICK_URL = "https://ad2click.media-412.com/click"
PID = "SM_REG_05NOV"
OFFER_ID = "873227"

def fire_click():
    click_id = str(uuid.uuid4())
    gaid = str(uuid.uuid4()).upper()
    params = {
        'pid': PID,
        'offer_id': OFFER_ID,
        'sub2': click_id,
        'sub1': 'playstore',
        'sub5': gaid
    }
    try:
        http.request('GET', CLICK_URL, fields=params, timeout=5.0)
    except:
        pass
    return click_id, gaid

# Vercel Handler
def handler(event, context):
    clicks = random.randint(90, 100)
    for _ in range(clicks):
        fire_click()
    final_click_id, final_gaid = fire_click()
    
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "text/plain" },
        "body": f"REG DONE → GAID: {final_gaid[:8]}... | Clicks: {clicks}"
    }
