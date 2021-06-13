# Pincrack

## Énoncé :

![](/home/fayred/.var/app/com.github.marktext.marktext/config/marktext/images/2021-06-13-16-49-35-image.png)

Aussitôt dl, on lance un ltrace :

```shell
$ ltrace ./pincrack 654321
strlen("654321")                                                                                           = 6
puts("[*] Thanks for your try! I am ch"...[*] Thanks for your try! I am checking...
)                                                                = 42
SHA1_Init(0x7ffdfd082200, 0x7ffdfd0822b0, 0x7ffdfd0822b0, 0x7fa2b7fa11e7)                                  = 1
SHA1_Update(0x7ffdfd082200, 0x7ffdfd082292, 6, 0x7ffdfd082292)                                             = 1
SHA1_Final(0x7ffdfd0822b0, 0x7ffdfd082200, 0x7ffdfd082200, 0x31363432)                                     = 1
crypto_scrypt(0x7ffdfd08228c, 6, 0x55ebe0ad7080, 16)                                                       = 0
strncmp("\234\376\237\210\3762\256\016\035\331\252H\375+\360\025\005\372\356_", "\323\377\356\324\a\255z\326`n\247c\\\342\004\357\271]\217\020", 20) = -55
puts("Nope."Nope.
)                                                                                              = 6
exit(0 <no return ...>
+++ exited (status 0) +++
```

On voit que lors que l'execution, le programme fait appel à des fonctions pour hacher le pin entré en sha1 et le compare avec ``strcmp`` à un autre hash.

On ce doute bien que la seconde chaine est le hash du pin à trouver.

On va donc reconstituer le hash en hexa et trouver à quelle valeur celui-ci correspond.

```python
In [1]: "".join([hex(ord(i))[2:].zfill(2) for i in "\323\377\356\324\a\255z\326`n\247c\\\342\004\357\271]\217\020"])
Out[2]: 'd3ffeed407ad7ad6606ea7635ce204efb95d8f10'
```

On va ensuite sur https://crackstation.net/ et on trouve la correspondance de celui-ci : ``667018``

![](/home/fayred/.var/app/com.github.marktext.marktext/config/marktext/images/2021-06-13-17-01-22-image.png)



Maintenant on file le pin trouvé au programme en pensant que c'est le bon, sauf que ...

```shell
$ ltrace ./pincrack 667018
strlen("667018")                                                                                           = 6
puts("[*] Thanks for your try! I am ch"...[*] Thanks for your try! I am checking...
)                                                                = 42
SHA1_Init(0x7fffabba5240, 0x7fffabba52f0, 0x7fffabba52f0, 0x7f9ea899b1e7)                                  = 1
SHA1_Update(0x7fffabba5240, 0x7fffabba52d2, 6, 0x7fffabba52d2)                                             = 1
SHA1_Final(0x7fffabba52f0, 0x7fffabba5240, 0x7fffabba5240, 0x38363731)                                     = 1
crypto_scrypt(0x7fffabba52cc, 6, 0x55e0ac47a080, 16)                                                       = 0
strncmp("j\367|\257y\v\326\231\234X3K\312\314q?\030u\2755", "\323\377\356\324\a\255z\326`n\247c\\\342\004\357\271]\217\020", 20) = -105
puts("Nope."Nope.
)                                                                                              = 6
exit(0 <no return ...>
+++ exited (status 0) +++
```

**CA NE MARCHE PAS !**

A partir de la je me dis que le pin subit certainement quelques modifications avant de passer dans le strcmp.

Je vérifie donc la correspondance en hexa de ``j\367|\257y\v\326\231\234X3K\312\314q?\030u\2755``

Et là surprise :

```python
In [3]: "".join([hex(ord(i))[2:].zfill(2) for i in "j\367|\257y\v\326\231\234X3K\312\314q?\030u\2755"])
Out[4]: '6af77caf790bd6999c58334bcacc713f1875bd35'
```

![](/home/fayred/.var/app/com.github.marktext.marktext/config/marktext/images/2021-06-13-17-08-30-image.png)

``6af77caf790bd6999c58334bcacc713f1875bd35``  =  ``061768``

On passe de 667018 à 061768, Mmmmmmh, les chiffres donc mélangé la manière suivant :




```
a=667018
a=a[3]+a[1]+a[4]+a[2]+a[0]+a[5]
```

Il faut donc faire le mélange jusqu'à retomber sur ``667018`` et récupéré la valeur précédente.

```python
In [51]: a="667018"
    ...: while 1:
    ...:     a=a[3]+a[1]+a[4]+a[2]+a[0]+a[5]
    ...:     if a == "667018":
    ...:         break
    ...:     print(a)
    ...: 
061768
766108
160678 # le bon PIN
```

On récupère obtiens donc le PIN : ``160678``

Manque plus qu'à tester le PIN sur le binaire :

```shell
$ ltrace ./pincrack 160678
strlen("160678")                                                                                           = 6
puts("[*] Thanks for your try! I am ch"...[*] Thanks for your try! I am checking...
)                                                                = 42
SHA1_Init(0x7ffca276a000, 0x7ffca276a0b0, 0x7ffca276a0b0, 0x7f45582b11e7)                                  = 1
SHA1_Update(0x7ffca276a000, 0x7ffca276a092, 6, 0x7ffca276a092)                                             = 1
SHA1_Final(0x7ffca276a0b0, 0x7ffca276a000, 0x7ffca276a000, 0x38313037)                                     = 1
crypto_scrypt(0x7ffca276a08c, 6, 0x555e5fbfe080, 16)                                                       = 0
strncmp("\323\377\356\324\a\255z\326`n\247c\\\342\004\357\271]\217\020", "\323\377\356\324\a\255z\326`n\247c\\\342\004\357\271]\217\020", 20) = 0
EVP_CIPHER_CTX_new(0x555e5fbfe040, 48, 0x7ffca276a0d0, 0x7ffca276a0a0)                                     = 0x555e61b8c000
EVP_aes_256_cbc(0x555e61b8c000, 0, 0x555e61b8c080, 0x555e61b8c080)                                         = 0x7f4558648500
EVP_DecryptInit_ex(0x555e61b8c000, 0x7f4558648500, 0, 0x7ffca276a0d0)                                      = 1
EVP_DecryptUpdate(0x555e61b8c000, 0x7ffca276a0f0, 0x7ffca276a050, 0x555e5fbfe040)                          = 1
EVP_DecryptFinal_ex(0x555e61b8c000, 0x7ffca276a110, 0x7ffca276a050, 0x7ffca276a110)                        = 1
EVP_CIPHER_CTX_free(0x555e61b8c000, 0x7ffca276a110, 12, 12)                                                = 0
printf("Good PIN! Here is your flag:\n%s\n"..., "THCon21{Dud3_Y0u_cR4Ck3d_mY_53cU"...Good PIN! Here is your flag:
THCon21{Dud3_Y0u_cR4Ck3d_mY_53cUrE_P1n_C0D3!}
)                     = 75
exit(0 <no return ...>
+++ exited (status 0) +++
```

Bingo !! On a donc le flag : 

``THCon21{Dud3_Y0u_cR4Ck3d_mY_53cUrE_P1n_C0D3!}``

