---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/12?category=3&page=1&search=vault
tags:
  - picoCTF
  - ReverseEngineering
---

# Solution

This challenge provides a Java code and aims for the player to recombine a character array using `charAt()`.

To solve this, simply recombine all the characters to get the flag. Finally, the flag will be:

```plain
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
```

> [!NOTE]  
>
> ## YOU
>
> here are a sequence of charAt(index), now according the index (ascending) sort the correct plaintext for me:
>
> ```java
> public boolean checkPassword(String password) {
> ...
> ```
>
> Finally, left all the [[java]] code, leave the character alone.
> And combine them into once sequence of string.
>
> ## ChatGPT
>
> The given [[Java]] code specifies certain characters at specific indices in a password string. Let's sort and combine these characters into a single plaintext sequence according to their indices.
>
> Here are the characters at their respective indices:
>
> 1. `password.charAt(0) == 'd'`
> 2. `password.charAt(1) == '3'`
> 3. `password.charAt(2) == '5'`
> 4. `password.charAt(3) == 'c'`
> 5. `password.charAt(4) == 'r'`
> 6. `password.charAt(5) == '4'`
> 7. `password.charAt(6) == 'm'`
> 8. `password.charAt(7) == 'b'`
> 9. `password.charAt(8) == 'l'`
> 10. `password.charAt(9) == '3'`
> 11. `password.charAt(10) == '_'`
> 12. `password.charAt(11) == 't'`
> 13. `password.charAt(12) == 'H'`
> 14. `password.charAt(13) == '3'`
> 15. `password.charAt(14) == '_'`
> 16. `password.charAt(15) == 'c'`
> 17. `password.charAt(16) == 'H'`
> 18. `password.charAt(17) == '4'`
> 19. `password.charAt(18) == 'r'`
> 20. `password.charAt(19) == '4'`
> 21. `password.charAt(20) == 'c'`
> 22. `password.charAt(21) == 'T'`
> 23. `password.charAt(22) == '3'`
> 24. `password.charAt(23) == 'r'`
> 25. `password.charAt(24) == '5'`
> 26. `password.charAt(25) == '_'`
> 27. `password.charAt(26) == 'f'`
> 28. `password.charAt(27) == 'f'`
> 29. `password.charAt(28) == '6'`
> 30. `password.charAt(29) == '3'`
> 31. `password.charAt(30) == 'b'`
> 32. `password.charAt(31) == '0'`
>
> Combining these characters into a single string:
>
> ```plain
> d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0
> ```
>
> This is the plaintext password derived from the given Java code.
