import requests 
from bs4 import BeautifulSoup as bs
requests.urllib3.disable_warnings()

ENDPOINT = ""

def getUsername(studentID, birthTuple):
    s = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Connection": "keep-alive"
    }

    r1 = s.get(ENDPOINT, verify=False, headers=headers) # Get validation data stuffs
    aspDATA = bs(r1.text, 'html.parser')

    data = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": aspDATA.find(id="__VIEWSTATE").get("value"),
        "__VIEWSTATEGENERATOR": aspDATA.find(id="__VIEWSTATEGENERATOR").get("value"),
        "__EVENTVALIDATION": aspDATA.find(id="__EVENTVALIDATION").get("value"),
        "tbStuId": studentID,
        "ddlDobMonth": birthTuple[0],
        "ddlDobDay": birthTuple[1],
        "ddlDobYear": birthTuple[2],
        "btnStuId": "Submit"
    }

    r2 = s.post(ENDPOINT, verify=False, data=data, headers=headers)
    aspUSERNAME = bs(r2.text, 'html.parser')
    return aspUSERNAME.find(id="lblUsername3").text

def convertBirthday(birthString):
    endStr = ""
    s = birthString.split("/")
    
    return (s[0], s[1], s[2])

id = str(input("StudentID (ex: 000000): "))
bday = str(input("birthday (ex: 1/1/2000): "))
print("Your username is: " + getUsername(id, convertBirthday(bday)))
