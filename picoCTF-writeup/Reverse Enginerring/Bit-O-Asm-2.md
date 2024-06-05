---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/392?category=3&page=3
tags:
  - picoCTF
  - ReverseEngineering
  - x86_64
---

# Solution

The challenge involves setting the value `0x9fe1a` in the `$eax` register. This value is first written to `rbp-0x4` and subsequently moved to the `$eax` register.

The flag is:

```
picoCTF{654874}
```
