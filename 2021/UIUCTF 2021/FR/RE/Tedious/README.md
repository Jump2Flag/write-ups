# Tedious

![](https://i.imgur.com/HPSce9G.png)

Dans ce challenge, on nous donne un binaire ELF x64 not stripped.

Analysons le binaire :

<img src="https://i.imgur.com/UeB4gJg.png" title="" alt="" width="378">

Au vue de la tête du graphe, on peut voir que plusieurs opérations sont effectué à la suite, lettre par lettre, afin de vérifier la validité du flag.

Pour ce facilité la tâche au vue du nombre d'instructions, nous allons ouvrir le binaire avec Ghidra et regarder ce que l'on a dans la fonction main avec le décompilateur :

```c

undefined8 main(void)

{
  long lVar1;
  undefined8 *puVar2;
  long in_FS_OFFSET;
  byte bVar3;
  int local_dc;
  undefined8 local_d8;
  undefined4 local_d0;
  undefined4 local_cc;
  undefined4 local_c8;
  undefined4 local_c4;
  undefined4 local_c0;
  undefined4 local_bc;
  undefined4 local_b8;
  undefined4 local_b4;
  undefined4 local_b0;
  undefined4 local_ac;
  undefined4 local_a8;
  undefined4 local_a4;
  undefined4 local_a0;
  undefined4 local_9c;
  undefined4 local_98;
  undefined4 local_94;
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  undefined4 local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  byte local_38 [40];
  long local_10;
  
  bVar3 = 0;
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts("Enter the flag:");
  fgets((char *)local_38,0x28,stdin);
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x3b ^ 0x38;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x12 ^ 0xfd;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 4 ^ 0x50;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x13 ^ 0x68;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0xc ^ 0x79;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0xbc ^ 0xa0;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 10 ^ 0xcd;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0xb8 ^ 0x5a;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0xb ^ 0xbd;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] - 0x1f ^ 0xed;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x45 ^ 0x22;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0xbe ^ 0x6b;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] - 0x26 ^ 0x6b;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x76 ^ 0xfa;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x16 ^ 0x6b;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0xb5 ^ 0x6b;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x8d ^ 100;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 10 ^ 0xab;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 99 ^ 0x1b;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] - 0x2b ^ 0xf0;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  local_dc = 0;
  while (local_dc < 0x27) {
    local_38[local_dc] = local_38[local_dc] + 0x75 ^ 0x6b;
    local_dc = local_dc + 1;
  }
  local_38[local_dc] = 0;
  lVar1 = 0x14;
  puVar2 = &local_d8;
  while (lVar1 != 0) {
    lVar1 = lVar1 + -1;
    *puVar2 = 0;
    puVar2 = puVar2 + (ulong)bVar3 * 0x1ffffffffffffffe + 1;
  }
  local_d8._0_4_ = 0x4d; //encrypted_flag 
  local_d8._4_4_ = 0xb9;
  local_d0 = 0x4d;
  local_cc = 0xb;
  local_c8 = 0xd4;
  local_c4 = 0x66;
  local_c0 = 0xe3;
  local_bc = 0x29;
  local_b8 = 0xb8;
  local_b4 = 0x4d;
  local_b0 = 0xdf;
  local_ac = 0x66;
  local_a8 = 0xb8;
  local_a4 = 0x4d;
  local_a0 = 0xe;
  local_9c = 0xc4;
  local_98 = 0xdf;
  local_94 = 0xd4;
  local_90 = 0x14;
  local_8c = 0x3b;
  local_88 = 0xdf;
  local_84 = 0x66;
  local_80 = 0x2c;
  local_7c = 0x14;
  local_78 = 0x47;
  local_74 = 0xdf;
  local_70 = 0xb7;
  local_6c = 0xb8;
  local_68 = 0xb7;
  local_64 = 0xdf;
  local_60 = 0x47;
  local_5c = 0x4d;
  local_58 = 0xa4;
  local_54 = 0xdf;
  local_50 = 0x32;
  local_4c = 0xb8;
  local_48 = 0xea;
  local_44 = 0xf5;
  local_40 = 0x92;
  local_dc = 0;
  do {
    if (0x26 < local_dc) {
      printf("GOOD JOB!");
LAB_001019db:
      if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
      return 0;
    }
    if ((uint)local_38[local_dc] != *(uint *)((long)&local_d8 + (long)local_dc * 4)) {
      printf("WRONG!");
      goto LAB_001019db;
    }
    local_dc = local_dc + 1;
  } while( true );
}



```

On voit que beaucoup d'opération sont effectué, ce qui modifiera notre input : ``local_38``.

Une fois toute les opérations effectué sur les items du tableau ``local_38`` ,  le programme compare les items de ``local_38`` et celle de ``local_d8`` à ``local_40``.

En gros : ``encrypted_flag`` = `{0x4d,0xb9,0x4d,0xb,0xd4,0x66,0xe3,0x29,0xb8,0x4d,0xdf,0x66,0xb8,0x4d,0xe,0xc4,0xdf,0xd4,0x14,0x3b,0xdf,0x66,0x2c,0x14,0x47,0xdf,0xb7,0xb8,0xb7,0xdf,0x47,0x4d,0xa4,0xdf,0x32,0xb8,0xea,0xf5,0x92}` .

Et donc notre input : ``local_38``, doit être égal à `encrypted_flag` .



Maintenant il suffit de faire un script permettant de trouver le flag en effectuant ces mêmes opérations et en récupérant les caractères donnant les memes valeurs que dans ``encrypted_flag``.

J'ai décidé de le faire en python mais attention l'input : ``local_38`` est un type bytes, il faut donc récupérer le LSB des valeurs de `local_38` :

```python
import string

encrypted_flag = [0x4d,0xb9,0x4d,0xb,0xd4,0x66,0xe3,0x29,0xb8,0x4d,0xdf,0x66,0xb8,0x4d,0xe,0xc4,0xdf,0xd4,0x14,
0x3b,0xdf,0x66,0x2c,0x14,0x47,0xdf,0xb7,0xb8,0xb7,0xdf,0x47,0x4d,0xa4,0xdf,0x32,0xb8,0xea,0xf5,0x92]

flag = [0]*0x27

for i in range(0x27):
    for char in string.printable:
        flag[i] = ord(char)
        flag[i] = (flag[i] + 0x3b ^ 0x38) % 256
        flag[i] = (flag[i] + 0x12 ^ 0xfd) % 256
        flag[i] = (flag[i] + 4 ^ 0x50) % 256
        flag[i] = (flag[i] + 0x13 ^ 0x68) % 256
        flag[i] = (flag[i] + 0xc ^ 0x79) % 256
        flag[i] = (flag[i] + 0xbc ^ 0xa0) % 256
        flag[i] = (flag[i] + 10 ^ 0xcd) % 256
        flag[i] = (flag[i] + 0xb8 ^ 0x5a) % 256
        flag[i] = (flag[i] + 0xb ^ 0xbd) % 256
        flag[i] = (flag[i] - 0x1f ^ 0xed) % 256
        flag[i] = (flag[i] + 0x45 ^ 0x22) % 256
        flag[i] = (flag[i] + 0xbe ^ 0x6b) % 256
        flag[i] = (flag[i] - 0x26 ^ 0x6b) % 256
        flag[i] = (flag[i] + 0x76 ^ 0xfa) % 256
        flag[i] = (flag[i] + 0x16 ^ 0x6b) % 256
        flag[i] = (flag[i] + 0xb5 ^ 0x6b) % 256
        flag[i] = (flag[i] + 0x8d ^ 100) % 256
        flag[i] = (flag[i] + 10 ^ 0xab) % 256
        flag[i] = (flag[i] + 99 ^ 0x1b) % 256
        flag[i] = (flag[i] - 0x2b ^ 0xf0) % 256
        flag[i] = (flag[i] + 0x75 ^ 0x6b) % 256
        if flag[i] == encrypted_flag[i]:
            flag[i] = char
            break

print(f"[+] FLAG : {''.join(flag)}")
```

```
$ python3 solve.py
[+] FLAG : uiuctf{y0u_f0unD_t43_fl4g_w0w_gud_j0b}
```

Youpi !! On peut maintenant valider le challenge avec le flag : ``uiuctf{y0u_f0unD_t43_fl4g_w0w_gud_j0b}``.
