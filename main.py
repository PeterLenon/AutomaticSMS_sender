import requests
import schedule
import time

API_KEY = 'f30d6e982b2202e92b1e4d580d4a5a3d096e9d78nrcyurvBbxZgVCwKSM6pld41G'
number_link_dict = {
    '7695674373': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&Q_DL=EMD_S8HCpCW5cI6VabX_3Ua4zpnLOCrIrX0_CGC_T0k5r0tr7YabtcY&_g_=g",
    '8127786648': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&Q_DL=EMD_S8HCpCW5cI6VabX_3Ua4zpnLOCrIrX0_CGC_fB93a7prL242KmD&_g_=g",
    '7172479172': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&Q_DL=EMD_S8HCpCW5cI6VabX_3Ua4zpnLOCrIrX0_CGC_1nFwlOgSxTcxIxz&_g_=g",
    '8126063889': "https://iu.co1.qualtrics.com/jfe/form/SV_3Ua4zpnLOCrIrX0?Q_CHL=email&Q_DL=EMD_S8HCpCW5cI6VabX_3Ua4zpnLOCrIrX0_CGC_pXlDBDbimJuwZh4&_g_=g"}


def send_message():
    for key in number_link_dict:
        number = key
        link = number_link_dict[key]
        resp = requests.post('http://textbelt.com/text', {
            'phone': str(number),
            'message': f"Hi, please fill out the form on the link attached. Thank you {str(link)}",
            'key': API_KEY
        })
        print(resp.json())


schedule.every().day.at('16:30').do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
