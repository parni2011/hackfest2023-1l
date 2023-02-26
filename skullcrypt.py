
# Online Python - IDE, Editor, Compiler, Interpreter

import random
#Encode
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
#Decode
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

opt = input("scramble(1)/unscramble(2)")
key = list(map(int,input("Enter Key ")))
psWrd = list(input("Enter Password "))
if opt == "1":
    print("".join(encode(psWrd,key)))
if opt == "2":
    print("".join(decode(psWrd,key)))
