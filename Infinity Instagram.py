import requests
import time
import proxyscrape
import os
os.system("Title Infinity Instagram Bot V1.0")
os.system("cls")
print("""Infinity Instagram Bot V1.0 | Features : 
# EveryTime You Refresh New Proxy 
# Self And Spam Report | @Mhmy""")
input("Enter To Continue : ")
collector = proxyscrape.create_collector('my-collector', 'http')
proxy = collector.get_proxy({'country': 'united states'})
proxies = {
  'http': f"{proxy.host}:{proxy.port}",
}
r = requests.session()
Login_Username = input("Username : ")
Login_Pass = input("Password : ")
Login_url = "https://www.instagram.com/accounts/login/ajax/"
Login_headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '270',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'ig_did=1C68ED86-809A-45DE-98A0-6793FF11FAE4; csrftoken=eC684p8yejyYtHvjvKRJP5CNMsYrfCTm; mid=YE0a2gALAAFloSK0CNneUXD8LY0P; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
'x-csrftoken': 'eC684p8yejyYtHvjvKRJP5CNMsYrfCTm',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
'x-instagram-ajax': '6d90752528fc',
'x-requested-with': 'XMLHttpRequest'
}
Login_payload = {
'username': Login_Username,
"enc_password":f"#PWD_INSTAGRAM_BROWSER:0:1589682409:{Login_Pass}",
'queryParams': "{}",
'optIntoOneTap': 'false'
}
Login = requests.post(Login_url,headers=Login_headers,data=Login_payload,proxies=proxies)
TRue = '"userId"'
if TRue in Login.text:
    print("Sucessfully Logined!")
    print("Get Your ID :")
    print("https://instagram.com/Target/?__a=1")
    Target = input("Target ID : ")
    Target_URL = f'https://www.instagram.com/users/{Target}/report/'
    Target_Headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '37',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=1C68ED86-809A-45DE-98A0-6793FF11FAE4; mid=YE0a2gALAAFloSK0CNneUXD8LY0P; ig_nrcb=1; shbid=16372; shbts=1616525357.6682472; rur=PRN; csrftoken=ZyfbHBxFlDCwBOGfckonw3K6fwBOMPoz; ds_user_id=46700123316; sessionid=46700123316%3AZgwuf9hkmnWIUs%3A4',
        'origin': 'https://www.instagram.com',
        'referer': f'https://www.instagram.com/users/{Target}/report/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'x-csrftoken': 'ZyfbHBxFlDCwBOGfckonw3K6fwBOMPoz',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1v2bkZzN29oD37TTrJzecWJFGPy3fOAKJVWyFVnd-r3VZA',
        'x-instagram-ajax': 'acb59e1f2c1f',
        'x-requested-with': 'XMLHttpRequest'
    }
    r.headers.update({'X-CSRFToken': Login.cookies['csrftoken']})
    Check_Target = f'https://instagram.com/{Target}/'
    Check_Headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'ig_did=1C68ED86-809A-45DE-98A0-6793FF11FAE4; mid=YE0a2gALAAFloSK0CNneUXD8LY0P; ig_nrcb=1; shbid=16372; shbts=1616525357.6682472; rur=PRN; csrftoken=ZyfbHBxFlDCwBOGfckonw3K6fwBOMPoz; ds_user_id=46700123316; sessionid=46700123316%3AZgwuf9hkmnWIUs%3A4; ig_cb=2',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    for x in range(100000):
        Spam = {
        'source_name': '',
        'reason_id': '1',
        'frx_context': ''
    }
        SpamR = requests.post(Target_URL,headers=Target_Headers,data=Spam,proxies=proxies)
        time.sleep(2)
        print(SpamR.text)
        r.headers.update({'X-CSRFToken': SpamR.cookies['csrftoken']})
        if SpamR.text == '{"description":"Your reports help keep our community free of spam.","status":"ok"}':
            print("[ SPAM ] : " + f"{proxy.host}:{proxy.port}")
        elif SpamR.text == '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We restrict certain activity to protect our community.","feedback_url":"repute/report_problem/instagram_user_flag/?violation_type\u0026responsible_policy=iGTooManyNegativeFeedbackBetweenAPairOfUsersV2","feedback_action":"report_problem","status":"fail"}':
            print('[ Blocked ] : ' + f"{proxy.host}:{proxy.port}")
        else:
            print('[ ERROR ] : ' + f"{proxy.host}:{proxy.port}")
        Self = {
            'source_name': '',
            'reason_id': '2',
            'frx_context': ''
        }
        time.sleep(2)
        SelfR = requests.post(Target_URL,headers=Target_Headers,data=Self,proxies=proxies)
        r.headers.update({'X-CSRFToken': SelfR.cookies['csrftoken']})
        print(SelfR.text)
        if SelfR.text == '{"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"}':
            print("[ SELF ] : " + f"{proxy.host}:{proxy.port}")
        else:
            print("[ ERROR ] : " + f"{proxy.host}:{proxy.port}")
else:
    print("False")
    pass

