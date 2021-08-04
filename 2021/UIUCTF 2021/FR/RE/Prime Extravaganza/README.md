# Prim Extravaganza

![](https://i.imgur.com/lCW44xW.png)

Pour ce challenge, on nous donne un ELF x64, not stripped.

Analysons ce binaire :

![](https://i.imgur.com/dGAoLTt.png)

Pour commencer on voit qu'une boucle est effectué 5 fois. Dans cette boucle on a plusieurs fonctions qui sont appelé, dont ``scanf`` qui va ce charger de récupérer la valeur qu'on aura rentré.

On voit que la valeur rentré dans ``scanf`` sera stocké dans ``rbp - 0x54`` et le retour de ``scanf`` dans ``rbp - 0x48``.

Donc si ``rbp - 0x48`` ne renvoi pas 1, le binaire affiche ``Bad input`` et stop le programme (en gros si la valeur rentré n'est pas un unsigned int).

Sinon le programme passe à la suite.

Après le programme regarde si notre input est supérieur à ``0x13a6`` (100 000), si c'est le cas pareil il renvoi `Bad input` sinon il passe à la suite.

Ensuite le programme effectue plusieurs opérations notamment l'opération ``mov edx, dword [var_54h]`` et  ``mov dword [rbp + rax*4 - 0x40], edx``  .

On voit donc que notre input est move dans ``edx`` puis dans ``dword [rbp + rax*4 - 0x40]`` 

Ensuite une fonction nommé ``getMaxPrimeFactor`` est appélé ainsi que ``printf`` qui affiche le retour de cette fonction prenant en argument notre input (on va pas s'interesser plus que ca à la fonction ``getMaxPrimeFactor``, car on a pas besoin de savoir ce qu'elle fait pour résoudre le challenge).

Et grosso modo on répète tous ca 5fois (on aura donc a rentré 5 fois un nombre entre 0 et 100 000).

Une fois sortie de la boucle on continue vers ``0x000012e1`` :

![](https://i.imgur.com/VEjU072.png)

Ici on voit qu'une boucle est effectué 5 fois encore si `eax` vaut 0 à ``0x00001308``  sinon le boucle s'arrête et le programme est stoppé.

Si les 5 boucles sont effectué alors on aura le droit au jolie message : ``Congratulations, you found the secret inputs!``.

Il faut donc à chaque fois que ``eax`` soit égal à 0 et on voit que nos inputs (``dword [rbp + rax*4 - 0x40]``) sont placé un par un dans ``eax`` puis divisé par une valeur stocké dans ``rbp - 0x44``.

Il faut donc connaitre la valeur stocké dans ``rbp - 0x44`` car ``edx`` est move dans ``eax`` juste avant ``test eax, eax`` et  ``edx`` correspond au reste de la division, nos input doivent donc être égal aux valeurs stocké dans ``rbp - 0x44``.

On voit aussi :

```asm
mov    eax, dword[var_4ch]
add    eax, 1
imul   eax, eax, 0x4d29
mov    dword[var_4ch]
```

La valeur stocké dans ``rbp - 0x44`` est donc égal à (``rbp - 0x4c`` + 1) * 0x4d29.

Sachant que ``rbp - 0x4c`` vaut 4 et est décrémenté à chaque fois, suffit de faire un simple petit script permettant de connaitre les valeurs stocké dans `rbp - 0x44`  (+``uiuctf{md5(sum_of_secret_inputs)}`` pour avoir le flag)  :

```python
import hashlib

values = [0]*5
for i in range(4, -1, -1):
    values[i] = (i + 1 )*0x4d29 # reverse because of LIFO
print(f"[+] VALUES : {values}")
flag = "uiuctf{"+hashlib.md5(str(sum(values)).encode()).hexdigest()+"}"
print(f"[+] FLAG : {flag}")
```

```
$ python3 solve.py
[+] VALUES : [19753, 39506, 59259, 79012, 98765]
[+] FLAG : uiuctf{627360eb8aa0da45ff04a514dab40e54}
```

On a le flag : ``uiuctf{627360eb8aa0da45ff04a514dab40e54}`` mais pour la beauté du truc, on va quand même executer le binaire et entrer les valeurs trouvé : 

```
$ ./challenge
Enter a number smaller than 100000: 19753
Max prime factor: 19753
Enter a number smaller than 100000: 39506
Max prime factor: 19753
Enter a number smaller than 100000: 59259
Max prime factor: 19753
Enter a number smaller than 100000: 79012
Max prime factor: 19753
Enter a number smaller than 100000: 98765
Max prime factor: 19753
Congratulations, you found the secret inputs!
```

Bingo !! Tous marche comme sur des roulettes, on peut valider le challenge avec le flag : ``uiuctf{627360eb8aa0da45ff04a514dab40e54}`` !! 


