import xml.dom.minidom
import urllib.request

zwskey = "X1-ZWz1940gy3bqbv_7j3qs"


def getaddressdata(address, city):
    escad = address.replace(' ', '+')
    url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?'
    url += 'zws-id=%s&address=%s&citystatezip=%s' % (zwskey, escad, city)
    doc = xml.dom.minidom.parseString(urllib.request.urlopen(url).read())
    code = doc.getElementsByTagName('code')[0].firstChild.data

    if code != '0':
        print('api error')
        return None

    try:
        zipcode = doc.getElementsByTagName('zipcode')[0].firstChild.data
        use = doc.getElementsByTagName('useCode')[0].firstChild.data
        year = doc.getElementsByTagName('yearBuilt')[0].firstChild.data
        bath = doc.getElementsByTagName('bathrooms')[0].firstChild.data
        bed = doc.getElementsByTagName('bedrooms')[0].firstChild.data
        rooms = doc.getElementsByTagName('totalRooms')[0].firstChild.data
        price = doc.getElementsByTagName('amount')[0].firstChild.data
    except:
        return None

    return zipcode, use, int(year), float(bath), int(bed), int(rooms), price


def getpricelist():
    l1 = []
    f = open('input/housedata.txt', 'w')
    for line in open('input/addresslist.txt'):
        data = getaddressdata(line.strip(), 'Cambridge,MA')
        if data is not None:
            f.write(','.join([str(i) for i in data]) + '\n')
            l1.append(data)
    return l1


def getdata(path):
    data = []
    for line in open(path):
        a = line.split(',')
        data.append((a[0], a[1], int(a[2]), float(a[3]), int(a[4]), int(a[5]), a[6]))

    return data
