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

import datetime

# from collections import OrderedDict

import config as cf
import parse as ps

# Explanation:
# html request process is already contained in parser.
# What the parser need is just url.


# ps.getText()

# This is additional function, 
# lets haksa information and sends noty before a week, 3 days.

# This function will not use database, 
# since schedule may change due to unexpected problems.

MONTH_STR = [
        "01 JAN", 
        "02 FEB", 
        "03 MAR", 
        "04 APR", 
        "05 MAY", 
        "06 JUN", 
        "07 JUL", 
        "08 AUG",
        "09 SEP",
        "10 OCT", 
        "11 NOV",
        "12 DEC"
    ]

#
# Author: acoustikue
def parseTextHaksa(text):
    
    # YNS_SITE_MAIN
    soup = BeautifulSoup(text, 'html.parser') # filter
    soup = BeautifulSoup(str(soup.find('table')), 'html.parser')
    
    schedule = [[], [], [], [], [], [], [], [], [], [], [], []]
    
    last_idx = 0
    raw = []
    
    for list_ in soup.find_all("tr"):
        
        raw = " ".join(list_.text.split())
        
        try:            
            
            last_idx = MONTH_STR.index(raw[0:6])
            schedule[last_idx].append(raw.replace(raw[0:7], ""))
            
        except:
            schedule[last_idx].append(raw)
            
    return schedule
        
    
    
    
    
#
# Author: acoustikue
def checkUpcoming(schedule, d_day):
    
    #
    # This function returns a single string!!

    # 7 days, 
    # 3 days,
    # 1 day left

    d_day_list = []
    
    exp_month = datetime.datetime.now() + datetime.timedelta(days=(d_day + 1))
    
    exp_day = exp_month.day
    exp_month = exp_month.month
    
    # print(exp_day)

    # loop
    for plan in schedule[exp_month - 1]:
        
        if plan[0:2].isdigit(): # case when XX
            
            # print(plan[0:1])
            
            if plan[0:2] == str(exp_day):
                d_day_list.append(plan)
            
        
        elif plan[0].isdigit() and plan[1] == '(': # case when X(
            
            if plan[0] == str(exp_day):
                d_day_list.append(plan)
            
        else:
            pass


    return d_day_list
    
    
    
    

# 
# script
if __name__ == '__main__':
    
    cf.projectBanner()
    
    # print(  parseTextHaksa(ps.getText(cf.YNS_SITE_HAKSA))  )
    print(  checkUpcoming(parseTextHaksa(ps.getText(cf.YNS_SITE_HAKSA)), 7)  )
    
    
    
    
    
    
    
    
    
    