import nmf
from pandas_datareader import data
import datetime
from numpy import *
import pickle

tickers = ['YHOO', 'AVP', 'BIIB', 'BP', 'CL', 'CVX',
           'PG', 'XOM', 'AMGN']


def getdata():
    shortest = 300
    prices = {}
    dates = None

    start = datetime.datetime(2000, 1, 1)
    end = datetime.date.today()

    for t in tickers:
        # Use pandas_datareader get finance data
        # Extract the volume field from every line
        rows = data.DataReader(t, 'google', start, end)
        print('Get %s data!' % t)
        prices[t] = list(rows['Volume'])

        if len(prices[t]) < shortest:
            shortest = len(prices[t])

        if not dates:
            dates = list(map(str, rows.index))

    return [[prices[tickers[i]][j]
             for i in range(len(tickers))]
            for j in range(shortest)], dates


# l1, dates = getdata()
# pickle.dump(l1, open('input/finance.txt','wb'))
# pickle.dump(dates, open('input/date.txt', 'wb'))

l1 = pickle.load(open('input/finance.txt', 'rb'))
dates = pickle.load(open('input/date.txt', 'rb'))
print('Data loaded!')
print('Start training!')

w, h = nmf.factorize(matrix(l1), pc=5)

print('h\n', h)
print('w\n', w)

# Loop over all the features
for i in range(shape(h)[0]):
    print("Feature %d" % i)

    # Get the top stocks for this feature
    ol = [(h[i, j], tickers[j]) for j in range(shape(h)[1])]
    ol.sort()
    ol.reverse()
    for j in range(len(tickers)):
        print(ol[j])
    print()

    # Show the top dates for this feature
    porder = [(w[d, i], d) for d in range(300)]
    porder.sort()
    porder.reverse()
    print([(p[0], dates[p[1]]) for p in porder[0:3]])
    print()
