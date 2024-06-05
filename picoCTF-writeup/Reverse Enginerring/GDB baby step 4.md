---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/398?category=3&page=3
tags:
  - picoCTF
  - ReverseEngineering
  - x86_64
---

# Solution

1. Set breakpoint at `main`
2. Inspect the function name as $f_{1}$
3. Set breakpoint at $f_{1}$
4. Analysis instructions, especially `imul`

The flag is: `picoCTF{12905}`

![](https://i.imgur.com/Ci110p7.png)
