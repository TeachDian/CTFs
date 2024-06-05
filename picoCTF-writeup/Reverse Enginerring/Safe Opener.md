---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/294?category=3&page=2
tags:
  - picoCTF
  - ReverseEngineering
---

# Solution

This challenge provides a Java source file, you then open it and decode the hash inside the sub-function (which is `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`), and that's the flag.

The flag is :

```plain
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```

## Base64 decoding

If you prefer decode with Python scripting than using online tools.
Then the code for decoding is:

```python
import base64
print(base64.b64decode("cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"))
```

Or you can even use inline Python script with `-c` argument:

```shell
python3 -c 'val: str = ""; import base64; print(base64.b64decode(val))'
```

Remember to fill the `val` with your Base64 string.
