import searchengine
import nn

# main()
# 因为网址无法访问，所以跳过爬虫和数据库建立部分，使用现成的数据库
crawler = searchengine.crawler('searchindex.db')
# crawler.createindextables()
# pages = [...]
# crawler.crawl(pages)

print('<----Database is prepared!---->')
print([row for row in crawler.con.execute( \
    'select rowid from wordlocation where wordid = 1')])

# Querying
print('<----Querying---->')
e = searchengine.searcher('searchindex.db')
result = e.getmatchrows('functional programming')
print(result)

# Content-Based Ranking
print('<----Content-Based Ranking---->')
e.query('functional programming')

# PageRank
print('<----PageRank!---->')
# crawler.calculatepagerank()
cur = crawler.con.execute('select * from pagerank order by score desc')
# pay attention to that 'sqlite3.Cursor' object is not subscriptable
for i in range(5):
    print(cur.fetchone())
print(e.geturlname(438))

# Learning from Clicks
print('<----Learning from Clicks---->')
mynet = nn.searchnet('nn.db')
# mynet.maketables()
wWorld, wRiver, wBank = 101, 102, 103
uWorldBank, uRiver, uEarth = 201, 202, 203

mynet.generatehiddennode([wWorld, wBank], [uWorldBank, uRiver, uEarth])
print('<-Before Training:->')
print(mynet.getresult([wWorld, wBank], [uWorldBank, uRiver, uEarth]))

mynet.trainquery([wWorld, wBank], [uWorldBank, uRiver, uEarth], uWorldBank)
print('<-After Training:->')
print(mynet.getresult([wWorld, wBank], [uWorldBank, uRiver, uEarth]))


