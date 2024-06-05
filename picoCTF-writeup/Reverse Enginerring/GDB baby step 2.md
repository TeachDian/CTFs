---
Done: true
Chapter: Reverse Engineering
URL: https://play.picoctf.org/practice/challenge/396?category=3&page=3
tags:
  - picoCTF
  - ReverseEngineering
  - x86_64
---

# Solution

Just like [GDB baby step 1](./GDB%20baby%20step%201.md).

```shell
(gdb) break main
Breakpoint 1 at 0x40110e
(gdb) r
Starting program: /home/kali/Desktop/ctf/debugger0_b
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
>
Breakpoint 1, 0x000000000040110e in main ()
(gdb) p $eax
$1 = 4198662
(gdb) n
Single stepping until exit from function main,
which has no line number information.
__libc_start_call_main (main=main@entry=0x401106 <main>, argc=argc@entry=1,
    argv=argv@entry=0x7fffffffddc8) at ../sysdeps/nptl/libc_start_call_main.h:74
74      ../sysdeps/nptl/libc_start_call_main.h: No such file or directory.
(gdb) p $eax
$2 = 307019
```

![](https://i.imgur.com/yMwctYY.png)

The flag is: `picoCTF{307019}`
