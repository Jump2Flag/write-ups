# crypto warmup

## Script donnée:
```python
import random
import math

n = 24

# sans importance
def make_stuff():
    A = []; b = [1, 10]
    for i in range(n):
        A.append(random.randint(*b))
        b[False] = sum(A) + 1
        b[True] = int(b[False] << 1)
    c = random.randint(sum(A), sum(A) << 1)
    while True:
        d = random.randint(sum(A), sum(A) << 1)
        if math.gcd(c, d) == 1:
            break

    return [(d*w) % c for w in A]


def weird_function_1(s): #s = OooO

    # liste en binaire sur un octet (8digits) / 3 colonnes => convertion en 1 seule colonne
    return sum([list(map(int,bin(ord(c))[2:].zfill(8))) for c in s], [])

def do_magic(OooO, B):
    # somme <= weird_function return[0..24] * B[0..24] <=> 24 fois <=> 1 * 4267101277 ou 0 * 4267101277
    return sum(m * b for m, b in zip(weird_function_1(OooO), B))
	
	
B = make_stuff()

with open("flag") as fd:
    flag = fd.read().strip()

print(B)
for i in range(0, len(flag), 3):
    print(do_magic(flag[i:i+3], B))
    


## B = [4267101277, 4946769145, 6306104881, 7476346548, 7399638140, 1732169972, 1236242271, 5109093704, 2163850849, 6552199249, 3724603395, 3738679916, 5211460878, 642273320, 3810791811, 761851628, 1552737836, 4091151711, 1601520107, 3117875577, 2485422314, 1983900485, 6150993150, 2045278518]
##34451302951
##58407890177
##49697577713
##45443775595
##38537028435
##47069056666
##49165602815
##43338588490
##32970122390
```

## Script de résolution:
```python
import string

L = [34451302951, 58407890177, 49697577713, 45443775595, 38537028435,
47069056666, 49165602815, 43338588490, 32970122390]

B = [4267101277, 4946769145, 6306104881, 7476346548, 7399638140, 1732169972,
1236242271, 5109093704, 2163850849, 6552199249, 3724603395, 3738679916,
5211460878, 642273320, 3810791811, 761851628, 1552737836, 4091151711,
1601520107, 3117875577, 2485422314, 1983900485, 6150993150, 2045278518]

PossibleCharsUsed = string.printable[:-6]

flag = ""

# on parcourt le tableau L afin de déchiffrer chaque block et reconstituer le flag
for block in L:
    # on test chaque lettres de PossibleCharsUsed jusqu'à trouver la bonne correspondance entre block et les lettres possible
    # sachant qu'il y a 3 lettres par block sauf potenciellement le dernier qui peut-être de 1,2 ou 3 lettres.
    for letter1 in PossibleCharsUsed:
        # convertion de la lettre en binaire sur 8bits sous forme de tableau
        letterToBinArray = [int(i) for i in bin(ord(letter1))[2:].zfill(8)]

        # si m = 1 alors on prend la valeur de b sinon ca donne 0, ensuite on fait la somme du tableau obtenu
        x = sum(m * b for m,b in zip(letterToBinArray, B))

        # si x == block alors letter1 correspond à la valeur déchiffré de block
        if x == block:
            print(f"{block} : {letter1}")
            flag += letter1

        for letter2 in PossibleCharsUsed:
            letterToBinArray = [int(i) for i in bin(ord(letter1))[2:].zfill(8)+bin(ord(letter2))[2:].zfill(8)]
            x = sum(m * b for m,b in zip(letterToBinArray, B)) 
            if x == block:
                print(f"{block} : {letter1+letter2}")
                flag += letter1+letter2

            for letter3 in PossibleCharsUsed:
                letterToBinArray = [int(i) for i in bin(ord(letter1))[2:].zfill(8)+bin(ord(letter2))[2:].zfill(8)+bin(ord(letter3))[2:].zfill(8)]
                x = sum(m * b for m,b in zip(letterToBinArray, B))
                if x == block:
                    print(f"{block} : {letter1+letter2+letter3}")
                    flag += letter1+letter2+letter3
            
print(f"\nFLAG : {flag}")

"""
$ python3 script.py
34451302951 : CTF
58407890177 : {w4
49697577713 : rmu
45443775595 : p-k
38537028435 : n4p
47069056666 : s4c
49165602815 : k-f
43338588490 : tw!
32970122390 : }

FLAG : CTF{w4rmup-kn4ps4ck-ftw!}
"""
```

