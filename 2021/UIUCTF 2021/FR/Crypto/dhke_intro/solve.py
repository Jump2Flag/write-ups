from Crypto.Cipher import AES

for k in range(40):
    k = str(k)
    key = ""
    i = 0
    padding = "uiuctf2021uiuctf2021"
    while (16 - len(key) != len(k)):
        key = key + padding[i]
        i += 1
    key = key + k
    key = bytes(key, encoding='ascii')

    flag = "b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6"

    iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.decrypt(bytes.fromhex(flag))

    if b"uiuctf" in ciphertext:
        print(f"[+] KEY : {key.decode()}")
        print(f"[+] FLAG : {ciphertext.decode().strip()}")