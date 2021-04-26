# Wrapper

```python
#coding:utf-8

import base64
import pwn
import string
import time

def hexaDecode(cipher):
    return base64.b16decode(cipher).decode()

def b32decode(cipher):
    return base64.b32decode(cipher).decode()

def binDecode7bit(cipher):
    plaintext = ""
    for i in range(0, len(cipher), 7):
        plaintext += chr(int(cipher[i:i+7], 2))
    return plaintext


host = "chall0.heroctf.fr"
port = 7001

nc = pwn.remote(host, port)
nc.recvline()
nc.recvline()

cipher = nc.recvline().decode().strip()

charsB32 = [i for i in string.ascii_uppercase+"234567="]
charsHex = [i for i in string.hexdigits]
charsBin = ["0","1"]

while cipher.find("pass:") == -1:
    z, y, x = 0, 0, 0
    for i in cipher:
        if i in charsBin:
            z+=1
        if i in charsHex:
            y+=1
        if i in charsB32:
            x+=1
    if z == len(cipher):
        cipher=binDecode7bit(cipher)
    elif y == len(cipher):
        cipher=hexaDecode(cipher)
    elif x == len(cipher):
        cipher=b32decode(cipher)

code = cipher.split(":")[1]

nc.sendline(code)
nc.recvline()

result = nc.recvline()

print(result)
```
