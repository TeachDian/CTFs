---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/436?page=1&search=sans
tags:
  - picoCTF
  - ReverseEngineering
---

# Solution

This challenge provides ELF file, which we shall decompile it and then see what’s inside.

I used IDA64 to analyze the file, and then I searched up main, there are bunch of main procedures we could inspect.

![procedures|300](https://i.imgur.com/9HKhTwE.png)

For this challenge, search for `main_menu`, and this segment of code is for the program to purchase things from the shop. This shop simply calculates item count and purchase amount with this formula:

$$ \text{wallet} = \text{wallet} - \text{count} \* \text{price} $$

This corresponds to the line `v15 = wallet - *_num * inv.array[v14].price;`.

After the purchase is done, it returns and replaces the original wallet value with the calculated one. This means if we input a negative number for purchasing, we are actually telling the shopkeeper to give us money (oh god, is this a robbery?).

```cpp
    v9 = *_num;
    v10 = _choice;
    if ( (unsigned int)*_choice >= inv.len )
      runtime_panicindex();
    v11 = *_choice;
    count = inv.array[v11].count;
    if ( v9 <= count )
    {
      if ( wallet < inv.array[v11].price )
      {
        v35[0] = &RTYPE_string_0;
        v35[1] = &main_statictmp_7;
        ai.array = (interface_ *)v35;
        *(_QWORD *)&ai.len = 0x100000001LL;
        fmt_Println(ai);
        v15 = wallet;
      }
      else
      {
        inv.array[v11].count = count - v9;
        if ( (unsigned int)*v10 >= inv.len )
          runtime_panicindex();
        v14 = *v10;
        v15 = wallet - *_num * inv.array[v14].price;
        if ( (unsigned int)*v10 >= user.len )
          runtime_panicindex();
        user.array[v14].count += *_num;
        if ( inv.len <= 2u )
          runtime_panicindex();
        if ( inv.array[2].count != 1 )
          main_get_flag();
      }
      v13 = v15;
```

After we got enough money to buy flag, we are able to solve this challenge.

```shell
$ nc mercury.picoctf.net 10337
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
0 -1000 2 1
How many do you want to buy?
You have 10040 coins
        Item            Price   Count
(0) Quiet Quiches       10      1012
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
How many do you want to buy?
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 51 100 97 51 52 97 56 102 125]
```

```python
flag = "112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 51 100 97 51 52 97 56 102 125"

for i in flag.split(" "):
    print(chr(int(i)), end="")
```

```bash
$ python3 solve.py
picoCTF{b4d_brogrammer_3da34a8f}
```

## Reference

[https://ctftime.org/writeup/28932](https://ctftime.org/writeup/28932)
