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


from pyfcm import FCMNotification

import config as cf # user
import db

# 
# save device token to database as, 
# 1. site: "device"
# 2. title: ""
# 3. sign: ""
# 4. url: "device token goes here"

# read server api key in a form of,
# 1. site: "key"
# 2. title: ""
# 3. sign: ""
# 4. url: "server api key goes here"

# intial set
YNS_FCM_APIKEY = db.dbFindApiKey()
YNS_FCM_APIKEY = YNS_FCM_APIKEY['url']
YNS_FCM_SERVER = FCMNotification(YNS_FCM_APIKEY)

YNS_FCM_DEVICES = []

for device in  db.dbFindDevices({"site": "device"}):
    YNS_FCM_DEVICES.append(device['url'])

#
# acoustikue
def sendToSingleDevice(device):
    pass

def sendToMultipleDevice(devices, msg_title, msg_body, msg_action):
    # self.fcm_service.notify_multiple_devices(registration_ids=self.device_token_list, message_title=m_title, message_body=m_body, click_action=action)
    YNS_FCM_SERVER.notify_multiple_devices(registration_ids=devices, message_title=msg_title, message_body=msg_body, click_action=msg_action)
    



#
# script
if __name__ == '__main__':
    cf.projectBanner()
    
    print('{color}Server api key: {key}'.format(color=cf.bcolors.ENDC, key=YNS_FCM_APIKEY))
    print('{color}Server: {key}'.format(color=cf.bcolors.ENDC, key=YNS_FCM_SERVER))
    
    print('{color}Devices: {devices}'.format(color=cf.bcolors.ENDC, devices=YNS_FCM_DEVICES))
