import random
#DECODE
def encode(inp,key):
    add = 0
    out = []
    for item in inp:
        #key adder
        out.append(chr(ord(item)+key[add]))
        #key cycler
        add += 1
        if add==len(key):
            add = 0

    return(out)
#ENCODE
def decode(inp,key):
    add = 0
    out = []
    for item in inp:
        #key subtracter
        out.append(chr(ord(item)-key[add]))
        #key cycler
        add += 1
        if add==len(key):
            add = 0

    return(out)

opt = input("Please choose one of the Option\nScramble (Encode) 1\nUnscramble(Decrypt) 2")
psWrd = list(input("Enter String Input to Encypt/Decrypt : "))
key = list(map(int,input("Enter Encrypt Key : ")))
if opt == "1":
    print("".join(encode(psWrd,key)))
if opt == "2":
    print("".join(decode(psWrd,key)))
