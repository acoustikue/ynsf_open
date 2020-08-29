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
import haksa_v2 as hk
import db
import fcm

#
# show banner
cf.projectBanner()

print('{color}haksa_v2 run.'.format(color=cf.bcolors.ENDC))

# first parse necessary infos

d_day_7 = hk.checkUpcoming(hk.parseTextHaksa(ps.getText(cf.YNS_SITE_HAKSA)), 7)
d_day_3 = hk.checkUpcoming(hk.parseTextHaksa(ps.getText(cf.YNS_SITE_HAKSA)), 3)
d_day_1 = hk.checkUpcoming(hk.parseTextHaksa(ps.getText(cf.YNS_SITE_HAKSA)), 1)

# send noty
for plan in d_day_7: 
    fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '연세대학교 학사 일정 알림(D-7)', '{body}'.format(body=plan), '')
    
for plan in d_day_3: 
    fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '연세대학교 학사 일정 알림(D-3)', '{body}'.format(body=plan), '')
    
for plan in d_day_1: 
    fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '연세대학교 학사 일정 알림(D-1)', '{body}'.format(body=plan), '')

    
print('{color}haksa_v2 done.'.format(color=cf.bcolors.ENDC))
    