---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/271?category=3&page=4
tags:
  - picoCTF
  - ReverseEngineering
  - java
---

# Solution

I reverse the `.class` with ghidra, inside main function is a bunch of statement used to check input string with correct password character by character.

And after combine all the characters, the flag is:

```
picoCTF{700l1ng_r3qu1r3d_738cac89}
```
