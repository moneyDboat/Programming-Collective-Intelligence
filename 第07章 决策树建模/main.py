import treepredict

# main function
# print('<----DivideSet---->')
# for item in treepredict.divideset(treepredict.my_data, 2, 'yes'):
#     print(item)
#
print('\n<----Build and Display the Tree---->')
tree = treepredict.buildtree(treepredict.my_data)
treepredict.printtree(tree)
#
# print('\n<----Graphical Display---->')
# path = 'output/treeview.jpg'
# treepredict.drawtree(tree, jpeg=path)
# print("picture has been saved in " + path)
#
# print('\n<----Classify and prune---->')
# test = ['(direct)', 'USA', 'yes', 5]
# print(test)
# print(treepredict.classify(test, tree), '\n')
#
# print('Before pune:')
# treepredict.printtree(tree)
# treepredict.prune(tree, 1.0)
# print('\nAfter pune:')
# treepredict.printtree(tree)

# print('<----Zillow API---->')
# import zillow
# # housedata = zillow.getpricelist()
# # print('house data saved!')
# housedata = zillow.getdata('input/housedata.txt')
# print('house data read!')
# housetree = treepredict.buildtree(housedata, scoref=treepredict.variance)
# treepredict.printtree(housetree)
# treepredict.drawtree(housetree, 'output/housetree.jpg')

# HotOrNot API is deprecated since 2008
