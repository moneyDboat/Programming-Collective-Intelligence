import advancedclassify
from sklearn import svm

# # main funtion
# # load data
# print('<----load data---->')
# agesonly = advancedclassify.loadmatch('agesonly.csv', allnum=True)
# matchmaker = advancedclassify.loadmatch('matchmaker.csv')
# advancedclassify.plotagematches(agesonly)
#
#
# # scikit svm
# print('<----Use Scikit Svm---->')
# X = [[1, 0, 1], [-1, 0, -1]]
# y = [1, -1]
# clf = svm.SVC()
# print(clf.fit(X, y))
# print(clf.predict([[1, 1, 1]]))

# Applying SVM to the Matchmaker Dataset
numericalset = advancedclassify.loadnumerical()
print(numericalset[0].data)
scaledset, scalef = advancedclassify.scaledata(numericalset)
answers, input = [r.match for r in scaledset], [r.data for r in scaledset]
clf = svm.SVC()
print(clf.fit(input, answers))
print(clf.predict([scalef([28, -1, 1, 26, -1, 1, 2, 0])]))

# a sample of cross_validating
print('<----A sample of cross_validating---->')
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(input, answers,
                                                    test_size=0.7, random_state=0)
clf = svm.SVC().fit(X_train, y_train)
print(clf.score(X_test, y_test))

from sklearn.model_selection import cross_val_score

clf = svm.SVC()
scores = cross_val_score(clf, input, answers, cv=50)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
