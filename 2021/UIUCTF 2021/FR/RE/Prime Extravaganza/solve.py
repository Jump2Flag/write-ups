import hashlib

values = [0]*5
for i in range(4, -1, -1):
    values[i] = (i + 1 )*0x4d29 # reverse because of LIFO
print(f"[+] VALUES : {values}")
flag = "uiuctf{"+hashlib.md5(str(sum(values)).encode()).hexdigest()+"}"
print(f"[+] FLAG : {flag}")