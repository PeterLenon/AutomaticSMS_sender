import requests
import schedule
import time
import random
import datetime
import pandas as pd

# API_KEY = 'f30d6e982b2202e92b1e4d580d4a5a3d096e9d78nrcyurvBbxZgVCwKSM6pld41G'
API_KEY = '477344530fb151b3584e2342f242ad24bedf766eIhSx1L7fznqthfbdmAAYVBwcx'  # NEVER TOUCH THIS

messages_filepath = "C:\\Users\gosho\OneDrive\Desktop\R-HouseFiles\ExpertPanel_Diary_Message.xlsx"
contacts_filepath = "C:\\Users\gosho\OneDrive\Desktop\R-HouseFiles\ExpertPanel_Contacts.xlsx"
minimum_time_diff_in_hrs = 2
messages_per_person = 2


class Person:
    def __init__(self, Name, Cell, Link):
        self.name = Name
        self.phone = Cell
        self.link = Link
        self.messages = []

    def add_message(self, sms):
        self.messages.append(sms)


def load_contactsV2(filepath):
    panelists = []
    df = pd.read_excel(filepath)
    for row in df.index:
        panelists.append(Person(df['FirstName'][row], df['Phone_Number'][row], df['Link'][row]))
    return panelists


def load_messagesV2(filepath, panelists, num_of_msg):
    df = pd.read_excel(filepath)
    for panelist in panelists:
        copy_of_msg_num = num_of_msg
        while copy_of_msg_num:
            message_order = "1st" if panelist.messages == [] else "2nd"
            disclaimer = "" if message_order == "1st" else "\nIf you missed the first diary of the day , then just fill out this one (2nd one) and do not worry about the first one."
            today = datetime.datetime.now().strftime("%B %d")
            panelist.add_message((df['message'][random.randrange(0, len(df.index), 1)] % (
                panelist.name, message_order, today, panelist.link, disclaimer)).format(newline='\n'))
            copy_of_msg_num -= 1


def send_messageV2():
    for panelist in message_receivers_list:
        resp = requests.post('http://textbelt.com/text', {
            'phone': panelist.phone,
            'message': panelist.messages[0],
            'key': API_KEY
        })
        panelist.messages.pop(0)
        print(resp.json())



def randTimeV2(min_diff, num_of_sms):
    def padding(num):
        if num < 10:
            num = str(f"0{num}")
        else:
            num = str(num)
        return num

    hr_set = set({})
    start_hr = 8
    end_hr = 20
    while num_of_sms != len(hr_set):
        hr_set.add(random.randrange(start_hr, end_hr, min_diff))
    hr_set = sorted(list(hr_set))
    for index in range(0, len(hr_set)):
        hr_set[index] = padding(hr_set[index]) + ":" + padding(random.randrange(0, 59, 1))
    return hr_set


timestamps = randTimeV2(minimum_time_diff_in_hrs, messages_per_person)
print(timestamps)
message_receivers_list = load_contactsV2(contacts_filepath)
load_messagesV2(messages_filepath, message_receivers_list, messages_per_person)

for Time in timestamps:
    schedule.every().day.at(Time).do(send_messageV2)


while True:
    schedule.run_pending()
    time.sleep(1)


