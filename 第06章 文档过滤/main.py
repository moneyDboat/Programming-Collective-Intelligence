import docclass
import feedfilter
import akismettest

# main funtion

# Bayes
print('<----Bayes\' Theorem---->')
c1 = docclass.naivebayes(docclass.getwords)
c1.setdb('test.db')
docclass.sampletrain(c1)
print(c1.classify('quick rabbit'))
print(c1.classify('quick money'))


# Fisher Method
print('\n<----Fisher Method---->')
c2 = docclass.fisherclassifier(docclass.getwords)
c2.setdb('test.db')
docclass.sampletrain(c2)
print(c2.classify('quick rabbit'))
print(c2.classify('quick money'))

# Filtering Blog Feeds
print('<----Filtering Blog Feeds---->')
c3 = docclass.fisherclassifier(docclass.getwords)
c3.setdb('python_feed.db')
feedfilter.read('python_search.xml', c3)


# Using Akismet
print('<----Using Akismet---->')
msg = 'Make money fast!'
akismettest.isspam(msg, 'spammer@spam.com', '127.0.0.1')
