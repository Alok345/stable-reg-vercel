# api/reg.py
import requests, uuid, random, time

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
        requests.get(CLICK_URL, params=params, timeout=5)
    except:
        pass
    return click_id, gaid

def handler(event, context):
    # Run only ONE registration
    clicks = random.randint(90, 100)
    print(f"Starting {clicks} clicks...")
    for i in range(clicks):
        fire_click()
        time.sleep(0.25)  # 0.25s × 100 = 25s → fits in 60s limit
    final_click_id, final_gaid = fire_click()
    
    return {
        "statusCode": 200,
        "body": f"REG DONE → GAID: {final_gaid[:8]}... | Clicks: {clicks}"
    }