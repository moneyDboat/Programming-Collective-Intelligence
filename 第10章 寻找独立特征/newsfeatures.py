import feedparser
import re

feedlist = ['http://feeds.reuters.com/reuters/topNews',
            'http://feeds.reuters.com/Reuters/worldNews',
            'http://feeds.reuters.com/reuters/MostRead',
            'http://feeds.reuters.com/reuters/businessNews',
            'http://feeds.reuters.com/news/wealth',
            'http://feeds.reuters.com/reuters/scienceNews',
            'http://feeds.reuters.com/reuters/technologyNews',
            'http://feeds.reuters.com/reuters/companyNews',
            'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/MostViewed.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/MostShared.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/Science.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
            'https://news.google.com/news/rss/?ned=us&hl=en',
            'https://news.google.com/news/rss/headlines/section/topic/WORLD?ned=us&hl=en',
            'https://news.google.com/news/rss/headlines/section/topic/BUSINESS?ned=us&hl=en',
            'https://news.google.com/news/rss/headlines/section/topic/TECHNOLOGY?ned=us&hl=en',
            'https://news.google.com/news/rss/headlines/section/topic/NATION?ned=us&hl=en',
            'https://news.google.com/news/rss/headlines/section/topic/SCIENCE?ned=us&hl=en',
            'http://rss.cnn.com/rss/cnn_topstories.rss',
            'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
            'http://hosted.ap.org/lineups/USHEADS-rss_2.0.xml?SITE=SCAND&SECTION=HOME',
            'http://www.npr.org/rss/rss.php?id=1001',
            'http://feeds.foxnews.com/foxnews/most-popular',
            'http://feeds.foxnews.com/foxnews/science',
            'http://feeds.foxnews.com/foxnews/tech',
            'http://feeds.foxnews.com/foxnews/world',
            ]


def stripHTML(h):
    p = ''
    s = 0
    for c in h:
        if c == '<':
            s = 1
        elif c == '>':
            s = 0
            p += ' '
        elif s == 0:
            p += str(c)
    return p


def separatewords(text):
    splitter = re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s) > 3]


def getarticlewords():
    allwords = {}
    articlewords = []
    articletitles = []
    ec = 0
    sum = 0
    # Loop over every feed
    for feed in feedlist:
        try:
            f = feedparser.parse(feed)

            # Loop over every article
            print(len(f.entries), 'news!')
            sum += len(f.entries)
            for e in f.entries:
                # Ignore identical articles
                if e.title in articletitles: continue

                # Extract the words
                txt = e.title + stripHTML(e.description)
                words = separatewords(txt)
                articlewords.append({})
                articletitles.append(e.title)

                # Increase the counts for this word in allwords and in articlewords
                for word in words:
                    allwords.setdefault(word, 0)
                    allwords[word] += 1
                    articlewords[ec].setdefault(word, 0)
                    articlewords[ec][word] += 1
                ec += 1
            print(feed, '  Done!')
        except:
            print(feed, '  Error!')
        print(sum, ' news altogether!')
    return allwords, articlewords, articletitles


def makematrix(allw, articlew):
    wordvec = []

    # Only take words that are common but not too common
    for w, c in list(allw.items()):
        if 3 < c < len(articlew) * 0.6:
            wordvec.append(w)

            # Create the word matrix
    l1 = [[(word in f and f[word] or 0.001) for word in wordvec] for f in articlew]
    return l1, wordvec


from numpy import *


def showfeatures(w, h, titles, wordvec, out='output/features.txt'):
    outfile = open(out, 'w')
    pc, wc = shape(h)
    toppatterns = [[] for i in range(len(titles))]
    patternnames = []

    # Loop over all the features
    for i in range(pc):
        slist = []
        # Create a list of words and their weights
        for j in range(wc):
            slist.append((h[i, j], wordvec[j]))
        # Reverse sort the word list
        slist.sort()
        slist.reverse()

        # Print the first six elements
        n = [s[1] for s in slist[0:6]]
        outfile.write(str(n) + '\n')
        patternnames.append(n)

        # Create a list of articles for this feature
        flist = []
        for j in range(len(titles)):
            # Add the article with its weight
            flist.append((w[j, i], titles[j]))
            toppatterns[j].append((w[j, i], i, titles[j]))

        # Reverse sort the list
        flist.sort()
        flist.reverse()

        # Show the top 3 articles
        for f in flist[0:3]:
            outfile.write(str(f) + '\n')
        outfile.write('\n')

    outfile.close()
    # Return the pattern names for later use
    return toppatterns, patternnames


def showarticles(titles, toppatterns, patternnames, out='output/articles.txt'):
    outfile = open(out, 'w')

    # Loop over all the articles
    for j in range(len(titles)):
        outfile.write(str(titles[j]) + '\n')

        # Get the top features for this article and
        # reverse sort them
        toppatterns[j].sort()
        toppatterns[j].reverse()

        # Print the top three patterns
        for i in range(3):
            outfile.write(str(toppatterns[j][i][0]) + ' ' +
                          str(patternnames[toppatterns[j][i][1]]) + '\n')
        outfile.write('\n')

    outfile.close()
