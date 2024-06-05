---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/395?category=3&page=3
tags:
  - picoCTF
  - ReverseEngineering
  - x86_64
---

# Solution

```shell
$ gdb --nx debugger0_a
$ (gdb) break main
$ (gdb) r
$ (gdb) n
$ (gdb) p $eax
$2 = 549698
```

### Explain

I think this challenge is just asking us the value of `$eax` after main function finished.

And that's why we should run after `main` function with `next` command, and then printout the registry's value.

the flag is: `picoCTF{549698}`

> [!WARNING]  
> Don't use gdb layout command while running both gdb TUI and gef TTY. gef TTY breaks TUI for no reason.