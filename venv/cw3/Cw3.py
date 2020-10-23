from cmath import sqrt

customerQTY = 4
productQTY  = 9
customerProduct = [     ['k1', 1, 0, 0, 1, 0, 1, 1, 1, 1],
                        ['k2', 1, 0, 0, 1, 0, 0, 0, 1, 1],
                        ['k3', 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        ['k4', 0, 0, 1, 1, 1, 0, 0, 0, 0],  ]
[print(line) for line in customerProduct]
print(" ")

def formatter(input):
    return  "{:<6}".format(round(input, 4))

def vectorCalc(*tabs):
    inputTab = [tabs[i] for i in range(customerQTY)]
    resultTab = [0 for j in range(customerQTY)]
    for i in range(len(tabs)):
        for j in range(1,productQTY+1):
            resultTab[i] = resultTab[i] + (inputTab[i][j] * inputTab[i][j])
    return resultTab

customerSimilarity = [[[0] for i in range(customerQTY)]for j in range(customerQTY)]

vectors = vectorCalc(customerProduct[0],customerProduct[1],customerProduct[2],customerProduct[3])
vc1,vc2,vc3,vc4 = [ element for element in vectors ]

for i in range(len(customerProduct)):
    for j in range(len(customerProduct)):
        customerSimilarityValue = 0
        for k in range(1, productQTY+1):
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