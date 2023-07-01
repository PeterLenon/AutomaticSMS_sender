import requests
import schedule
import time
import random
import datetime
import pandas as pd

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


# def send_message(message_order):
#     resp = requests.post('http://textbelt.com/text', {
#         'phone': str(7695674373),
#         'message': f"{message_order} message {datetime.datetime.now().strftime(' %B, %d')}",
#         'key': API_KEY
#     })
#     print(resp.json())




# while True:
#     schedule.run_pending()
#     time.sleep(1)
#
# print(datetime.datetime.now().strftime('%B, %d'))

name_number_dict = {}
number_link_dict = {}

def load_contacts(filepath, name_number_dictionary, number_link_dictionary):
    df = pd.read_csv(filepath)
    df['Phone_Number'] = df['Phone_Number'].astype(str)
    for row in df.index:
        name_number_dictionary[df['FirstName'][row]] = df['Phone_Number'][row]
        number_link_dictionary[df['Phone_Number'][row]] = df['Link'][row]


load_contacts("C:\\Users\gosho\OneDrive\Desktop\R-HouseFiles\ExpertPanel_Contacts.csv", name_number_dict, number_link_dict)
print(name_number_dict)


messagefile = "C:\\Users\gosho\OneDrive\Desktop\R-HouseFiles\ExpertPanel_Diary_Message.xlsx"
def send_message(message_order):
    def load_messages(filepath):
        messages_list = []
        df = pd.read_excel(filepath)
        for row in df.index:
            messages_list.append((df['message'][row] % (today, name, message_order, link, disclaimer)).format(newline='\n'))
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

        messages = [
            f"{today}\nHi {name}, I hope this message finds you well. This is a friendly reminder to complete the {message_order} diary now by clicking on the following link: {link}.\n\nThank you!\nPlease note that this is an automated message, so there is no need to reply directly to it. If you have any questions or concerns, please feel free to reach out to our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHello {name}, Just a quick reminder to complete the {message_order} diary by accessing the following link: {link}.\n\nYour input is greatly appreciated!\nPlease note that this is an automated message, so there is no need to reply directly to it. If you have any questions or concerns, please feel free to reach out to our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHey there, {name}, Just wanted to gently remind you to take a moment and complete the {message_order} diary using the provided link: {link}.\n\nIf you have any questions, don't hesitate to reach out to our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHi {name}! Friendly reminder to finish the {message_order} diary task. Simply click on the link provided: {link}.\n\nShould you have any concerns, feel free to contact our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nGreetings, {name}, Just a gentle nudge to complete the {message_order} diary by accessing the following link: {link}.\n\nIf you have any questions or need assistance, don't hesitate to reach out to our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHello {name}, This is a friendly reminder to kindly complete the {message_order} diary using the provided link: {link}.\n\nIf you require any clarifications or have concerns, please feel free to contact our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHi there, {name}, Just a quick reminder to complete the {message_order} diary task. Please click on the following link: {link}.\n\nIf you need assistance, reach out to our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHey {name}! We kindly remind you to finish the {message_order} diary by clicking on the provided link: {link}.\n\nShould you have any questions or concerns, feel free to contact our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHi {name}, Just a friendly reminder to complete the {message_order} diary using the link below: {link}.\n\nIf you have any queries or need support, don't hesitate to reach out to our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHello, {name}, This is a gentle reminder to complete the {message_order} diary task at your convenience. You can access it through the following link: {link}.\n\nFor any questions or concerns, feel free to contact our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}",
            f"{today}\nHey {name}! Just a quick reminder to wrap up the {message_order} diary by using the provided link: {link}.\n\nIf you need any assistance or have questions, don't hesitate to reach out to our team at pgoshomi@iu.edu or text (769) 567-4373.{disclaimer}"
        ]
    messages1 = load_messages(messagefile)
    print(messages1[0])

send_message("2nd")