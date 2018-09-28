import numpredict

# main function
# Building a Sample Dataset
print('\n<----Building a Sample Dataset--->')
print(numpredict.wineprice(90.0, 41.0))
data = numpredict.wineset1()
print(data[:2])

# K-Nearnest Neighbors
print('\n<----K-Nearnest Neighbors---->')
print(numpredict.knnestimate(data, (95.0, 3.0)))
print(numpredict.wineprice(95.0, 3.0))
print('<----Weighted KNN---->')
print(numpredict.weightedknn(data, (95.0, 3.0)))

# Cross_Validation
print('\n<----Cross-Validation---->')
data  = numpredict.wineset1()
def knn1(d, v):
    return numpredict.knnestimate(d, v, k=3)
def knn2(d, v):
    return numpredict.weightedknn(d, v, k=3)
print(numpredict.crossvalidate(knn1, data))
print(numpredict.crossvalidate(knn2, data))

# Parameter tuning
import optimization
print('<----Parameter tuning---->')
data2 = numpredict.wineset2()
print(numpredict.crossvalidate(knn1, data2))
print(numpredict.crossvalidate(numpredict.weightedknn, data2))
print('<--scaling-->')
sdata = numpredict.rescale(data2, [10, 10, 0, 0.5])
print(numpredict.crossvalidate(knn1, sdata))
print('<--optimizing-->')
costf = numpredict.createcostfunction(numpredict.knnestimate, data2)
print(optimization.geneticoptimize(numpredict.weightdomain, costf, step=2))

# Probability Density
print('\n<----Probability Density---->')
data3 = numpredict.wineset3()
numpredict.cumulativegraph(data3, (99, 20), 120)
numpredict.probabilitygraph(data3, (99, 20), 120)



# eBay API
# remaining problems
# import  ebaypredict
# laptops = ebaypredict.doSearch('laptop')
# print(laptops[:10])