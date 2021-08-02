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