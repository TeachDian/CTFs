# speeds and feeds

There is something on my shop network running at nc mercury.picoctf.net 53740, but I can't tell what it is. Can you?

# Hints

no hints.

# What I Did

I tried everything on the website and then check the website source,
I saw nothing on the html code then I went to the script file.
The script file is obfuscated and almost impossible for me to understand it,
so i ask ChatGpt to deobfuscate the java script code and i get
more understandable script (script.js).
In the script I saw that it fetch something from another path of URL

```'./JIFxzHyW8W'```

I tried curl (link)/JIFxzHyW8W

and i get the flag at the bottom part of the output
the flag is

``` picoCTF{d88090e679c48f3945fcaa6a7d6d70c5} ```
