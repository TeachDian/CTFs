---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/368?category=3&page=1&search=Ready%20Gladiator%200
tags:
  - picoCTF
  - ReverseEngineering
---

# Solution

> [!CAUTION] ~~I actually don't know how I solve it.~~

> [!IMPORTANT] I solved it and fully understand
> CoreWar is a well developed game and it has a rule:
>
> > If you perform incorrect action, you lose the round then a game.

I just replace the `mov 0 1` to `mov 1 1` then I won the game.

```shell
$ cat imp.red
;redcode
;name Imp Ex
;assert 1
mov 1, 1
end
```

```shell
$ nc saturn.picoctf.net 60439 < imp.red
;redcode
;name Imp Ex
;assert 1
mov 1, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 1, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_be33d1f6}
```
