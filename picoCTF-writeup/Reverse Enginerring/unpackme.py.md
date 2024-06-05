---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/314?category=3&page=2
tags:
  - picoCTF
  - ReverseEngineering
  - packing
---

# Solution

This challenge provides a Python code, and simply comment out the final line and print out `plain`. The flag appears inside the output string.

```python
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkzWGWvEp8gLI9AcIn5o-ahDUwkTvM6EwF7YYMZlE-_Gf9rcNYjxIgX4b0ltY6bcxKarib2ds6POclRwCwhsRb1LOXVt4Q3ePtMY4BmHFFZlIHLk05CjwigT7hiI9p3sH9e7Cpk1uO90xbHbuy-mfi3nkmn411aBgwxyWpJvykpkuBIG_nty6zbox3UhbB85TOis0TgM0zG4ht0-GUW4wTq2_5-wkw3kV1ZAisLJHzF-Z9oLMmwFZU0UCAcHaBTGDF5BnVLmUeCGTgzVLSNn6BmB61Yg=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
print(plain)
# exec(plain.decode())
```

```bash
$ py unpackme.flag.py
b"\\npw = input('What\\\\'s the password? ')\\n\\nif pw == 'batteryhorse':\\n  print('picoCTF{175_chr157m45_85f5d0ac}')\\nelse:\\n  print('That password is incorrect.')\\n\\n"
```

```plain
picoCTF{175_chr157m45_85f5d0ac}
```

## Reference

- [Fernet (symmetric encryption) — Cryptography 43.0.0.dev1 documentation](https://cryptography.io/en/latest/fernet/)
- [Fernet (symmetric encryption) using Cryptography module in Python - GeeksforGeeks](https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/)
