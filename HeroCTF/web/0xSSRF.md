![Screen](../img/Pasted%20image%2020210426184918.png)
Le titre est plutôt clair, il faut performer une SSRF.
Une fois sur le site on remarque rapidement qu'il y a une URL pour obtenir le flag. Evidemment, c'est accessible uniquement via `127.0.0.1`
![Screen](../img/Pasted%20image%2020210426184956.png)

Pour réussir le challenge, il suffit de trouver un bypass à l'ip `127.0.0.1`.
`http://0` suffit! Puisque le chall est sur le port 3000, il faut l'ajouter à l'url

Payload final:
`http://0:3000/flag`

![Screen](../img/Pasted%20image%2020210426185136.png)
