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

#
# Database design(main site)
# 1. site: "https://www.yonsei.ac.kr/sc/support/notice.jsp"
# 2. title: "2020학년도 1학기 선택교양 일몰 교과목 재수강 지정 목록 및 신청 안내"
# 3. sign: "신촌/국제 학부대학 2020.02.04"
# 4. url: "https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=181932&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15"

# 
# commands
# service mongod start
# mongo admin -u ynsf -p 'acoustikue1ynsf'
# show dbs
# use ynsf, db.notice.find({}), db.notice.remove({})

import config as cf
import pymongo
# pip3 install pymongo


YNS_DB_CLIENT = pymongo.MongoClient('mongodb://%s:%s@%s' % (cf.YNS_DB_USER, cf.YNS_DB_PASSWORD, 'localhost')) 
YNS_DB_COLLECTION = YNS_DB_CLIENT.ynsf.notice # use ynsf, use notice, if not created create one.


#
# Author: acoustikue
def dbFind(target):
    return YNS_DB_COLLECTION.find_one(target)

def dbFindAll(target):
    return YNS_DB_COLLECTION.find(target)

def dbFindDevice(target):
    return YNS_DB_COLLECTION.find_one(target)

def dbFindDevices(target):
    return YNS_DB_COLLECTION.find(target)

def dbFindApiKey():
    return YNS_DB_COLLECTION.find_one({"site": "key"}) # fixed

def dbInsertOne(target):
    YNS_DB_COLLECTION.insert_one(target)

def dbInsertList(target):
    YNS_DB_COLLECTION.insert_many(target)

def dbRemoveOne(target):
    YNS_DB_COLLECTION.remove(target)
    
def dbFindSTMP():
    return YNS_DB_COLLECTION.find_one({"site": "mail_admin"}) # fixed

def dbFindSTMPRegistered():
    return YNS_DB_COLLECTION.find({"site": "mail"}) # fixed


#
# update function
def dbSaveOne(target):
    
    if not dbFind(target):

        dbInsertOne(target)
        print("{color}Document inserted".format(color=cf.bcolors.OKGREEN))
        
        return target
    
    else: 
        print("{color}Document exists.".format(color=cf.bcolors.FAIL))
        
        return -1
        
 
#
# update needed?
# why?


# 
# script
if __name__ == "__main__":
    
    cf.projectBanner()
    
    # api key
    # dbSaveOne({"site": "key", "title": "", "sign": "", "url": ""})
    
    # # mail smtp
    # dbSaveOne({"site": "mail_admin", "title": "acoustikue@yonsei.ac.kr", "sign": "", "url": ""})
    
    # # my laptop device
    # dbSaveOne({"site": "device", "title": "", "sign": "", "url": ""})

    # Update after deactivation of FCM service
    dbSaveOne({"site": "mail_admin", "title": "acoustikue@yonsei.ac.kr", "sign": "", "url": ""})
    dbSaveOne({"site": "mail", "title": "acoustikue@yonsei.ac.kr", "sign": "", "url": ""})

    # insert more to register other service users



