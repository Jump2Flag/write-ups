# hvhpgs{synt}

![](https://i.imgur.com/R9P06ik.png)

Dans ce challenge on nous donne un binaire ELF 64bits, not stripped.

Pour commencer, le binaire demande d'entrer le flag sous la forme : ``flag_words_with_underscores_and_letters``.

On entre donc cette chaine pour tester : 

```
$ ./chal
enter input with the form: flag_words_with_underscores_and_letters
flag_words_with_underscores_and_letters
very funny
```

Le programme nous renvois ``very funny``.

Essayons maintenant de rentrer une autre chaine de caractères :

```
$ ./chal
enter input with the form: flag_words_with_underscores_and_letters
test
incorrect
```

Le binaire nous renvoi maintenant incorrect.

Analysons la partie suivant la récupération de l'input :

![](https://i.imgur.com/PJMTRQG.png)

Ici nous pouvons voir que l'on fait une boucle ``0x538`` (1337) fois et dans cette boucle on appel la fonction ``rot`` et ``shift``, après la boucle terminé le binaire compare la chaine entré mélangé avec ``rot`` et ``shift`` à ``azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o``.

Si les deux chaines de caractères ne sont pas les mêmes, le binaire va alors ensuite comparer notre input mélangé à ``qe_mzp_xqffqderxms_iadpe_iuft_gzpqdeoad`` et si ce sont les mêmes, le binaire va nous renvoyer ``very funny``, ce qui correspond à la réponse obtenu lorsque l'on rentre ``flag_words_with_underscores_and_letters`` donc ``flag_words_with_underscores_and_letters`` = ``qe_mzp_xqffqderxms_iadpe_iuft_gzpqdeoad``, mais ce n'est pas ce qui nous interesse ici.

Sinon si les deux chaines de caractères sont les mêmes, le binaire va alors finir par jump à ``0x000016a5`` :

![](https://i.imgur.com/91Biu4t.png)

Et nous voyons ici que c'est la partie qui s'éxecute lorsque l'on a trouvé le flag (cela met l'input entre ``uiuctf{`` et ``}``).

Nous devons donc retrouver le flag à partir de ``azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o``.

Au vu du nom des fonctions, on ce doute que de simple rotations et décalages sont effectué pour rendre le flag illisible, on essai donc de voir ce que donne ``azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o`` une fois décodé avec du code césar sur [dcode](https://www.dcode.fr/caesar-cipher).

Cela nous donne : ``onsider_the_question_can_machines_thinki_propose_to_c`` avec un rot à 12. On voit clairement que c'est une phrase compréhensible, suffit donc d'appliquer le shift.

On voit bien que la partie ``thinki`` ne devrait pas être collé mais séparé avec un ``_`` on arrange donc la chaine de caractère et cela nous donne : ``i_propose_to_consider_the_question_can_machines_think``.

Testons cette chaine de caractères dans le binaire : 

```
$ ./chal
enter input with the form: flag_words_with_underscores_and_letters
i_propose_to_consider_the_question_can_machines_think
uiuctf{i_propose_to_consider_the_question_can_machines_think}
```

Youpi !! On peut maintenant valider le challenge avec le flag : ``uiuctf{i_propose_to_consider_the_question_can_machines_think}``.






