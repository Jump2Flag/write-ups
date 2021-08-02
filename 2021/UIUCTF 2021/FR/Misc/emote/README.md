# Emote

![emote](https://i.imgur.com/XDF96Q0.png)

Dans ce challenge, on nous dit qu'une chaine de caractères a été transformé en image et que l'image a été partagé sur discord.

On va donc sur le serveur discord de l'[UIUCTF 2021](https://discord.gg/E6BAsrhg9B).

Une fois dessus on voit qu'il y a une émote `:emote:` de disponible qui a le même nom que le challenge et qui est suspecte, c'est certainement une décomposition pixelisé, le blanc = 1 et la noir = 0, ce qui nous fera une représentation binaire et donc une correspondance en caractères de la table ascii.

On télécharge donc l'image et on la décode sur [dcode](https://www.dcode.fr/image-binaire) :

![dcode-decomp-pix](https://i.imgur.com/23WRvPx.png)

On obtient un code binaire, suffit de convertir tous ca en caractères via la table ascii et on obtient le flag : ``uiuctf{staring_at_pixels_is_fun}``.












