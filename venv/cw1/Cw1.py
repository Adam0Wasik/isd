import re
from cmath import sqrt

D1 = "bazy relacyjne, bazy tekstowe, bazy inne"
D2 = "bazy danych: przykady, zastosowania"
D3 = "bazy danych - zalety; bazy danych - wady"
D4 = "skadowanie danych"

def containS(word,d):
    if word in d:
        return(1)
    else:
        return(0)

def vCacl(tab,ind):
    vD = 0
    for i in range(len(tab)):
        vD += int(tab[i][ind])*int(tab[i][ind])
    vD = sqrt(vD)
    return(vD)

def cutter(sentence):
    sentence = re.sub(", ", " ", sentence)
    sentence = re.sub(" - ", " ", sentence)
    sentence = re.sub(": ", " ", sentence)
    sentence = re.sub("; ", " ", sentence)
    sentence = sentence.split(" ")
    sentence = set(sentence)
    sentence = list(sentence)
    return sentence

def printer(D1,D2,D3,D4):
    print(D1)
    print(D2)
    print(D3)
    print(D4)
    print(" ")
print("Podstawowe pliki:")
printer(D1,D2,D3,D4)

D1 = cutter(D1)
D2 = cutter(D2)
D3 = cutter(D3)
D4 = cutter(D4)

print("Wycięte tagi:")
printer(D1,D2,D3,D4)

allWords = D1 + D2 + D3 + D4
allWords = set(allWords)
allWords = list(allWords)
allWords.sort()

print("tablica tagów:")
print(allWords)
print(" ")
print("slowo:           D1 D2 D3 D4")

tab = [[[None] for i in range(5)] for i in range(len(allWords))]
for i in range(len(allWords)):

    word = allWords[i]
    tab[i][0] = word

    tab[i][1] = containS(word, D1)
    tab[i][2] = containS(word, D2)
    tab[i][3] = containS(word, D3)
    tab[i][4] = containS(word, D4)

    #printing formatter V
    tab[i][0] = "{:<12}".format(tab[i][0])
    print(tab[i])

print(" ")
vD1 = vCacl(tab,1).real
vD2 = vCacl(tab,2).real
vD3 = vCacl(tab,3).real
vD4 = vCacl(tab,4).real
print("długości")
print("vD1 = " + str(vD1))
print("vD2 = " + str(vD2))
print("vD3 = " + str(vD3))
print("vD4 = " + str(vD4))
print(" ")

print(" Tablica po normalizacji")
for j in range(len(allWords)):
    tab[j][1] ="{:<6}".format( round( tab[j][1] * (tab[j][1]/vD1) , 4))
    tab[j][2] ="{:<6}".format( round( tab[j][2] * (tab[j][2]/vD2) , 4))
    tab[j][3] ="{:<6}".format( round( tab[j][3] * (tab[j][3]/vD3) , 4))
    tab[j][4] ="{:<6}".format( round( tab[j][4] * (tab[j][4]/vD4) , 4))
    print(tab[j])
