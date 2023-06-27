import requests
import schedule
import time
import random

API_KEY = 'f30d6e982b2202e92b1e4d580d4a5a3d096e9d78nrcyurvBbxZgVCwKSM6pld41G'
number_link_dict = {
    '7695674373': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_T0k5r0tr7YabtcY&_g_=g",
    '8127786648': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_fB93a7prL242KmD&_g_=g",
    '7172479172': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_1nFwlOgSxTcxIxz&_g_=g",
    '8126063889': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&RID=CGC_pXlDBDbimJuwZh4&_g_=g"
}

name_number_dict = {
    'Peter': '7695674373',
    'Long-Jing': '8127786648',
    'Manasi': '8126063889',
    'Weslie': '7172479172'
}

def randTime():
    hr = random.randrange(8, 20, 1)
    if hr < 10:
        hr = str(f"0{hr}")
    else:
        hr = str(hr)
    mins = random.randrange(0, 59, 1)
    if mins < 10:
        mins = str(f"0{mins}")
    else:
        mins = str(mins)
    timestamp = hr + ":" + mins
    return timestamp


def send_message():
    for nameKey in name_number_dict:
        name = nameKey
        number = name_number_dict[name]
        link = number_link_dict[number]

        messages = [
            f"Hi {name}, I hope this message finds you well. This is a friendly reminder to complete the diary now by clicking on the following link: {link}.\n\n Thank you!\nPlease note that this is an automated message, so there is no need to reply directly to it. If you have any questions or concerns, please feel free to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"Hello {name}, Just a quick reminder to complete the diary by accessing the following link: {link}.\n\n Your input is greatly appreciated!\nPlease note that this is an automated message, so there is no need to reply directly to it. If you have any questions or concerns, please feel free to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"Hey there, {name}, Just wanted to gently remind you to take a moment and complete the diary using the provided link: {link}. \n\n If you have any questions, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654. ",
            f"Hi {name}! Friendly reminder to finish the diary task. Simply click on the link provided: {link}.\n\n Should you have any concerns, feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"Greetings, {name}, Just a gentle nudge to complete the diary by accessing the following link: {link}.\n\n If you have any questions or need assistance, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"Hello {name}, This is a friendly reminder to kindly complete the diary using the provided link: {link}. If you require any clarifications or have concerns, please feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"Hi there, {name}, Just a quick reminder to complete the diary task. Please click on the following link: {link}.\n\n If you need assistance, reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654. ",
            f"Hey {name}! We kindly remind you to finish the diary by clicking on the provided link: {link}.\n\n Should you have any questions or concerns, feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"Hi {name}, Just a friendly reminder to complete the diary using the link below: {link}.\n\n If you have any queries or need support, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654.",
            f"Hello, {name}, This is a gentle reminder to complete the diary task at your convenience. You can access it through the following link: {link}.\n\n For any questions or concerns, feel free to contact Long-Jing (Claire) at hsulon@iu.edu or via text at (765) 537-8654.",
            f"Hey {name}! Just a quick reminder to wrap up the diary by using the provided link: {link}.\n\n If you need any assistance or have questions, don't hesitate to reach out to Long-Jing (Claire) at hsulon@iu.edu or text (765) 537-8654."
        ]

        resp = requests.post('http://textbelt.com/text', {
            'phone': str(number),
            'message': random.choice(messages),
            'key': API_KEY
        })
        print(resp.json())


time1 = randTime()
time2 = randTime()
while abs(int(time2[:2]) - int(time1[:2])) <= 1:
    time2 = randTime()
print(time1)
print(time2)
schedule.every().day.at(time1).do(send_message)
schedule.every().day.at(time2).do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
