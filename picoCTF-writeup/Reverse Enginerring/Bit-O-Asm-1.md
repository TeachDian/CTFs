---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/391?category=3&page=2
tags:
  - picoCTF
  - ReverseEngineering
  - x86_64
---

# Solution

The challenge provides an assembly code and asks for the value of `eax`.

According to this [documentation](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html), we then know that the `mov eax, [ebx]` instruction moves the value in `ebx` into `eax`, which means `eax = ebx`.

The submit form is asking for the decimal content. It moves `0x30` into `eax`, which is `48`.

$$30_{\text{(16)}} = 48_{\text{(10)}}$$

Therefore, the flag is:

```
picoCTF{48}
```
