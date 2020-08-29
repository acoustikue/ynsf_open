#-*- coding:utf-8 -*-

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

import os
import platform
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

# Here the module's base directory will be set to folder where it is located.
# Every config files and other saved files must be in folder below the base directory.

YNS_PROJECT_CODE = 'YNS_l'
YNS_PROJECT_OS = 'Linux'
YNS_PROJECT_SYS = ''
YNS_PROJECT_VERSION = '0.1.3va'

YNS_CURRENT_CODE = 'YNS_l'
YNS_CURRENT_OS = str(platform.system())
YNS_CURRENT_SYS = YNS_CURRENT_OS + ' ' + str(platform.release()) + ' ' + str(platform.version())


YNS_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
YNS_DB_DIR = ''
YNS_MESSAGE_DIR = ''

YNS_SITE_MAIN = 'https://www.yonsei.ac.kr/sc/support/notice.jsp'
YNS_SITE_EE = 'https://ee.yonsei.ac.kr/ee/community/academic_notice.do'
YNS_SITE_HAKSA = 'https://www.yonsei.ac.kr/sc/support/calendar.jsp' # v2
YNS_SITE_EE_SEMINAR = 'https://ee.yonsei.ac.kr/ee/research/seminar.do'
YNS_SITE_ETC = 'https://www.yonsei.ac.kr/sc/support/etc_notice.jsp'

# SET
YNS_SITE_ENG_BASE = 'https://engineering.yonsei.ac.kr/main/'
YNS_SITE_ENG_05_01 = 'https://engineering.yonsei.ac.kr/main/board.asp?mid=m05_01' # Engineering Department main notice
YNS_SITE_ENG_05_03 = 'https://engineering.yonsei.ac.kr/main/board.asp?mid=m05_03' # Engineering Department competition notice

# temporary
YNS_SITE_CORONA = 'https://www.yonsei.ac.kr/sc/support/corona_notice.jsp'


YNS_DB_INFO = 'database.info'
YNS_DB_USER = 'ynsf'
YNS_DB_PASSWORD = 'acoustikue1ynsf'

#
# SMTP Service
YNS_SMTP_SERVER = 'smtp.gmail.com'
YNS_SMTP_PORT = 465

#with open(YNS_DB_INFO, "r", encoding="utf-8") as db_file:
#    lines = db_file.readlines()
#    YNS_DB_USER = lines[0].rstrip()
#    YNS_DB_PASSWORD = lines[1].rstrip()
        
#
# Visual options
class bcolors:
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
#
#
def projectBanner():
    
    print("{color}[Project YNS] Yonsei Univ. Notification Service".format(color=bcolors.HEADER))
    print("{color}0.1.0va, 20.02.02. First launched.".format(color=bcolors.HEADER))
    print("{color}written by acoustikue(SukJoon Oh), Yonsei University EE".format(color=bcolors.HEADER))
    print("{color}{sys}".format(color=bcolors.HEADER, sys=YNS_CURRENT_SYS))

    
# 
# script
if __name__ == "__main__":
    
    projectBanner()
    
    
    
    
    
