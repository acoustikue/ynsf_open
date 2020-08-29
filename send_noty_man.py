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

import config as cf
import parse as ps
import db
import fcm

#
# show banner
cf.projectBanner()

_title = '웹푸시 종료 안내'
_body = '이제 외부기관공고, 코로나19관련 공지사항 탭 소식도 받아보실 수 있습니다.'
_body2 = '웹푸시를 지원하지 않는 디바이스(iOS)를 위해 메일로도 알림 받을 수 있도록 지원하고 있습니다. 메일 등록을 원하시면 acoustikue@yonsei.ac.kr로 연락 주십시오.'
_body3 = '이제 공과대학 공지사항, 공과대학 공모전 페이시 소식도 받아보실 수 있습니다.'
_body4 = '학사일정 알림의 서버시간 차로 인해 새벽에 알림이 갈 수 있습니다. 현재 조정 중에 있으니 기다려주시기 바랍니다.'
_body5 = '공지드린 바와 같이 Web Push 알림 서비스를 현시간부로 종료합니다. 감사합니다.'


#
# send noty
# fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '{title}'.format(title=_title), '{body}'.format(body=_body3), '')
# fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '{title}'.format(title=_title), '{body}'.format(body=_body2), '')
# fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '{title}'.format(title=_title), '{body}'.format(body=_body4), '')
fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '{title}'.format(title=_title), '{body}'.format(body=_body5), '')


    
# send notification
# code goes here.


# done.

