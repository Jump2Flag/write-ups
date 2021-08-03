# back_to_basics

![](https://i.imgur.com/58CC9k7.png)

Dans ce challenge, deux fichiers sont donnés, un fichier ``main.py`` et un fichier ``flag_enc`` . 

Pour commencer annalysons le fichier ``main.py`` :

```python
from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary
#from secret import flag, key

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

def base_n_encode(bytes_in, base):
    return mpz(bytes_to_long(bytes_in)).digits(base).upper().encode()

def base_n_decode(bytes_in, base):
    bytes_out = to_binary(mpz(bytes_in, base=base))[:1:-1]
    return bytes_out

def encrypt(bytes_in, key):
    out = bytes_in
    for i in key:
            print(i)
            out = base_n_encode(out, ALPHABET.index(i))
    return out

def decrypt(bytes_in, key):
    out = bytes_in
    for i in key:
        out = base_n_decode(out, ALPHABET.index(i))
    return out

"""
flag_enc = encrypt(flag, key)
f = open("flag_enc", "wb")
f.write(flag_enc)
f.close()
"""
```

Dans le script ``main.py``, nous pouvons voir que la fonction ``encrypt()`` prend en argument le plaintext et la clé, elle va ensuite encoder le plaintext avec une base correspondant à l'index caractère par caractère de la clé dans ``ALPHABET``.

Le nombre d'encodage utilisé pour rendre le flag illisible et donc égal à la longueur de la clé et la base utilisé est égal à l'index des lettres de la clé dans la variable ``ALPHABET``.

Il suffit donc de décoder avec les bonnes base plusieurs fois à la suite jusqu'à tomber sur le flag.

Pour être sure que c'est la bonne base qui sera appliquer à chaque fois, il suffit de vérifier que tout les caractères après le décodage soit dans la variable `ALPHABET` ou alors que la chaine de caractères contienne ``uiuctf{``.

Il suffit donc de faire un script, permettant de réaliser cela : 

```python
from gmpy2 import mpz, to_binary

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")
flag_encrypt = bytes(open("flag_enc").read(), "utf-8")
key = ""
while 1:
    for base in range(38, 2, -1):
        test = to_binary(mpz(flag_encrypt, base=base))[:1:-1]
        if b"uiuctf{" in test:
            break
        bad = False
        for char in test:
            if char not in ALPHABET:
                bad = True
                break
        if not bad:
            key += chr(ALPHABET[base])
            break

    currentBase = base
    flag_encrypt = test
    print(f"[+] CURRENT BASE {currentBase}")

    if b"uiuctf{" in flag_encrypt:
        print(f"\n[+] FLAG : {flag_encrypt.decode()}")
        print(f"[+] KEY : {key[::-1]}")
        break
```

(J'ai rajouté, l'affichage de la clé en bonus, mais c'est pas du tout une obligation)

Résultat lors de l'execution : 

```
$ python3 solve.py
[+] CURRENT BASE 32
[+] CURRENT BASE 22
[+] CURRENT BASE 5
[+] CURRENT BASE 35
[+] CURRENT BASE 8
[+] CURRENT BASE 12
[+] CURRENT BASE 27
[+] CURRENT BASE 19
[+] CURRENT BASE 10
[+] CURRENT BASE 11
[+] CURRENT BASE 33
[+] CURRENT BASE 19
[+] CURRENT BASE 13
[+] CURRENT BASE 19
[+] CURRENT BASE 5
[+] CURRENT BASE 32

[+] FLAG : uiuctf{r4DixAL}
[+] KEY : 5JDJXBAJRC8Z5MW
```

Bingo !! Suffit de valider avec le flag : ``uiuctf{r4DixAL}`` !!
