from math import sqrt

moviesQty = 6
pickedMovie = 0
pickedUser  = 0
nRange = 2
                           #users
                        #     1   2   3   4   5   6   7   8   9  10  11  12
userMovies =              [ [ 1 ," ", 3 ," "," ", 5 ," "," ", 5 ," ", 4 ," "],
                            [" "," ", 5 , 4 ," "," ", 4 ," "," ", 2 , 1 , 3 ],
                            [ 2 , 4 ," ", 1 , 2 ," ", 3 ," ", 4 , 3 , 5 ," "],
                            [" ", 2 , 4 ," ", 5 ," "," ", 4 ," "," ", 2 ," "],
                            [" "," ", 4 , 3 , 4 , 2 ," "," "," "," ", 2 , 5 ],
                            [ 1 ," ", 3 ," ", 3 ," "," ", 2 ," "," ", 4 ," "],  ]

userMoviesOrigin =        [ [ 1 ," ", 3 ," "," ", 5 ," "," ", 5 ," ", 4 ," "],
                            [" "," ", 5 , 4 ," "," ", 4 ," "," ", 2 , 1 , 3 ],
                            [ 2 , 4 ," ", 1 , 2 ," ", 3 ," ", 4 , 3 , 5 ," "],
                            [" ", 2 , 4 ," ", 5 ," "," ", 4 ," "," ", 2 ," "],
                            [" "," ", 4 , 3 , 4 , 2 ," "," "," "," ", 2 , 5 ],
                            [ 1 ," ", 3 ," ", 3 ," "," ", 2 ," "," ", 4 ," "],  ]
pickedMovie = int(input("wybierz film (1-6)\n"))


def avg(tab):
    suma = 0
    cnt =  0
    for i in range(len(tab)):
        if tab[i] != " ":
            suma = suma + tab[i]
            cnt = cnt +1
    return suma/cnt

def center(tab, avg):
    for i in range(len(tab)):
        if tab[i] != " ":
            tab[i] = round(tab[i]-avg, 1)
        else:
            tab[i]=0
    return tab

def sumOfProductsTabs(tab, tab2):
    sop = 0
    for i in range(len(tab)):
        sop = sop + (tab[i] * tab2[i])
    return sop

def absTab(tab):
    abs = 0
    for i in range(len(tab)):
        abs = abs + tab[i]* tab[i]
    return sqrt(abs)

simTab = [0 for i in range(moviesQty)]

for i in range(moviesQty):
    tab1 = center(userMovies[pickedMovie-1],avg(userMovies[pickedMovie-1]))
    tab2 = center(userMovies[i],avg(userMovies[i]))
    upper = sumOfProductsTabs(tab1,tab2)
    bottom = absTab(userMovies[pickedMovie-1]) * absTab(userMovies[i])
    simTab[i] = round(upper / bottom, 2)
simTabSorted = sorted(simTab, reverse=True)

print("Similarity table:")
print(simTabSorted)
mostRevelantIndexes = [ [0,0] for i in range(nRange)]

print("\n most revelant films value: index")
for i in range(nRange):
    mostRevelantIndexes[i] = [simTabSorted[i+1], simTab.index(simTabSorted[i+1]) ]
    print(mostRevelantIndexes[i])
pickedUser = int(input("wybierz usera (1- 12)"))

UserTab = [0 for i in range(moviesQty)]
for i in range(moviesQty):
    if userMoviesOrigin[i][pickedUser-1] != " ":
        UserTab[i] = userMoviesOrigin[i][pickedUser-1]
    else:
        UserTab[i] = 0
print(UserTab)



upper = 0
lower = 0
for N in range(nRange):
    upper = upper + (mostRevelantIndexes[N][0] * UserTab[mostRevelantIndexes[N][1]])
    lower = lower + mostRevelantIndexes[N][0]
print("predicted value for movie: " + str(pickedMovie) + ": ")
print(upper/lower)
