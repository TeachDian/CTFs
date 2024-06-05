---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/60?category=3&page=1&search=vault
tags:
  - picoCTF
  - ReverseEngineering
  - substitution
---

# Solution

This challenge substituted the flag's position, we then write a reverse function to decode original flag.

```python
def reverse_substitution(substituted):
    if len(substituted) != 32:
        return False

    buffer = [''] * 32

    # First loop (reverse of the fourth loop in substitution)
    for i in range(31, 16, -2):
        buffer[i] = substituted[i]

    # Second loop (reverse of the third loop in substitution)
    for i in range(16, 32, 2):
        buffer[i] = substituted[46 - i]

    # Third loop (reverse of the second loop in substitution)
    for i in range(8, 16):
        buffer[i] = substituted[23 - i]

    # Fourth loop (reverse of the first loop in substitution)
    for i in range(8):
        buffer[i] = substituted[i]

    return ''.join(buffer)

substituted_string = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
original_string = reverse_substitution(substituted_string)
print("picoCTF{" + original_string + "}")
```

```plain
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
```
