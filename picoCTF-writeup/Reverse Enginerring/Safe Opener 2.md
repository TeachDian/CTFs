---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/375?category=3&page=2
tags:
  - picoCTF
  - ReverseEngineering
---

# Solution

Challenge has a `.class` file; it is a program that was compiled using Java. Then, to get the flag, we need to decompile the executable to check what's inside the program.

After we inspect function used to handle password check, the flag is inside of it.

```plain
picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_de45efd6}
```
