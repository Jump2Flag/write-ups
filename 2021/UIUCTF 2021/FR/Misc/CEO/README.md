# CEO

![CEO](https://i.imgur.com/sRn1Ndo.png)

Dans ce challenge on nous donne un fichier ``megacorp-01.cap`` contenant le handshake d'un certain point d'accès, suffit donc de lancer un outils permettant de cracker le mot de  passe contenu dans la capture :

```
$ aircrack-ng megacorp-01.cap -w rockyou.txt
Opening megacorp-01.cap wait...
Read 1914 packets.

   #  BSSID              ESSID                     Encryption

   1  E4:95:6E:45:90:24  joesheer                  WPA (1 handshake)

Choosing first network as target.

Opening megacorp-01.cap wait...
Read 1914 packets.

1 potential targets

                              Aircrack-ng 1.5.2 


      [00:12:53] 3325080/9822769 keys tested (2559.76 k/s)

      Time left: 42 minutes, 19 seconds                         33.85%

                        KEY FOUND! [ nanotechnology ]


      Master Key     : E5 CF 85 D1 09 1B EB 88 92 4E FD 6A 9E 4F FE FB
                       64 8F 19 06 40 F9 12 EC 73 6F CA F4 D9 FA 47 44

      Transient Key  : 44 E4 65 83 FE 2D 4B 6E C7 DB A9 2F CF 7A 1C 2A
                       E3 15 EA E1 AD D8 5E 44 B7 07 A7 85 51 B2 55 B8
                       A1 AF 58 88 87 B6 51 3B CE 88 69 B2 EC 5F 41 D4
                       F6 04 9E FB E1 7A E4 5D 45 FF 2A 0F E6 23 A7 BC

      EAPOL HMAC     : B5 F1 3A A9 56 CF B1 E3 14 A9 07 A9 E3 19 70 48
```

Flag : ``uiuctf{nanotechnology}``
