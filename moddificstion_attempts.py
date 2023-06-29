import requests
import schedule
import time
import random
import datetime

API_KEY = 'f30d6e982b2202e92b1e4d580d4a5a3d096e9d78nrcyurvBbxZgVCwKSM6pld41G'

msg_order_dict = {}


def randTime(min_hour_diff):  # returns a sorted list of timestamps to send messages i.e ["12:03", "17:47"]
    def padding(num):
        if num < 10:
            num = str(f"0{num}")
        else:
            num = str(num)
        return num

    hr1 = random.randrange(8, 20, 1)
    hr2 = random.randrange(8, 20, 1)
    hr2 = padding(hr2)
    hr1 = padding(hr1)
    while abs(int(hr2) - int(hr1)) <= min_hour_diff:  # ensuring that the times are spaced by at least an hour
        hr2 = random.randrange(8, 20, 1)
        hr2 = padding(hr2)

    mins1 = random.randrange(0, 59, 1)
    mins2 = random.randrange(0, 59, 1)
    mins1 = padding(mins1)
    mins2 = padding(mins2)
    timestamp1 = hr1 + ":" + mins1
    timestamp2 = hr2 + ":" + mins2
    if int(hr1) < int(hr2):
        return [timestamp1, timestamp2]
    return [timestamp2, timestamp2]


min_time_diff = 2
# timestamps = randTime(min_time_diff)
# print(timestamps)
timestamps = ["00:59", "01:00"]
msg_order_dict[timestamps[0]] = "1st"
msg_order_dict[timestamps[1]] = "2nd"


def send_message(message_order):
    resp = requests.post('http://textbelt.com/text', {
        'phone': str(7695674373),
        'message': f"{message_order} message {datetime.datetime.now().strftime(' %B, %d')}",
        'key': API_KEY
    })
    print(resp.json())


schedule.every().day.at(timestamps[0]).do(send_message, message_order=msg_order_dict[timestamps[0]])
schedule.every().day.at(timestamps[1]).do(send_message, message_order=msg_order_dict[timestamps[1]])

while True:
    schedule.run_pending()
    time.sleep(1)

print(datetime.datetime.now().strftime('%B, %d'))
