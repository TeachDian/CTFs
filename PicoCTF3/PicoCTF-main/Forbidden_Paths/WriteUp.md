# Platform: PicoCTF
# Name: Forbidden_Paths

Following the link we get to this page:

![pg1](img1.png)

Testing this online file reader we find out about a "php" page responsible with reading the files.

![pg2](img2.png)

This looks like a Local File Inclusion (LFI) so I'll try to get to the root directory and then read the flag.

![payload](img3.png)

And it worked!

![flag](img4.png)

# We got the Flag!s