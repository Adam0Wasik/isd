import re


D1 = "bazy relacyjne, bazy tekstowe, bazy inne"
D2 = "bazy danych: przyklady, zastosowania"
D3 = "bazy danych - zalety; bazy danych - wady"
D4 = "skladowanie danych"
Z  = "bazy danych"

def printer(*args):
    for element in args:
        print(element)

def cutter(sentence):
    sentence = re.sub(", ", " ", sentence)
    sentence = re.sub(" - ", " ", sentence)
    sentence = re.sub(": ", " ", sentence)
    sentence = re.sub("; ", " ", sentence)
    sentence = sentence.split(" ")
    sentence = list(sentence)
    return sentence

# D1 = cutter(D1)
# D2 = cutter(D2)
# D3 = cutter(D3)
# D4 = cutter(D4)
# Z = cutter(Z)
# printer(D1,D2,D3,D4,Z)

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
D1,D2,D3,D4,Z  =[sentence for sentence in  cutter(D1,D2,D3,D4,Z) ]
printer(D1,D2,D3,D4,Z)

