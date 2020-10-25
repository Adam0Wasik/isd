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

def cutter(*args):
    tab = [[0] for i in range(len(args))]
    i = 0
    for sentence in args:
        sentence = re.sub(", ", " ", sentence)
        sentence = re.sub(" - ", " ", sentence)
        sentence = re.sub(": ", " ", sentence)
        sentence = re.sub("; ", " ", sentence)
        sentence = sentence.split(" ")
        sentence = list(sentence)
        tab[i] = sentence
        i = i +1
    return tab

def printer(*args):
    for element in args:
        print(element)
########################################################################################################################

D1 = "bazy relacyjne, bazy tekstowe, bazy inne"
D2 = "bazy danych: przyklady, zastosowania"
D3 = "bazy danych - zalety; bazy danych - wady"
D4 = "składowanie danych"
# Z  = "bazy danych"
print("Program sprawdzi podobienstwo zadanego zapytania do przedstawionych plikow")
print("Podstawowe pliki:")
printer(D1,D2,D3,D4)
Z = input("Podaj zapytanie:\n")
DV = 4

print("Wycięte tagi:")
words = cutter(D1,D2,D3,D4)
for i in words:
    print(i)

D1,D2,D3,D4,Z = [sentence for sentence in  cutter(D1,D2,D3,D4,Z) ]

allWords = D1 + D2 + D3 + D4
allWords = set(allWords)
allWords = list(allWords)
allWords.sort()

print("tablica tagów:")
print(allWords)
print(" ")
print("Czestowtliwosc wystepowania w pliku:")
print("slowo:           D1 D2 D3 D4  Z")

tab, tab2, tab3  =[ [[[0] for i in range(6)] for j in range(len(allWords))] for k in range(3)]
vecD = [[0] for i in range(DV)]
words.append(Z)
for i in range(len(allWords)):
    i = i
    word = allWords[i]
    tab[i][0] = word
    tab2[i][0] = word

    for j in range(len(words)):
        tab[i][j+1] = containSQty(word, words[j])

    for j in range(len(words)):
        tab2[i][j+1] = containS(word, words[j])

    for j in range(len(words)):
        tab3[i][j+1] = containSQty(word, words[j])

    #printing formatter V
    tab[i][0] = "{:<12}".format(tab[i][0])
    print(tab[i])

print(" ")
for i in range(DV):
    vecD[i] = vCacl(tab,i+1).real
    print(vCacl(tab,i+1).real)

print(" Tablica po pierwszej normalizacji")
for j in range(len(allWords)):
    tab[j][1] ="{:<6}".format(round(   tab[j][1] * (1/vecD[0])    , 4))
    tab[j][2] ="{:<6}".format(round(   tab[j][2] * (1/vecD[1])    , 4))
    tab[j][3] ="{:<6}".format(round(   tab[j][3] * (1/vecD[2])    , 4))
    tab[j][4] ="{:<6}".format(round(   tab[j][4] * (1/vecD[3])    , 4))
    tab[j][5] ="{:<6}".format(round(   tab[j][5] * (1/vecD[3])    , 4))
    print(tab[j])
print(" ")

print(" Tablica po indeksowaniu")
for j in range(len(allWords)):
    for k in range(1,DV+1):
        tab[j][k] ="{:<6}".format(round(   math.log2(DV/wordCounter(tab2,j))* tab3[j][k]   , 4) )

    print(tab[j])

print(" ")
vecD = [[0] for i in range(DV)]
for i in range(DV):
    vecD[i] = vCacl(tab,i+1).real
    print(vCacl(tab,i+1).real)

print(" Tablica znormalizowana")
for j in range(len(allWords)):
    for k in range(1, DV + 1):
        tab[j][k] ="{:<6}".format(round(   float(tab[j][k]) * (1/vecD[k-1])    , 4))
    print(tab[j])
print(" ")

#Podobienstwa
pD1 = 0
pD2 = 0
pD3 = 0
pD4 = 0
for j in range(len(allWords)):
    for k in range(1, DV + 1):
        tab[j][k] ="{:<6}".format(round( float(tab[j][k]) * float(tab[j][5])     , 4))

    pD1 = pD1 + float(tab[j][1])
    pD2 = pD2 + float(tab[j][2])
    pD3 = pD3 + float(tab[j][3])
    pD4 = pD4 + float(tab[j][4])

print("Pliki:")
printer(D1,D2,D3,D4)
print(" ")

print("Zapytanie:")
print(Z)
print(" ")

print("Podobienstwa:")
print("podobieństwo zapytania Z do D1 = " + str(pD1))
print("podobieństwo zapytania Z do D2 = " + str(pD2))
print("podobieństwo zapytania Z do D3 = " + str(pD3))
print("podobieństwo zapytania Z do D4 = " + str(pD4))