#picoCTF morse-code SABIR Yassine


Morse={".__":"A","_...":"B","_._.":"C","_..":"D",".":"E",".._.":"F","__.":"G","....":"H","..":"I",".___":"J","_._":"K","._..":"L","__":"M","_.":"N","___":"O",".__.":"P","__._":"Q","._.":"R","...":"S","_":"T",".._":"U","..._":"V",".__":"W","_.._":"X","_.__":"Y","__..":"Z",".____":"1","..___":"2","...__":"3","...._":"4",".....":"5","_....":"6","__...":"7","___..":"8","____.":"9","_____":"0"}


#Put underscores in place of pauses, and use all lowercase.


morse_flag=[".__","....","...._","__...","pause","....","...._","__...","....","pause","____.","_____","_..","pause",".__","..___","_____",".._","____.","....","__..."]

flag=""

for f in morse_flag:
    if f=="pause":
        flag+="_"
    else:
        flag+=Morse[f].lower()

print(flag)#wh47_h47h_90d_w20u9h7
