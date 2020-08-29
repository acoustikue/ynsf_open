# [Project YNS] Yonsei Univ. Notification Service, Project KNSF based.
# 0.1.2va, 20.02.02. First launched.
# written by acoustikue(SukJoon Oh), Yonsei University EE
#                                 __  _ __            
#    ____ __________  __  _______/ /_(_) /____  _____ 
#   / __ `/ ___/ __ \/ / / / ___/ __/ / //_/ / / / _ \
#  / /_/ / /__/ /_/ / /_/ (__  ) /_/ / ,< / /_/ /  __/
#  \__,_/\___/\____/\__,_/____/\__/_/_/|_|\__,_/\___/ 
#                                                     
# Ubuntu 18.04 LTS, Goorm IDE(https://ide.goorm.io/)
# 

# This project requires pyfcm library, 
# thus first install it by
# $ pip3 install pyfcm

# In initial version, many of original KENS/KNS functions are refactored, 
# since YNS can be distinguished by only methods of sending notifications to devices.

# YNS used FCM for push service, and used Flask as a server for getting devices' tokens.
# In this source there is no relation with the Flask server.

# Database added, for device token control and saving previous notices.
#
#

import requests
from bs4 import BeautifulSoup # parser

# from collections import OrderedDict

import config as cf

# Explanation:
# html request process is already contained in parser.
# What the parser need is just url.

def getText(url):
    req = requests.get(url)
    
    print('{color}{url} status[{status}]'.format(color=cf.bcolors.OKGREEN, url=url, status=str(req.status_code))) # debug
    
    return req.text

#
# A dict.
def makeGroup(site, title, sign, url):
    
    dict_ = {}
    
    dict_['site'] = site
    dict_['title'] = title
    dict_['sign'] = sign
    dict_['url'] = url
    
    return dict_
       
    

#
# Author: acoustikue
def parseTextMain(text):
    
    # YNS_SITE_MAIN
    soup = BeautifulSoup(text, 'html.parser') # filter
    soup = BeautifulSoup(str(soup.find('div', class_='article')), 'html.parser')
    
    # Each notice information
    title = []
    sign = []
    url = []    
    
    # title
    for title_list in soup.find_all('strong'): # title
        title.append(" ".join(title_list.text.split()))
        
    for sign_list in soup.find_all('span', class_='title'): 
        sign.append(" ".join(sign_list.text.split()))
        # information, like 신촌/국제 학부대학 2020.02.04
        
    for link_list in soup.findAll("a"):
        if 'href' in link_list.attrs:            
            link_t = link_list.attrs['href'] # temporary
            
            # filter
            if (link_t != 'javascript:;') and (link_t[:22] != '/sc/support/notice.jsp'):
                # print(link_list.attrs['href'])
                url.append(link_t)                 
            
            del link_t    
    
    # return
    list_ = []

    for i in range(len(title)):
        list_.append(makeGroup(cf.YNS_SITE_MAIN, title[i], sign[i], url[i]))
        
    return list_
    
            
            
def parseTextEE(text):
    
    # YNS_SITE_EE
    soup = BeautifulSoup(text, 'html.parser') # filter
    soup = BeautifulSoup(str(soup.find('table', class_='board-table')), 'html.parser')
    
    # Each notice information
    title = []
    sign = [] # author is always fixed to '전기전자공학부', thus date is only needed.
    url = []    
    
    
    for title_list in soup.find_all('a', class_='c-board-title'): # title
        title.append(" ".join(title_list.text.split()))

    for sign_list in soup.find_all('div', class_='c-board-info-m'): # title
        sign.append(" ".join(sign_list.text.split()).replace('전기전자공학부', '전기전자공학부 ')) # remove EE
        # sign.append(" ".join(sign_list.text.split()))

    for link_list in soup.findAll("a"):
        if 'href' in link_list.attrs:
            url.append(link_list.attrs['href'])
            
    # return
    list_ = []

    for i in range(len(title)):
        list_.append(makeGroup(cf.YNS_SITE_EE, title[i], sign[i], url[i]))
        
    return list_



def parseTextEESeminar(text):
    
    # YNS_SITE_EE
    soup = BeautifulSoup(text, 'html.parser') # filter
    soup = BeautifulSoup(str(soup.find('table', class_='board-table')), 'html.parser')
    
    # Each notice information
    title = []
    sign = [] # author is always fixed to '전기전자공학부', thus date is only needed.
    url = []    
    
    
    for title_list in soup.find_all('a', class_='c-board-title'): # title
        title.append(" ".join(title_list.text.split()))

    for sign_list in soup.find_all('div', class_='c-board-info-m'): # title
        sign.append(" ".join(sign_list.text.split()).replace('전기전자공학부', '전기전자공학부 ')) # remove EE
        # sign.append(" ".join(sign_list.text.split()))

    for link_list in soup.findAll("a"):
        if 'href' in link_list.attrs:
            url.append(link_list.attrs['href'])
            
    # return
    list_ = []

    for i in range(len(title)):
        list_.append(makeGroup(cf.YNS_SITE_EE_SEMINAR, title[i], sign[i], url[i]))
        
    return list_



def parseTextEtc(text):
    
    # YNS_SITE_MAIN
    soup = BeautifulSoup(text, 'html.parser') # filter
    soup = BeautifulSoup(str(soup.find('div', class_='article')), 'html.parser')
    
    # Each notice information
    title = []
    sign = []
    url = []    
    
    # title
    for title_list in soup.find_all('strong'): # title
        title.append(" ".join(title_list.text.split()))
        
    for sign_list in soup.find_all('span', class_='title'): 
        sign.append(" ".join(sign_list.text.split()))
        # information, like 신촌/국제 학부대학 2020.02.04
        
    for link_list in soup.findAll("a"):
        if 'href' in link_list.attrs:            
            link_t = link_list.attrs['href'] # temporary
            
            # filter
            if (link_t != 'javascript:;') and (link_t[:22] != '/sc/support/etc_notice.jsp'):
                # print(link_list.attrs['href'])
                url.append(link_t)                 
            
            del link_t    
    
    # return
    list_ = []

    for i in range(len(title)):
        list_.append(makeGroup(cf.YNS_SITE_ETC, title[i], sign[i], url[i]))
        
    return list_



def parseTextCorona(text):
    
    # YNS_SITE_MAIN
    soup = BeautifulSoup(text, 'html.parser') # filter
    soup = BeautifulSoup(str(soup.find('div', class_='article')), 'html.parser')
    
    # Each notice information
    title = []
    sign = []
    url = []    
    
    # title
    for title_list in soup.find_all('strong'): # title
        title.append(" ".join(title_list.text.split()))
        
    for sign_list in soup.find_all('span', class_='title'): 
        sign.append(" ".join(sign_list.text.split()))
        # information, like 신촌/국제 학부대학 2020.02.04
        
    for link_list in soup.findAll("a"):
        if 'href' in link_list.attrs:            
            link_t = link_list.attrs['href'] # temporary
            
            # filter
            if (link_t != 'javascript:;') and (link_t[:22] != '/sc/support/corona_notice.jsp'):
                # print(link_list.attrs['href'])
                url.append(link_t)                 
            
            del link_t
    
    # return
    list_ = []

    for i in range(len(title)):
        list_.append(makeGroup(cf.YNS_STIE_CORONA, title[i], sign[i], url[i]))
        
    return list_
    
         

def parseTextEngDepart(text):

    # YNS_SITE_MAIN
    soup = BeautifulSoup(text, 'html.parser') # filter
    soup = BeautifulSoup(str(soup.find('tbody')), 'html.parser')

    # Each notice information
    title = []
    sign = [] # unnecessary
    url = []   

    # title
    for title_list in soup.find_all('td', class_='Subject'): # title
        title.append(" ".join(title_list.text.split()))

    for sign_list in soup.find_all('td', class_='board_date'): 
        sign.append( '공과대학 {date}'.format(date=" ".join(sign_list.text.split())))
        # information, like 공과대학 2020.02.04

    for link_list in soup.findAll("a"):
        if 'href' in link_list.attrs:            
            link_t = link_list.attrs['href'] # temporary           
            url.append(link_t)   

            del link_t    

     # return
    list_ = []

    for i in range(len(title)):
        list_.append(makeGroup(cf.YNS_SITE_ENG_BASE, title[i], sign[i], url[i]))

    # print(url)

    return list_


# 
# script
if __name__ == '__main__':
    
    cf.projectBanner()

    eng_05_01 = parseTextEngDepart(getText(cf.YNS_SITE_ENG_05_01))
    eng_05_03 = parseTextEngDepart(getText(cf.YNS_SITE_ENG_05_03))

    for info in eng_05_03:
        print(info)
        pass

    