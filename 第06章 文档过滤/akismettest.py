from pykismet3 import Akismet

# code is wrong

# defaultagent = 'akismettest python script from the Collective Intelligence book'
defaultagent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) '
defaultagent += 'AppleWebKit/525.27.1 (KHTML, like Gecko) '
defaultagent += 'Version/3.2.1 Safari/525.27.1'

a = Akismet(blog_url='moneydboat.top', user_agent=defaultagent)
a.api_key = 'e467cda4de57'


def isspam(comment, author, ip, agent=defaultagent):
    try:
        result = a.check({'user_ip': ip,
                 'user_agent': agent,
                 'referrer': 'unknown',
                 'comment_content': comment,
                 'comment_author': author,
                 'is_test': 1,
                 })
        print(result)
    except Akismet.AkismetError as e:
        print(e.response, e.statuscode)
        return False
