---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/397?category=3&page=3
tags:
  - picoCTF
  - ReverseEngineering
  - x86_64
---

# Solution

This challenge is quite difficult and more advanced than [[GDB baby step 2]] and [[GDB baby step 1]]. To tackle this challenge, we need to use additional memory allocation commands beyond just setting a breakpoint at main. By using commands like `break *(main+addr)`, we can gather more information about memory flow.

The challenge has already told us we should keep an eye on `0x2262c96b`, and `$rbp-0x4` is the only location that holds this value.

```plain
     0x401106 <main+0>         endbr64
     0x40110a <main+4>         push   rbp
     0x40110b <main+5>         mov    rbp, rsp
     0x40110e <main+8>         mov    DWORD PTR [rbp-0x14], edi
     0x401111 <main+11>        mov    QWORD PTR [rbp-0x20], rsi
 →   0x401115 <main+15>        mov    DWORD PTR [rbp-0x4], 0x2262c96b
     0x40111c <main+22>        mov    eax, DWORD PTR [rbp-0x4]
     0x40111f <main+25>        pop    rbp
     0x401120 <main+26>        ret
```

So, we move the locator to `0x401115 <main+15>` to see what's inside the `$rbp-0x4` with `x/4xb $rbp-0x4`.

> [!NOTE]  
> Command `x/4xb` is a convenient command used to check a register's value. Enter the command `x/` prefix, followed by `<integer>x<b|o|d|h>` to perform this action.

![](https://i.imgur.com/yFsqQ6a.png)![](https://i.imgur.com/7DFYvTB.png)

Finally, we retrieve four bytes with the content `0x6b 0xc9 0x62 0x22`, and the flag is `picoCTF{0x6bc96222}`.
