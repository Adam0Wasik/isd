import re
from cmath import sqrt

from numpy import save

D1 = "bazy relacyjne, bazy tekstowe, bazy inne"
D2 = "bazy danych: przykady, zastosowania"
D3 = "bazy danych - zalety; bazy danych - wady"
D4 = "skadowanie danych"

def cutter(sentence):
    sentence = re.sub(", ", " ", sentence)
    sentence = re.sub(" - ", " ", sentence)
    sentence = re.sub(": ", " ", sentence)
    sentence = re.sub("; ", " ", sentence)
    sentence = sentence.split(" ")
    sentence = set(sentence)
    sentence = list(sentence)
    return sentence

D1 = cutter(D1)
D2 = cutter(D2)
D3 = cutter(D3)
D4 = cutter(D4)

print(D1)
print(D2)
print(D3)
print(D4)
print(" ")

Cont = D1 + D2 + D3 + D4
Cont = set(Cont)
Cont = list(Cont)
Cont.sort()

print(Cont)
print(" ")
print("slowo:           D1 D2 D3 D4")

table = [[None]*5]*len(Cont)
for i in range(len(Cont)):
    table[i][0] = Cont[i]
    word = Cont[i]
    if word in D1:
        table[i][1] = "1"
    if not word in D1:
        table[i][1] = "0"

    if word in D2:
        table[i][2] = "1"
    if not word in D2:
        table[i][2] = "0"

    if word in D3:
        table[i][3] = "1"
    if not word in D3:
        table[i][3] = "0"

    if word in D4:
        table[i][4] = "1"
    if not word in D4:
        table[i][4] = "0"

    #printing formatter V
    table[i][0] = "{:<12}".format(table[i][0])
    print(table[i])
for i in range(5):
    print(table[i])