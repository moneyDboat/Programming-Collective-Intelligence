from numpy import *
import newsfeatures
import nmf
import pickle

# allw, artw, artt = newsfeatures.getarticlewords()
# pickle.dump(allw, open('input/tmp1.txt','wb'))
# pickle.dump(artw, open('input/tmp2.txt','wb'))
# pickle.dump(artt, open('input/tmp3.txt','wb'))
allw = pickle.load(open('input/tmp1.txt', 'rb'))
artw = pickle.load(open('input/tmp2.txt', 'rb'))
artt = pickle.load(open('input/tmp3.txt', 'rb'))


wordmatrix, wordvec = newsfeatures.makematrix(allw, artw)
print(len(wordvec))
v = matrix(wordmatrix)
weights, feat = nmf.factorize(v, pc=20, iter=50)
