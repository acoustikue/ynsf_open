# [Project YNS] Yonsei Univ. Notification Service, Project KNSF based.
# 0.1.0va, 20.02.02. First launched.
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
# since KNSF can be distinguished by only methods of sending notifications to devices.

# YNS used FCM for push service, and used Flask as a server for getting devices' tokens.
# In this source there is no relation with the Flask server.

# Database added, for device token control and saving previous notices.
#
