from cmath import sqrt

N = 2
customerQTY = 4
productQTY  = 9
customerProduct = [     [1, 0, 0, 1, 0, 1, 1, 1, 1],
                        [1, 0, 0, 1, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0],  ]
[print(line) for line in customerProduct]
print(" ")

def formatter(input):
    return  "{:<6}".format(round(input, 4))

def vectorCalc(*tabs):
    inputTab = [tabs[i] for i in range(len(tabs))]
    resultTab = [0 for j in range(len(tabs))]
    for i in range(len(tabs)):
        for j in range(len(tabs[i])):
            resultTab[i] = resultTab[i] + (inputTab[i][j] * inputTab[i][j])
    return resultTab

customerSimilarity = [[[0] for i in range(customerQTY)]for j in range(customerQTY)]

vectors = vectorCalc(customerProduct[0],customerProduct[1],customerProduct[2],customerProduct[3])
vc1,vc2,vc3,vc4 = [ element for element in vectors ]

for i in range(len(customerProduct)):
    for j in range(len(customerProduct)):
        customerSimilarityValue = 0
        for k in range( productQTY):
            customerSimilarityValue = customerSimilarityValue + ( customerProduct[i][k] * customerProduct[j][k] )
        customerSimilarityValue2 = sqrt(vectors[i]).real * sqrt(vectors[j]).real
        customerSimilarityValue = float(customerSimilarityValue)/float(customerSimilarityValue2)

        if i == j:
            customerSimilarity[i][j] = formatter(1)
        else:
            customerSimilarity[i][j] = formatter(customerSimilarityValue)

print("Podobieństwa miedzy klientami:")
print("     K1:         K2:       K3:       K4:")
[print("K" + str(customerSimilarity.index(line)+1) + ": " , line) for line in customerSimilarity]

client = int(input("\n\n\nPodaj nr klienta 1-4:\n"))
sorted = list(customerSimilarity[client-1])
sorted.sort(reverse=True)

tabN = [0 for i in range(N)]
for i in range(N):
    tabN[i] = sorted[i+1]

tabIndexes = [0 for i in range(N)]
for i in range(N):
    tabIndexes[i] = customerSimilarity[client-1].index(tabN[i])

newTab = [[0 for i in range(productQTY)] for j in range(N+1)]
for i in range(productQTY):
    for j in range(N):
        newTab[j][i] = customerProduct[tabIndexes[j]][i] * tabN[j]
        if newTab[j][i] == '' or newTab[j][i-1] =="":
            newTab[j][i] = 0.0
        newTab[j][i - 1] = formatter(float(newTab[j][i-1]))
for j in range(productQTY):
    suma = 0
    for i in range(N):
        suma = suma + float(newTab[i][j])

    newTab[N][j] = formatter(suma/N)
print("wymnozone tablice produtków przez podobieństwo klientów wraz ze sednia")
for i in range(len(newTab)):
    print(newTab[i])
########################################################################################################################
####################################################CUOSTOMER###########################################################
####################################################BASED###VIEW########################################################
########################################################################################################################
itemSimilarity = [[0 for i in range(productQTY)]for j in range(productQTY)]


productVectors = list([[] for i in range(productQTY)])
for i in range(productQTY):
    for k in range(customerQTY):
        productVectors[i].append(customerProduct[k][i])

    calcluatedVectors = vectorCalc(productVectors[0], productVectors[1], productVectors[2],
                                   productVectors[3], productVectors[4], productVectors[5],
                                   productVectors[6], productVectors[7], productVectors[8], )

for i in range(productQTY):
    for j in range(productQTY):
        productValue = 0
        for f in range(4):
            productValue = productValue + (productVectors[i][f] * productVectors[j][f])
        down = sqrt(calcluatedVectors[i]).real * sqrt(calcluatedVectors[j]).real
        try:
            itemSimilarity[i][j] = float(productValue) / float(down)

            itemSimilarity[i][j] = formatter(itemSimilarity[i][j])
        except:
            itemSimilarity[i][j] = '------'
        if i == j:
            itemSimilarity[i][j] = formatter(1.0)
print("\n\nMacierz podobieństwa produktów\n")
for i in range(productQTY):
    print(itemSimilarity[i])