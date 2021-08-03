# dhke_intro

![dhke_intro](https://i.imgur.com/0BXdi8e.png)

Pour ce challenge on nous donne un fichier ``dhkectf_intro.py`` et un fichier 

``output.txt`` qui contient le flag chiffré.

Analysons le fichier ``dhkectf_intro.py`` :

```python
import random
from Crypto.Cipher import AES

# generate key
gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]
g, p = random.choice(gpList)
a = random.randint(1, p)
b = random.randint(1, p)
k = pow(g, a * b, p)
k = str(k)

# print("Diffie-Hellman key exchange outputs")
# print("Public key: ", g, p)
# print("Jotaro sends: ", aNum)
# print("Dio sends: ", bNum)
# print()

# pad key to 16 bytes (128bit)
key = ""
i = 0
padding = "uiuctf2021uiuctf2021"
while (16 - len(key) != len(k)):
    key = key + padding[i]
    i += 1
key = key + k
key = bytes(key, encoding='ascii')

"""with open('flag.txt', 'rb') as f:
    flag = f.read()"""

iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(flag)

print(ciphertext.hex())
```

Dans ce script on aura une variable ``k`` qui contiendra un nombre généré aléatoirement et transformé en string, elle sera ensuite concaténé à ``padding[:16-len(k)]``, ce qui fait : ``padding[:16-len(k)]`` + ``k``.

Il suffit donc de faire un script qui déchiffre le flag en testant plusieurs valeur de ``k`` : 

```python
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
```

```python
$ python3 solve.py
[+] KEY : uiuctf2021uiuct9
[+] FLAG : uiuctf{omae_ha_mou_shindeiru_b9e5f9}
```

Super !! On peut maintenant valider le challenge avec le flag : ``uiuctf{omae_ha_mou_shindeiru_b9e5f9}``.


