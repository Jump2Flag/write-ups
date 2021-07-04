# Strange File

Dans ce challenge en stéganographie, on nous donne un fichier ``74df9ed7b79cfcbca84002619b670802.png``.

Au vu de l'extension on se doute que le fichier est une image, cepedant elle ne charge pas, on se dit donc que c'est certainement xoré.

Pour trouver la clé avec lequel l'image a été xoré, il nous faut tout d'abord le header PNG d'une image valide, on dl donc une image PNG valide et on regarde
 le header fournie.

```
$ hd PNG_transparency_demonstration_1.png | head
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
00000010  00 00 03 20 00 00 02 58  08 06 00 00 00 9a 76 82  |... ...X......v.|
00000020  70 00 03 76 3c 49 44 41  54 78 01 ec c6 05 a1 86  |p..v<IDATx......|
00000030  00 18 03 40 dc 4a d3 87  12 14 a0 d3 d0 02 cf e5  |...@.J..........|
00000040  bf fb 64 2b de 01 00 00  00 00 00 00 00 00 00 00  |..d+............|
00000050  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000080  00 00 00 00 00 00 00 20  e5 79 49 aa e7 ea 79 4e  |....... .yI...yN|
00000090  b7 2c 19 8e 6c 8f 1c 9f  3e 1d 39 26 a9 8f ec 8f  |.,..l...>.9&....|
000000a0  eb b6 2d d3 ba a6 2f 1e  49 da 24 75 01 00 f0 cd  |..-.../.I.$u....|

$ hd 74df9ed7b79cfcbca84002619b670802.png | head
00000000  d9 10 3d 34 7a 3a 2a 78  64 50 40 7e 3a 3f 74 62  |..=4z:*xdP@~:?tb|
00000010  72 64 50 eb 73 73 77 af  38 74 64 50 40 f5 70 5e  |rdP.ssw.8tdP@.p^|
00000020  92 30 72 2d 05 3a 27 2b  03 62 51 05 44 20 32 1c  |.0r-.:'+.bQ.D 2.|
00000030  15 1e 5c 55 52 10 29 30  16 53 12 48 59 14 64 50  |..\UR.)0.S.HY.dP|
00000040  38 a9 ae ea 69 a6 97 52  e2 25 8c 4a fd 07 34 70  |8...i..R.%.J..4p|
00000050  40 ea a1 f3 73 cf 66 fd  d2 e2 0f 3b f0 6d 25 18  |@...s.f....;.m%.|
00000060  63 eb cb f9 ba d9 ff e3  0c d4 0c 99 0e 52 43 6f  |c............RCo|
00000070  4c f7 0a 6c 8f 2f bf dc  84 8f bf cf 8a eb 00 8e  |L..l./..........|
00000080  27 fc 4c a5 aa 29 aa 77  bf c8 a8 aa 52 d7 5d 91  |'.L..).w....R.].|
00000090  ac be a4 85 c8 f3 49 9d  1b bf bf 86 94 90 57 d1  |......I.......W.|


```

On compare les 16 premiers octets, on voit qu'on est passé de ``89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52``    à    ``d9 10 3d 34 7a 3a 2a 78 64 50 40 7e 3a 3f 74 62``.

Suffit donc de XOR les deux headers pour espérer retrouver la clé en entier et déchiffrer toute l'image avec.

```python
In [1]: a = "d9 10 3d 34 7a 3a 2a 78 64 50 40 7e 3a 3f 74 62".split(" ")

In [2]: b = "89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52".split(" ")

In [3]: "".join([chr(int(a[i],16) ^ int(b[i], 16)) for i in range(len(a))])
Out[4]: 'P@ssw00rdP@ssw00'

```

On trouve donc la clé ``P@ssw00rd`` on doit maintenant déchiffrer l'image avec.

```python
In [5]: r=open("74df9ed7b79cfcbca84002619b670802.png", "rb").read()

In [6]: key = b"P@ssw00rd"*10000

In [7]: recoverImage = bytearray()
    ...: for i in range(len(r)):
    ...:     recoverImage.append(r[i] ^ key[i])
    ...: 

In [8]: open("recoverImage.png", "wb").write(recoverImage)

```

<img title="" src="https://i.imgur.com/GgXxlnm.png" alt="ff" width="196">

L'image restauré est un qr code, cependant je n'ai pas réussi à trouver un site qui le decode correctement. J'ai donc utilisé mon téléphone.

![https](https://i.imgur.com/xbNJuQN.jpg)

On a donc le flag : ``CYBERTF{H1dD3n_M3Ss4g3_Fr0m_G4r1z0V}`` !!


