import pprint
# from googleapiclient.discovery import build
import optparse
import time
import sys
import os
import re
import threading
import datetime
import random
import json
import psycopg2
import string
import psutil
import subprocess
import urllib.parse
from bs4 import BeautifulSoup
from datetime import timezone
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from bs4 import BeautifulSoup, Tag
try:
    import requests
except ImportError:  # if requests module isn't installed
    if sys.platform.startswith('linux'):  # if platform is linux
        print(" please install requests  module in Debian")
        sys.exit(" sudo apt-get install python-requests ")
    else:
        print(" install requets module for python here : https://pypi.python.org/pypi/requests/2.9.1 or try: pip install requests")
        sys.exit()
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value]


user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100)


name = sys.argv[0].split('/')[-1]
com = 'pgrep -f ' + name

totalQueries = 0

p = subprocess.Popen([com], stdout=subprocess.PIPE, shell=True)
res = p.communicate()[0]

if isinstance(res, bytes):
    res = res.decode("utf-8")
res = [str(x) for x in res.split('\n') if len(x) > 0]


# if len(res) > 0:
#     print('Already running!')
#     print('Exit!')
#     exit()
#     exit()
#     exit()


proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050',
}


class Response1:
    def __init__(self, code1, text1):
        self.status_code = code1
        self.text = text1


num11 = 10
relsite = 1
safe11 = 'off'
counttreads = 0
lastcomment = 0
prev_numpost = 0
lastip = 0
restTorStart = 0
nowH = 0
relsite = 0
safe11 = 'active'
datelist = ['d', 'w', 'm', 'y']
targetlist = []
visitedUrl = []
alreadyAdded = []

blockThread = False
emptylist = []


targetlist3 = ['xamarin', 'ксамарин', 'ксомарин', 'AppGyver', 'App Gyver', 'Аппгайвер', ' Ionic ', 'PhoneGap', 'Phone Gap', 'Sencha Touch', 'SenchaTouch', 'CodeName One', 'CodeNameOne', 'React Native', 'ReactNative', 'Appcelerator', ' PWA ', ' PWA,', ' PWA.', ' pwa ', ' pwa,', ' pwa.', 'GoodBarber', 'Good Barber', 'Shoutem', 'Swiftic', 'AppInstitute', 'App Institute', 'Appy Pie', 'AppyPie', 'Bizness Apps', 'BiznessApps', 'AppYourself', 'App Yourself', 'Mobile Roadie', 'MobileRoadie', 'AppMachine', 'App Machine', 'Mobincube', 'AppsBuilder', 'Apps Builder', 'MobAppCreator', 'Mob App Creator', 'MobApp Creator',
               'AppMakr', 'App Makr', 'IBuild App', 'IBuildApp', 'BuildFire', 'Build Fire', 'Appery.io', 'Gamesalad', 'Zoho Creator', 'ZohoCreator', 'Zengine', 'Зенджин', 'Taplytics', 'Тэплитикс', 'Salesforce', 'Salesforce1', 'Mobile Roadie', 'MobileRoadie', 'Мобайл Роуди', 'Мобикарт', 'MobiCart', 'Гудбарбер', 'GoodBarber', 'Good Barber', 'GameSalad', 'Game Salad', 'Геймсэлэд', 'EachScape', 'Each Scape', ' Ичскейп ', 'BuildFire', 'Bizness Apps', 'BiznessApps', 'AppNotch', 'App Notch', 'AppMakr', 'App Makr', 'App Machine', 'AppMachine', 'Appery.io', 'AppBuilder', 'App Builder', 'App Factory', 'AppFactory', 'app.cat']


def find_phrases2(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = '\n'.join(str1.split())  # normalize whitespace
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True


def find_phrases(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = ' '.join(str1.split())  # normalize whitespace
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True
    # return filter(text.__contains__, phrases) # return phrases themselves


def getip():
    # print('---')
    try:
        r45 = requests.get('https://ident.me', proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return Response1("201", '')
        # continue
    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return Response1("201", '')
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return Response1("201", '')
        # continue
    print(r45.text)
    # print('---')
    return r45


global time1lastrestart1
time1lastrestart1 = datetime.datetime.now()
# /////////////////////////////////////////////////


def restartTor(sec=0):
    global time1lastrestart1
    global torWath
    # global restTorStart
    # restTorStart = restTorStart+1
    # if restTorStart > 12000:
    #     restTorStart = 0
    #     time.sleep(sec*10)

    diff1 = (datetime.datetime.now()-time1lastrestart1).seconds
    if diff1 < torWath:
        return 0
    # subprocess.run(["brew", "services", "restart", "tor"])
    # subprocess.run(["brew", "services", "reload", "tor"])
    subprocess.run(["killall", "-HUP", "tor"])
    time1lastrestart1 = datetime.datetime.now()
    # getip()
    if sec == 0:
        sec = 0.001
    time.sleep(sec)


def getCountryCode(ip=''):
    # print('---')
    try:
        r45 = requests.get('https://freegeoip.app/json/' +
                           str(ip), proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return 0
        # continue
    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return 0
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return 0
        # continue
    print(r45.text)
    d = json.JSONDecoder()
    rval = d.decode(r45.text)
    countryCode = rval['country_code']
    # print('---')
    return countryCode


def switchProxyIfNeedForCountry():
    while getCountryCode(getip().text) != 'RU':
        restartTor()


def switchProxyIfNeedForGoogle():
    while google() != '200':
        restartTor()


def switchProxyIfNeed(target, targetlist3):
    if target not in targetlist3:
        while getCountryCode(getip().text) != 'RU' and google() != '200' and random.randint(1, 10) > 1:
            restartTor()
    getCountryCode(getip().text)


def google():
    q = 'mobsted'
    randUa = user_agent_rotator.get_random_user_agent()
    headersget = {
        # random.choice(ua14) , #
        'User-Agent': randUa,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    # s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    try:
        r = requests.get(url, headers=headersget,
                         proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return '201'

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return '201'

    # print ('google target :'+str(r.status_code) + ' q:'+str(q))
    print('google target :'+str(r.status_code))
    return str(r.status_code)
    # soup = BeautifulSoup(r.text, "html.parser")
    # output = []
    # for searchWrapper in soup.find_all('h3', {'class':'r'}): #this line may change in future based on google's web page structure
    #    url = searchWrapper.find('a')["href"]
    #    text = searchWrapper.find('a').text.strip()
    #    result = {'text': text, 'url': url}
    #    output.append(result)
    # return output


def find_all(a_str, sub):
    a_str = a_str.lower()
    sub = sub.lower()
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def makeGetRequest(url, main):
    # print('(url, main)')
    # print((url, main))
    if url[-4].find('.jpg') > -1:
        return None
    if url[-4].find('.png') > -1:
        return None
    if url[-5].find('.tiff') > -1:
        return None
    if url[-4].find('.tif') > -1:
        return None
    if url[-4].find('.bmp') > -1:
        return None
    if url[-5].find('.jpeg') > -1:
        return None
    if url[-4].find('.gif') > -1:
        return None
    if url[-4].find('.eps') > -1:
        return None
    if url[-4].find('.raw') > -1:
        return None
    
    nproxy=False
    if url.find('.php') > -1:
        print((url, main))
    # if url.find('video')>-1:
    # print('(url, main)')
    # print((url, main))
    str1, str2, *_ = main.split('//')
    if url.find(str2) == -1:
        return None
    global visitedUrl
    if str(url) in visitedUrl:
        return None
    visitedUrl.append(url)
    if(random.randint(1,1000)==1):
      print(url)
    counttryes = 0
    global httpTimeOut
    while True:
        useTor = True
        r = Response1("0", '')
        counttryes = counttryes+1
        if counttryes > 4:
            return None
        if counttryes > 1:
            nproxy = not nproxy
        try:

            randUa = user_agent_rotator.get_random_user_agent()
            # print ('randUa:'+str(randUa))
            if not nproxy:
             useTor = False
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': randUa
             }, timeout=httpTimeOut, allow_redirects=True)  # , allow_redirects=True
            else:
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': randUa
             }, proxies=proxies, timeout=httpTimeOut, allow_redirects=True)
            # print ('status_code:'+str(r.status_code))
            # print ('r.text:'+str(r.text)[0:100])
            # print(r.headers)
            # print(r.headers['Content-Type'])
            if r.history:
                # print("Request was redirected")
                # for resp in r.history:
                #     print(r.status_code, resp.url)
                # print("Final destination:")
                # print(r.status_code, r.url)
                return makeGetRequest(r.url,main)

            if str(r.headers['Content-Type']).find('text/html') == -1 and str(r.headers['Content-Type']).find('application/json') == -1:
                return None
        except requests.ConnectionError as e:  # if host don't exist
            # print(url)
            # print('requests.HTTPError:'+str(requests))
            # print("[-] host die  ConnectionError: "+str(e))
            # sys.exit()
            if useTor:
             restartTor()
            # time.sleep(10)
            continue
        except requests.HTTPError as e:
            print("[-] host die  HTTPError: "+str(e))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.ConnectTimeout as e:
            print("[-] host die  ConnectTimeout: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.ReadTimeout as e:
            if(random.randint(1,1000)==1):
              print("[-] host die  ReadTimeout: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.Timeout as e:
            print("[-] host die  Timeout: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.TooManyRedirects as e:
            print("[-] host die TooManyRedirects: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            # print("[-] host die RequestException: "+str(e))

            if (str(str(e))).find('Failed to parse:') != -1:
                # return None
                continue
        except:
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
            # sys.exit(1)

        if int(r.status_code) != 200:
            # print("restart tor r.status_code= "+str(r.status_code))
            if useTor:
             restartTor()
            # time.sleep(1)
            # return None
            continue

        d = json.JSONDecoder()
        if r.text == None:
            print("[-] empty result from  "+str(url))
            restartTor()
            continue
        try:
            items23r = r.text
            if len(items23r) <= 20:
                print("[-] empty result from  "+str(url))
                restartTor()
                continue
        except:
            print('I got a KeyError - reason r.text ')
            print(repr(r.text))
            if useTor:
             restartTor()
            continue
        if len(str(items23r)) == 0:
            if useTor:
             restartTor()
            continue
        # print(url)
        # print(r.text[0:100])
        return r.text


def recursiveUrl(url, link, depth, urlMain, strUrl, alreadyAdded, time1start1):
    diff1 = (datetime.datetime.now()-time1start1).seconds
    # print('(url) '+str(url))
    # print('type(link) '+str(type(link)))
    
    


    # print('spentTime seconds:'+str(diff1))
    global diffTimeProcess
    if diff1 > diffTimeProcess:
        print('exit by diffTimeProcess')
        return url
    if link is None:
        print('exit by link is None')
        return url
    global depthSite
    if depth == depthSite:
        print('exit by depthSite')
        return url
    if len(alreadyAdded) > 32:
        print('exit by alreadyAdded > 32')
        return url


    if not isinstance(link, str):
      if link.has_attr('href'):
        # 
        link = {'href': link['href']}
    if isinstance(link, str):
      print('(link[:15]]) '+str(link[:15]))


    if link == '#####':
        link = {'href': '#####'}
    else:
        if not type(link) is dict:
          if not link.has_attr('href'):
            # print('!!!!!!!!!!!!!!!!!!-------------type(link) '+str(type(link)))
            # if type(link) == Tag:
            #     print("bs4_element_var's type is bs4.element.Tag "+str(link))
            #     # link = {'href': '#####'}
            return url

    # try:
    #     a1111test = link['href']
    # except ValueError:
    #     return url

    if len(link['href']) < 2:
        # print('exit by len(link[\'href\']) < 2:')
        # print('<2  -  (link[\'href\']) '+str(link['href']))
        return url
    global visitedUrl
    if str(url)+link['href'] in visitedUrl:
        # print('exit by in visitedUrl')
        return None





    newUrl = link['href']
    if str(link['href']).find('http://') == -1 and str(link['href']).find('https://') == -1:
        newUrl = str(url) + link['href']
        print('(newUrl) '+str(newUrl))

    page = makeGetRequest(newUrl, str(urlMain))
    page2 = page
    visitedUrl.append(str(url)+link['href'])
    # print(page[0:100])
    newlink = []
    newlink1 = []
    mailtos = []
    if not page is None:
        soup1 = BeautifulSoup(page, 'html.parser')
        mailtos = soup1.select('a[href^=mailto]')
        newlink1 = soup1.select('a')
        newlink = newlink1
        for a in soup1.find_all('a', href=True):
         if a['href']:
          if (a['href']).find('linkedin.com')>-1:
           mailtos.append(a)
    newUrl = link['href']
    if str(link['href']).find('http://') == -1 and str(link['href']).find('https://') == -1:
        newUrl = str(url) + link['href']
    

    # print(page2[0:100])
    mailtos2 = []
    if not page2 is None:
        soup = BeautifulSoup(page2, 'html.parser')
        mailtos2 = soup.select('a[href^=mailto]')
        newlink = soup.select('a')
    # print('mailtos2')
    # print(mailtos2)
    # print('url:'+str(url))
    # print('urlMain:'+str(urlMain))
    # print('alreadyAdded:'+str(alreadyAdded))


    some_list = mailtos+mailtos2
    mailtos = list(dict.fromkeys(some_list))

    # print('newlink')
    # print(newlink)
    # time.sleep(20)
    # print('mailtos!!')
    # print(mailtos)
    for i in mailtos:
        if i['href']:
            href = i['href']
            try:
                str1, str2 = href.split(':')
            except ValueError:
                continue

            str2 = str2.lower()
            if str2.find('?subject') != -1:
                try:
                    str2, str1 = str2.split('?subject')
                except ValueError:
                    continue
            if str2.find('mailto:') != -1:
                try:
                    str1, str2 = str2.split('ailto:')
                except ValueError:
                    continue
            str2 = str2.strip(' \t\n\r')
            str2 = str2.strip()
            # print(str(str2))
            # global alreadyAdded
            # if not find_phrases(filename11, str2) and not str2 in alreadyAdded:
            #     f = open(filename11, 'a')
            #     f.write(str(str2)+'\n')
            #     f.close()
            #     alreadyAdded.append(str2)
            #     print('++text in file')
            # else:
            #     print('--text already in file')

            if (not str2 in alreadyAdded) and ('@' in str2):
                alreadyAdded.append(str2)
                print('++new mail')
                print(alreadyAdded)
            # else:
            #     print('--was')

    emails1 = []
    if not page2 is None:
        emails1 = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", page2)
        # print ('emails'+str(emails1))
    for str2 in emails1:
          if (not str2 in alreadyAdded):
                alreadyAdded.append(str2)
                print('++new mail')
                print(alreadyAdded)


    if newlink is None:
        newlink = newlink1

    if newlink is None:
        return link

    if len(newlink) == 0:
        newlink = newlink1

    if len(newlink) == 0:
        return link

    for link1 in newlink:
        recursiveUrl(url, link1, depth + 1, urlMain, strUrl, alreadyAdded, time1start1)

        # while threading.active_count() > 9999:
        #     time.sleep(random.randint(10, 30))
        # # print('startTime:'+str(datetime.datetime.now()))
        # thread = threading.Thread(
        #     target=recursiveUrl, args=(url, link1, depth + 1, urlMain, strUrl, alreadyAdded, time1start1))
        # thread.daemon = True
        # thread.start()


def makeGetRequestAddData(url, data, nproxy=False):

    new_list = data.copy()
    site1 = new_list.pop(0)
    strForWrite = ';'.join(new_list)
    if True:
        useTor = False
        r = Response1("0", '')

        try:
            randUa = user_agent_rotator.get_random_user_agent()
            data2 = {"site": str(site1), "resText": str(strForWrite),   "resJson": new_list }  #"resJsonArr": data[10],
            r = requests.post(url, headers={
            'origin': url,
            # 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'content-type': 'application/json',
            'user-agent': randUa
            }, timeout=120, allow_redirects=True, json=(data2), verify=False )
            print(r.text)
            # r.close()
        except requests.ConnectionError as e:
            print("[-] host die  ConnectionError: "+str(e))
        except requests.HTTPError as e:
            print("[-] host die  HTTPError: "+str(e))
        except requests.exceptions.ConnectTimeout as e:
            print("[-] host die  ConnectTimeout: "+str(e))
        except requests.exceptions.ReadTimeout as e:
            print("[-] host die  ReadTimeout: "+str(e))
        except requests.exceptions.Timeout as e:
            print("[-] host die  Timeout: "+str(e))
        except requests.exceptions.TooManyRedirects as e:
            print("[-] host die TooManyRedirects: "+str(e))
        except requests.exceptions.RequestException as e:
            print("[-]requests.exceptions.RequestException: "+str(e))
        except:
            print("[-] some excep: ")
            return None

        if int(r.status_code) != 200:
            return None
     
        return r


 


def check_lives(siteData, time1start, strForWrite, n):
        print( json.dumps(siteData) )
        # exit()

        p = psutil.Process(os.getpid())
        p.nice(2)
        
        r = makeGetRequestAddData('https://aleksandr-admin.mbst.xyz/api/v8/file/uploadDataFromGParser', siteData)
        if r is None:
            return False
        pprint.pprint(r)

        print( r.status_code )
        print(r.text)
        print(siteData)
        # exit()
        if int(n)>0 and int(r.status_code)==200:
            strForWrite = strForWrite+';'
            filename11 = 'targets_result'+str(n)+'.txt'
            f = open(filename11, 'a')
            f.write(str(strForWrite)+'\n')
            f.close()
            exit()
            return True
        else:
            return False



def main33(url, urlMain, strUrl, n, time1start):

    rtext = makeGetRequest('http://'+str(url), 'http://'+str(urlMain))
    links = []
    if not rtext is None:
        soup = BeautifulSoup(rtext, 'html.parser')
        links = soup.find_all('a')

    rtext = makeGetRequest('https://'+str(url), 'https://'+str(urlMain))
    links2 = []
    if not rtext is None:
        soup = BeautifulSoup(rtext, 'html.parser')
        links2 = soup.find_all('a')


    if not rtext is None:
        soup = BeautifulSoup(rtext, 'html.parser')
        #links = soup.find_all('a')
        keywords = []
        descriptions = []
        if siteData[2] is None or siteData[2]=='' or siteData[2]==' ':
         keywords = [item['content'] for item in soup.select('[name=Keywords][content], [name=keywords][content]')]
         print('keywords '+str(keywords))
        if siteData[3] is None or siteData[3]=='' or siteData[3]==' ':
         descriptions = [item['content'] for item in soup.select('[name=Description][content], [name=description][content]')]
         print('descriptions '+str(descriptions))
    emails = []
    if not rtext is None:
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", rtext)
        print ('emails'+str(emails))
         
    some_list = links + links2 + emails
    links = list(dict.fromkeys(some_list))

    alreadyAdded1 = []
    alreadyAdded1.append(strUrl)

    Object1 = '#####'
    recursiveUrl('http://'+str(url), Object1, 0,
                 'http://'+str(urlMain), strUrl, alreadyAdded1, time1start)
    recursiveUrl('https://'+str(url), Object1, 0,
                 'https://'+str(urlMain), strUrl, alreadyAdded1, time1start)

    for link in links:
      if link:
        if isinstance(link, str):
         print('link')
         print(link[:20])
         if len(link)<3:
             continue
        recursiveUrl('http://'+str(url), link, 0,
                     'http://'+str(urlMain), strUrl, alreadyAdded1, time1start)
        recursiveUrl('https://'+str(url), link, 0,
                     'https://'+str(urlMain), strUrl, alreadyAdded1, time1start)
    # links.append()
    # print('result links')
    # print(result1)
    # print('result mails')
    # print(result2)
    strForWrite = ';'.join(alreadyAdded1)
    print('strForWrite '+str(strForWrite))
    exit()
    # if len(alreadyAdded1)>1:
    #     # print('wrote')
    #     # print(strForWrite) 

    #     thread = threading.Thread(
    #         target=check_lives, args=(alreadyAdded1, datetime.datetime.now(),strForWrite,n))
    #     thread.daemon = True
    #     thread.start()        
        

def fromBase():
    try:
        tshema = 'a7db574a'
        conpg = psycopg2.connect(database=tshema, user=pguser, password=pgpswd,
                                host=pghost, port=pgport, options=f'-c search_path={tshema}')
        curpg = conpg.cursor(name='foo11')
        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
               sql = "SELECT \"Url\" FROM objects  where (\"SwState\"='2' or  \"ManifestState\"='2') and \"Em1\"='' order by \"LastModified\" desc;" 
               curpg.execute(sql)
               res1 = curpg.fetchall()
            #    print('res1 %s' % len(res1[0]))
               return res1
    except psycopg2.DatabaseError as e:
        print('Error %s' % e)


# uniqlines = set(open(fname,'r', encoding='utf-8').readlines())
# gotovo = open(fname,'w', encoding='utf-8').writelines(set(uniqlines))

# f = open(fname, 'r')
# text = f.readlines()
# f.close()
# random.shuffle(text)

# f = open(fname, 'w')
# f.writelines(text)
# f.close()
global httpTimeOut
httpTimeOut = 0
global torWath
torWath = 6
global diffTimeProcess
diffTimeProcess = 998
global depthSite
depthSite = 94
first = True

maxProcCount = 499

i1 = 0

# pgdb = 'great_paraser'
pguser = 'postgres'
pgpswd = 'postgres'
pghost = '10.b.a.d'
pgport = '1111'
# pgschema = 'great_paraser'
max_process_count = 2
d1 = json.JSONDecoder()



siteGen = sys.argv
siteGen.pop(0)

if True:
    torWath = torWath + 1
    diffTimeProcess = diffTimeProcess + 2
    depthSite = depthSite+1
    httpTimeOut = httpTimeOut+1
    
    print(str(threading.active_count())+' - threading.active_count()')
    print(str(torWath)+' - torWath')
    print(str(diffTimeProcess)+' - diffTimeProcess')
    print(str(depthSite)+' - depthSite')
    print(str(httpTimeOut)+' - httpTimeOut')

    #siteGen = fromBase()
    print(str(len(siteGen))+' - len(siteGen)')
    print(str((siteGen))+' - (siteGen)')
    for siteData in siteGen:
        print('siteData '+str(siteData))
        str2 = str(siteData)
        str2 = str2.replace('http://', '')
        str2 = str2.replace('https://', '')
        if len(str2) < 3:
            continue

        str1 = str2.strip()
        str2 = str1
        print('str2 '+str(str2))
        print('str1 '+str(str1))
        if threading.active_count() < maxProcCount:
            print('startTime:'+str(datetime.datetime.now()))
            thread = threading.Thread(
                target=main33, args=(str1, str1, str2, i1, datetime.datetime.now()))
            thread.daemon = True
            thread.start()
            # time.sleep(random.randint(10, 30))
            # time.sleep(14)
            if(random.randint(1,1000)==1):
                print('--------------------------------'+str(str1))
        else:
            # print('---')
            # print('sleep')
            time.sleep(120)
            # restartTor()
            # try:
            #     r45 = requests.get('https://ident.me',
            #                        proxies=proxies, timeout=1000)
            # except requests.exceptions.Timeout as e:
            #     print("\r SSL Error with : "+str(e))
            #     restartTor(5)

            # except requests.exceptions.RequestException as e:
            #     print("\r Error with  Credentials: "+str(e))
            #     restartTor(5)

            # print(r45.text)

            # print('---')
    first = False

# for i in range(0, 61):
#     print('current active process:'+str(threading.active_count()))
#     time.sleep(60)
while threading.active_count() > 1:
    print('--')
    time.sleep(300)
print('exit')
