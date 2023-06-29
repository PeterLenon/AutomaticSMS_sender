import requests
import schedule
import time
import random
import datetime


API_KEY = 'f30d6e982b2202e92b1e4d580d4a5a3d096e9d78nrcyurvBbxZgVCwKSM6pld41G'
number_link_dict = {
    '7695674373': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_T0k5r0tr7YabtcY&_g_=g",
    '8127786648': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_fB93a7prL242KmD&_g_=g",
    '7172479172': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_1nFwlOgSxTcxIxz&_g_=g",
    '8126063889': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_pXlDBDbimJuwZh4&_g_=g",
    '8123616267': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_OhPtBXw6pZ5dryc&_g_=g",
    '8123615242': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_n9nLlYZAAXt72bn&_g_=g"
}

name_number_dict = {
    'Peter': '7695674373',
    'Long-Jing': '8127786648',
    'Manasi': '8126063889',
    'Weslie': '7172479172',
    'Phil': '8123616267',
    'Selma': '8123615242'
}

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


min_time_diff = 2 #set the minimum time difference
timestamps = randTime(min_time_diff)
msg_order_dict[timestamps[0]] = "1st"
msg_order_dict[timestamps[1]] = "2nd"


def send_message(message_order):
    for nameKey in name_number_dict:
        name = nameKey
        number = name_number_dict[name]
        link = number_link_dict[number]
        date = datetime.datetime.now().strftime('%B, %d')

        messages = [
            f"{date}\n Hi {name}, I hope this message finds you well. This is a friendly reminder to complete the {message_order} diary now by clicking on the following link: {link}.\n\n Thank you!\nPlease note that this is an automated message, so there is no need to reply directly to it. If you have any questions or concerns, please feel free to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"{date}\n Hello {name}, Just a quick reminder to complete the {message_order} diary by accessing the following link: {link}.\n\n Your input is greatly appreciated!\nPlease note that this is an automated message, so there is no need to reply directly to it. If you have any questions or concerns, please feel free to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"{date}\n Hey there, {name}, Just wanted to gently remind you to take a moment and complete the {message_order} diary using the provided link: {link}. \n\n If you have any questions, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654. ",
            f"{date}\n Hi {name}! Friendly reminder to finish the {message_order} diary task. Simply click on the link provided: {link}.\n\n Should you have any concerns, feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"{date}\n Greetings, {name}, Just a gentle nudge to complete the {message_order} diary by accessing the following link: {link}.\n\n If you have any questions or need assistance, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"{date}\n Hello {name}, This is a friendly reminder to kindly complete the {message_order} diary using the provided link: {link}. If you require any clarifications or have concerns, please feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"{date}\n Hi there, {name}, Just a quick reminder to complete the {message_order} diary task. Please click on the following link: {link}.\n\n If you need assistance, reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654. ",
            f"{date}\n Hey {name}! We kindly remind you to finish the {message_order} diary by clicking on the provided link: {link}.\n\n Should you have any questions or concerns, feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"{date}\n Hi {name}, Just a friendly reminder to complete the {message_order} diary using the link below: {link}.\n\n If you have any queries or need support, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"{date}\n Hello, {name}, This is a gentle reminder to complete the {message_order} diary task at your convenience. You can access it through the following link: {link}.\n\n For any questions or concerns, feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"{date}\n Hey {name}! Just a quick reminder to wrap up the {message_order} diary by using the provided link: {link}.\n\n If you need any assistance or have questions, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654."
        ]

        resp = requests.post('http://textbelt.com/text', {
            'phone': str(number),
            'message': random.choice(messages),
            'key': API_KEY
        })
        print(resp.json())


schedule.every().day.at(timestamps[0]).do(send_message, message_order=msg_order_dict[timestamps[0]])
schedule.every().day.at(timestamps[1]).do(send_message, message_order=msg_order_dict[timestamps[1]])

while True:
    schedule.run_pending()
    time.sleep(1)