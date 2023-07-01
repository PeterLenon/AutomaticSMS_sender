import requests
import schedule
import time
import random
import datetime
import pandas as pd

API_KEY = 'f30d6e982b2202e92b1e4d580d4a5a3d096e9d78nrcyurvBbxZgVCwKSM6pld41G'  # NEVER TOUCH THIS


message_filepath = "C:\\Users\gosho\OneDrive\Desktop\R-HouseFiles\ExpertPanel_Diary_Message.xlsx"
contacts_filepath = "C:\\Users\gosho\OneDrive\Desktop\R-HouseFiles\ExpertPanel_Contacts.xlsx"
minimum_hr_diff = 2

number_link_dict = {
    '7695674373': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_T0k5r0tr7YabtcY&_g_=g"
}
name_number_dict = {
    'Peter': '7695674373'
}


def load_contacts(filepath, name_number_dictionary, number_link_dictionary):
    df = pd.read_excel(filepath)
    df['Phone_Number'] = df['Phone_Number'].astype(str)
    for row in df.index:
        name_number_dictionary[df['FirstName'][row]] = df['Phone_Number'][row]
        number_link_dictionary[df['Phone_Number'][row]] = df['Link'][row]


def randomize_Time(min_hour_diff):  # returns a sorted list of timestamps to send messages i.e ["12:03", "17:47"]
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
    return [timestamp2, timestamp1]


msg_order_dict = {}
timestamps = randomize_Time(minimum_hr_diff)
msg_order_dict[timestamps[0]] = "1st"
msg_order_dict[timestamps[1]] = "2nd"
load_contacts(contacts_filepath, name_number_dict, number_link_dict)


def send_message(message_order):
    def load_messages(filepath):
        messages_list = []
        df = pd.read_excel(filepath)
        for row in df.index:
            messages_list.append(
                (df['message'][row] % (today, name, message_order, link, disclaimer)).format(newline='\n'))
        return messages_list

    if message_order == "2nd":
        disclaimer = "\nIf you missed the first diary, then just fill out this one (2nd one) and do not worry about the first one."
    else:
        disclaimer = ""
    for nameKey in name_number_dict:
        name = nameKey
        number = name_number_dict[name]
        link = number_link_dict[number]
        today = datetime.datetime.now().strftime('%B, %d')
        messages = load_messages(message_filepath)

        resp = requests.post('http://textbelt.com/text', {
            'phone': str(number),
            'message': random.choice(messages),
            'key': API_KEY
        })
        print(resp.json())


schedule.every().day.at(timestamps[0]).do(send_message, message_order=msg_order_dict[timestamps[0]])
schedule.every().day.at(timestamps[1]).do(send_message, message_order=msg_order_dict[timestamps[1]])
print(timestamps)

while True:
    schedule.run_pending()
    time.sleep(1)
