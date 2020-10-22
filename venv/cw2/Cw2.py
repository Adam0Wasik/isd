import math
import re
from cmath import sqrt

def containS(word,d):
    if word in d:
        return(1)
    else:
        return(0)

def containSQty(word,d):
    amount = 0
    for w in d:
        if w == word:
            amount = amount + 1
    return(amount)

def wordCounter(tab,j):
    counter = 0
    for i in range(4):
        counter = counter + tab[j][i+1]
    return (counter)

def vCacl(tab,ind):
    vD = 0
    for i in range(len(tab)):
        vD += float(tab[i][ind])*float(tab[i][ind])
    vD = sqrt(vD)
    return(vD)

def cutter(sentence):
    sentence = re.sub(", ", " ", sentence)
    sentence = re.sub(" - ", " ", sentence)
    sentence = re.sub(": ", " ", sentence)
    sentence = re.sub("; ", " ", sentence)
    sentence = sentence.split(" ")
    sentence = list(sentence)
    return sentence

def printer(D1,D2,D3,D4):
    print(D1)
    print(D2)
    print(D3)
    print(D4)
    print(" ")
########################################################################################################################

D1 = "bazy relacyjne, bazy tekstowe, bazy inne"
D2 = "bazy danych: przyklady, zastosowania"
D3 = "bazy danych - zalety; bazy danych - wady"
D4 = "skladowanie danych"
Z  = "bazy danych"
# Z  = input("Podaj zapytanie:\n")
DV = 4

print("Podstawowe pliki:")
printer(D1,D2,D3,D4)

D1 = cutter(D1)
D2 = cutter(D2)
D3 = cutter(D3)
D4 = cutter(D4)
Z = cutter(Z)
print("Wycięte tagi:")
printer(D1,D2,D3,D4)

allWords = D1 + D2 + D3 + D4
allWords = set(allWords)
allWords = list(allWords)
allWords.sort()

print("tablica tagów:")
print(allWords)
print(" ")
print("Czestowtliwosc wystepowania w pliku:")
print("slowo:           D1 D2 D3 D4  Z")

tab  = [[[0] for i in range(6)] for i in range(len(allWords))]
tab2 = [[[0] for j in range(6)] for j in range(len(allWords))]
tab3 = [[[0] for j in range(6)] for j in range(len(allWords))]
for i in range(len(allWords)):

    word = allWords[i]
    tab[i][0] = word
    tab2[i][0] = word

    tab[i][1] = containSQty(word, D1)
    tab[i][2] = containSQty(word, D2)
    tab[i][3] = containSQty(word, D3)
    tab[i][4] = containSQty(word, D4)
    tab[i][5] = containSQty(word, Z)

    tab2[i][1] = containS(word, D1)
    tab2[i][2] = containS(word, D2)
    tab2[i][3] = containS(word, D3)
    tab2[i][4] = containS(word, D4)
    tab2[i][5] = containS(word, Z)

    tab3[i][1] = containSQty(word, D1)
    tab3[i][2] = containSQty(word, D2)
    tab3[i][3] = containSQty(word, D3)
    tab3[i][4] = containSQty(word, D4)
    tab3[i][5] = containSQty(word, Z)

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

print(" Tablica po pierwszej normalizacji")
for j in range(len(allWords)):
    tab[j][1] ="{:<6}".format(round(   tab[j][1] * (1/vD1)    , 4))
    tab[j][2] ="{:<6}".format(round(   tab[j][2] * (1/vD2)    , 4))
    tab[j][3] ="{:<6}".format(round(   tab[j][3] * (1/vD3)    , 4))
    tab[j][4] ="{:<6}".format(round(   tab[j][4] * (1/vD4)    , 4))
    tab[j][5] ="{:<6}".format(round(   tab[j][5] * (1/vD4)    , 4))
    print(tab[j])
print(" ")


print(" Tablica po indeksowaniu")
for j in range(len(allWords)):
    tab[j][1] ="{:<6}".format(round(   math.log2(DV/wordCounter(tab2,j))* tab3[j][1]   , 4) )
    tab[j][2] ="{:<6}".format(round(   math.log2(DV/wordCounter(tab2,j))* tab3[j][2]   , 4) )
    tab[j][3] ="{:<6}".format(round(   math.log2(DV/wordCounter(tab2,j))* tab3[j][3]   , 4) )
    tab[j][4] ="{:<6}".format(round(   math.log2(DV/wordCounter(tab2,j))* tab3[j][4]   , 4) )
    print(tab[j])

print(" ")
vD1 = vCacl(tab,1).real
vD2 = vCacl(tab,2).real
vD3 = vCacl(tab,3).real
vD4 = vCacl(tab,4).real

print(" Tablica znormalizowana")
for j in range(len(allWords)):
    tab[j][1] ="{:<6}".format(round(   float(tab[j][1]) * (1/vD1)    , 4))
    tab[j][2] ="{:<6}".format(round(   float(tab[j][2]) * (1/vD2)    , 4))
    tab[j][3] ="{:<6}".format(round(   float(tab[j][3]) * (1/vD3)    , 4))
    tab[j][4] ="{:<6}".format(round(   float(tab[j][4]) * (1/vD4)    , 4))
    print(tab[j])
print(" ")


#Podobienstwa
pD1 = 0
pD2 = 0
pD3 = 0
pD4 = 0
for j in range(len(allWords)):
    tab[j][1] ="{:<6}".format(round( float(tab[j][1]) * float(tab[j][5])     , 4))
    tab[j][2] ="{:<6}".format(round( float(tab[j][2]) * float(tab[j][5])     , 4))
    tab[j][3] ="{:<6}".format(round( float(tab[j][3]) * float(tab[j][5])     , 4))
    tab[j][4] ="{:<6}".format(round( float(tab[j][4]) * float(tab[j][5])     , 4))
    pD1 = pD1 + float(tab[j][1])
    pD2 = pD2 + float(tab[j][2])
    pD3 = pD3 + float(tab[j][3])
    pD4 = pD4 + float(tab[j][4])



print("Pliki:")
print(D1)
print(D2)
print(D3)
print(D4)
print(" ")

print("Zapytanie:")
print(Z)
print(" ")

print("Podobienstwa:")
print("podobieństwo zapytania Z do D1 = " + str(pD1))
print("podobieństwo zapytania Z do D2 = " + str(pD2))
print("podobieństwo zapytania Z do D3 = " + str(pD3))
print("podobieństwo zapytania Z do D4 = " + str(pD4))


