import requests
import time
from random import getrandbits

print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " - Adidas account creator with captcha bypass")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " - Developed by @jamzigod")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------\n")

time.sleep(2)

first_name = "Jamzi" #Enter first name
last_name = "God" #Enter last name
password = "Adidas123" #Enter chosen password
base_email = "carts" #Enter base of the email you want to use
domain = "@jamzigod.com" #Enter domain for your emails e.g. (@gmail.com)
times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of account(s) you would like to create: "))) #DONT CHANGE

text_file = open("Accounts.txt", "w")

def create_account():

    global email

    email = (base_email + "{}" + domain).format(getrandbits(40))

    base_url = "https://shop.miteam.adidas.co.uk/miadidas-miteam/Login.action"

    s = requests.session()

    params = {
        "registerUser": "",
        "sourcePath": "",
        "recipeIdent": "",
        "orderId": "",
        "minAge": "14",
        "userVO.userAuthentication.regFirstName": first_name,
        "userVO.userAuthentication.regLastName": last_name,
        "userVO.userAuthentication.regLogin": email,
        "userVO.userAuthentication.regPassword": password,
        "userVO.userAuthentication.confrmPassword": password,
        "userVO.dateVO.day": "01",
        "userVO.dateVO.month": "01",
        "userVO.dateVO.year": "1996",
        "agree": "true",
        "_sourcePage": "Q_zM-69uzSnv_J5IuzfaPzCh8EB353v6Dyn4g6K-ZaE=",
        "__fp": "cwbm4kzjY63tX0vBwkvCEZJLK9EzG94c0gJWx_ZSn7KmRJxEPupQ7btb9qEXch6S7V9LwcJLwhFmRiJ-SrR4x1OD6-LbZO5dzB5dlMOuFKLKYpT2bTd5fGOQ9fAgsISr"
    }


    res = s.post(base_url, params=params)

    if "e-mail address already exists" in res.text:
        print("[" + (time.strftime("%H:%M:%S") + "]" + ' - This email "' + email + '" is a duplicate!'))
    else:
        print("[" + (time.strftime("%H:%M:%S") + "]" + " - Successfully created adidas account with " + email))
        write()

def write():

    text_file.write(email + ":" + password + "\n")

for i in range (times):
    create_account()

text_file.close()
