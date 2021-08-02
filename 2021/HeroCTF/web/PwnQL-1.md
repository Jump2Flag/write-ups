![Screen](../img/Pasted%20image%2020210426184206.png)

D'après l'énoncé, il s'agit clairement d'une SQLi.
Quand on va sur le site, en fouillant dans l'html on peut voir un commentaire.

![Screen](../img/Pasted%20image%2020210426184304.png)

Le fichier contient le code suivant:
```php
<?php

require_once(__DIR__  . "/config.php");

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT * FROM users WHERE username = :username AND password LIKE :password;";
    $sth = $db->prepare($sql, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
    $sth->execute(array(':username' => $username, ':password' => $password));
    $users = $sth->fetchAll();

    if (count($users) === 1) {
        $msg = 'Welcome back admin ! Here is your flag : ' . FLAG;
    } else {
        $msg = 'Wrong username or password.';
    }
}
```

Puisqu'on doit se connecter en tant qu'admin, il ne reste qu'à trouver le mot de passe. Ou explotier une faille. La ligne 
`$sql = "SELECT * FROM users WHERE username = :username AND password LIKE :password;";` est exploitable.
Le dev utilise `LIKE`, en se renseignant un peu sur [w3s](https://www.w3schools.com/sql/sql_like.asp) on appprend plusieures choses.
Ce qui nous intéresse, c'est la wildcard `%`

![Screen](../img/Pasted%20image%2020210426184729.png)

Puisque `a%` renvoie tous les résultats commençant par `a`, `%` doit renvoyer tous les résultats. Et puisque `admin` n'a qu'un mot de passe, il suffit d'enter admin:%

![Screen](../img/Pasted%20image%2020210426184854.png)
