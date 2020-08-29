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
import mail

#
# show banner
cf.projectBanner()

# first parse necessary infos
list_main = ps.parseTextMain(ps.getText(cf.YNS_SITE_MAIN))
list_ee = ps.parseTextEE(ps.getText(cf.YNS_SITE_EE))
list_ee_seminar = ps.parseTextEESeminar(ps.getText(cf.YNS_SITE_EE_SEMINAR))
list_etc = ps.parseTextEtc(ps.getText(cf.YNS_SITE_ETC))

# added
list_eng_05_01 = ps.parseTextEngDepart(ps.getText(cf.YNS_SITE_ENG_05_01))
list_eng_05_03 = ps.parseTextEngDepart(ps.getText(cf.YNS_SITE_ENG_05_03))

# insert to database
# code goes here.

new_nlist = []
notice = ''

#
# get notice info from main site
print('{color}Main site parsing...'.format(color=cf.bcolors.ENDC))

for obj in list_main: 
    notice = db.dbSaveOne(obj)
    
    if notice != -1:
        new_nlist.append(notice)

print('{color}Done.'.format(color=cf.bcolors.OKGREEN))  

# get notice info from ee site
print('{color}EE site parsing...'.format(color=cf.bcolors.ENDC))

for obj in list_ee: 
    notice = db.dbSaveOne(obj)
    
    if notice != -1:
        new_nlist.append(notice)
    
print('{color}Done.'.format(color=cf.bcolors.OKGREEN))

#
# get notice info from ee seminar site
print('{color}EE seminar site parsing...'.format(color=cf.bcolors.ENDC))

for obj in list_ee_seminar: 
    notice = db.dbSaveOne(obj)
    
    if notice != -1:
        new_nlist.append(notice)
    
print('{color}Done.'.format(color=cf.bcolors.OKGREEN))

#
# get notice info from etc site
print('{color}Etc site parsing...'.format(color=cf.bcolors.ENDC))

for obj in list_etc: 
    notice = db.dbSaveOne(obj)
    
    if notice != -1:
        new_nlist.append(notice)
    
print('{color}Done.'.format(color=cf.bcolors.OKGREEN))

#
# get notice info from eng site
print('{color}Eng 05_01 site parsing...'.format(color=cf.bcolors.ENDC))

for obj in list_eng_05_01: 
    notice = db.dbSaveOne(obj)
    
    if notice != -1:
        new_nlist.append(notice)
    
print('{color}Done.'.format(color=cf.bcolors.OKGREEN))
print('{color}Eng 05_03 site parsing...'.format(color=cf.bcolors.ENDC))

for obj in list_eng_05_03: 
    notice = db.dbSaveOne(obj)
    
    if notice != -1:
        new_nlist.append(notice)
    
print('{color}Done.'.format(color=cf.bcolors.OKGREEN))

#
# send noty
# Web push deprecated!!!
# for notice in new_nlist:
#     fcm.sendToMultipleDevice(fcm.YNS_FCM_DEVICES, '{title}'.format(title=notice['title']), '{body}'.format(body=notice['sign']), '{site}{url}'.format(site=notice['site'], url=notice['url']))

del notice

#
# send mail
if new_nlist: # if not empty
    mail.send_mail(mail.YNS_SMTP_REGISTERED, mail.generate_mail_content(new_nlist))

    
# send notification
# code goes here.


# done.

