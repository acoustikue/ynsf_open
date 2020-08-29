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
import db

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#
# load registered mail address
YNS_SMTP_REGISTERED = []

for device in  db.dbFindSTMPRegistered():
    YNS_SMTP_REGISTERED.append(device['title'])
    
# YNS_SMTP_REGISTERED = " ".join(YNS_SMTP_REGISTERED)


# Email validation
def is_addr_valid(addr):
    
    import re
    if re.match('(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
        return True
    else:
        return False
    
    
def send_mail(addr, content):
    
    # if not is_addr_valid(addr):
    #     return
    
    #
    # user info
    YNS_SMTP_USER = db.dbFindSTMP()
    
    msg = MIMEText(content, _charset='utf-8')
    msg['Subject'] = '[YNSF] 새로운 공지 사항이 있습니다.'
    msg['From'] = 'acoustikue@yonsei.ac.kr'
    msg['To'] = ",".join(addr)
    
    YNS_SMTP_SERVER = smtplib.SMTP_SSL(cf.YNS_SMTP_SERVER, cf.YNS_SMTP_PORT)
    YNS_SMTP_SERVER.login(YNS_SMTP_USER["title"], YNS_SMTP_USER['sign']) # For same format
    YNS_SMTP_SERVER.sendmail('acoustikue@yonsei.ac.kr', addr, msg.as_string())


def send_mail2(addr, content):

    YNS_SMTP_USER = db.dbFindSTMP()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = '[YNSF] {0}'.format('Notice updates.')
    msg['From'] = 'acoustikue@yonsei.ac.kr'
    msg['To'] = ",".join(addr)
    
    msg.attach(MIMEText('New notice updates.', 'plain'))
    msg.attach(MIMEText(content, 'html'))
    
    YNS_SMTP_SERVER = smtplib.SMTP_SSL(cf.YNS_SMTP_SERVER, cf.YNS_SMTP_PORT)
    YNS_SMTP_SERVER.login(YNS_SMTP_USER["title"], YNS_SMTP_USER['sign']) # For same format
    YNS_SMTP_SERVER.sendmail('acoustikue@yonsei.ac.kr', addr, msg.as_string())


    
def generate_mail_content(n_notice_list):
    
    content = '업데이트된 새로운 공지입니다.\n\n'
    
    for info in n_notice_list:
        content = content + '{title}\n{site}{url}\n'.format(title=info['title'], site=info['site'], url=info['url'])
    
    content_tail = '\n문의사항이나 구독 취소 신청은 acoustikue@yonsei.ac.kr로 연락 주십시오.'
    content = content + content_tail
    
    return content


def generate_mail_content_nyscec(n_notice_list):
    # This additional function was added from nyscec.

    mail_content = ''

    html_frame_upper = '<!doctype html><html> <head> <meta name="viewport" content="width=device-width" /> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> <title>Simple Notice Form</title> <style> img { border: none; -ms-interpolation-mode: bicubic; max-width: 100%; } body { background-color: #f6f6f6; font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0; padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; } table { border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; } table td { font-family: sans-serif; font-size: 14px; vertical-align: top; } /* ------------------------------------- BODY & CONTAINER ------------------------------------- */ .body { background-color: #f6f6f6; width: 100%; } /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */ .container { display: block; margin: 0 auto !important; /* makes it centered */ max-width: 580px; padding: 10px; width: 580px; } .content { box-sizing: border-box; display: block; margin: 0 auto; max-width: 580px; padding: 10px; } /* ------------------------------------- HEADER, FOOTER, MAIN ------------------------------------- */ .main { background: #ffffff; border-radius: 3px; width: 100%; } .wrapper { box-sizing: border-box; padding: 20px; } .content-block { padding-bottom: 10px; padding-top: 10px; } .footer { clear: both; margin-top: 10px; text-align: center; width: 100%; } .footer td, .footer p, .footer span, .footer a { color: #999999; font-size: 14px; text-align: center; } /* ------------------------------------- TYPOGRAPHY ------------------------------------- */ h1, h2, h3, h4 { color: #000000; font-family: sans-serif; font-weight: 400; line-height: 1.4; margin: 0; margin-bottom: 30px; } h1 { font-size: 35px; font-weight: 300; text-align: center; text-transform: capitalize; } p, ul, ol { font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px; } p li, ul li, ol li { list-style-position: inside; margin-left: 5px; } a { color: #3498db; text-decoration: underline; } /* ------------------------------------- BUTTONS ------------------------------------- */ .btn { box-sizing: border-box; width: 100%; } .btn > tbody > tr > td { padding-bottom: 15px; } .btn table { width: auto; } .btn table td { background-color: #ffffff; border-radius: 5px; text-align: center; } .btn a { background-color: #ffffff; border: solid 1px #3498db; border-radius: 5px; box-sizing: border-box; color: #3498db; cursor: pointer; display: inline-block; font-size: 14px; font-weight: bold; margin: 0; padding: 12px 25px; text-decoration: none; text-transform: capitalize; } .btn-primary table td { background-color: #3498db; } .btn-primary a { background-color: #3498db; border-color: #3498db; color: #ffffff; } /* ------------------------------------- OTHER STYLES THAT MIGHT BE USEFUL ------------------------------------- */ .last { margin-bottom: 0; } .first { margin-top: 0; } .align-center { text-align: center; } .align-right { text-align: right; } .align-left { text-align: left; } .clear { clear: both; } .mt0 { margin-top: 0; } .mb0 { margin-bottom: 0; } .preheader { color: transparent; display: none; height: 0; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all; visibility: hidden; width: 0; } .powered-by a { text-decoration: none; font-size: 14px; } hr { border: 0; border-bottom: 1px solid #f6f6f6; margin: 20px 0; } /* ------------------------------------- RESPONSIVE AND MOBILE FRIENDLY STYLES ------------------------------------- */ @media only screen and (max-width: 620px) { table[class=body] h1 { font-size: 28px !important; margin-bottom: 10px !important; } table[class=body] p, table[class=body] ul, table[class=body] ol, table[class=body] td, table[class=body] span, table[class=body] a { font-size: 16px !important; } table[class=body] .wrapper, table[class=body] .article { padding: 10px !important; } table[class=body] .content { padding: 0 !important; } table[class=body] .container { padding: 0 !important; width: 100% !important; } table[class=body] .main { border-left-width: 0 !important; border-radius: 0 !important; border-right-width: 0 !important; } table[class=body] .btn table { width: 100% !important; } table[class=body] .btn a { width: 100% !important; } table[class=body] .img-responsive { height: auto !important; max-width: 100% !important; width: auto !important; } } /* ------------------------------------- PRESERVE THESE STYLES IN THE HEAD ------------------------------------- */ @media all { .ExternalClass { width: 100%; } .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div { line-height: 100%; } .apple-link a { color: inherit !important; font-family: inherit !important; font-size: inherit !important; font-weight: inherit !important; line-height: inherit !important; text-decoration: none !important; } #MessageViewBody a { color: inherit; text-decoration: none; font-size: inherit; font-family: inherit; font-weight: inherit; line-height: inherit; } .btn-primary table td:hover { background-color: #34495e !important; } .btn-primary a:hover { background-color: #34495e !important; border-color: #34495e !important; } } </style> </head> <body class=""> <!-- <span class="preheader">This is preheader text. Some clients will show this text as a preview.</span> --> <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body"> <tr> <td>&nbsp;</td> <td class="container"> <div class="content"> <!-- START CENTERED WHITE CONTAINER --> <table role="presentation" class="main"> <!-- START MAIN CONTENT AREA --> <tr> <td class="wrapper"> <table role="presentation" border="0" cellpadding="0" cellspacing="0"> <tr> <td><p>Hi there, <br>there are some new updates from Yonsei notice boards.</p>'
    html_frame_lower = '<p>From YNSF.</p></td> </tr> </table> </td> </tr> <!-- END MAIN CONTENT AREA --> </table> <!-- END CENTERED WHITE CONTAINER --> <!-- START FOOTER --> <div class="footer"> <table role="presentation" border="0" cellpadding="0" cellspacing="0"> <tr> <td class="content-block"> <span class="apple-link">You are receiving this letter due to the agreement of subscription.</span><br> Send your information to <u><a href="mailto:acoustikue@yonsei.ac.kr">acoustikue@yonsei.ac.kr</a></u> to unsubscribe. </td> </tr> <tr> <td class="content-block powered-by"> Provided by <u><a href="https://github.com/dev-acoustikue">acoustikue</a></u> (SukJoon Oh). </td> </tr> </table> </div> <!-- END FOOTER --> </div> </td> <td>&nbsp;</td> </tr> </table> </body></html>'

    for info in n_notice_list:
        mail_content = mail_content + '<p> <b>{title}</b> <br><a href="{site}{url}"> Click here to open link. </a></p>'.format(title=info['title'], site=info['site'], url=info['url'])

    mail_content = html_frame_upper + mail_content + html_frame_lower

    return mail_content
    
# 
# script
if __name__ == "__main__":
    
    cf.projectBanner()
    
    sample_notice = [{"site": cf.YNS_SITE_MAIN, "title": "샘플 공지입니다. (2020.03.)", "sign": "연세대학교 임시 부서", "url": "sample_url"}, {"site": cf.YNS_SITE_MAIN, "title": "샘플 공지입니다. 2 (2020.03.)", "sign": "연세대학교 임시 부서", "url": "sample_url"}]
    
    print(YNS_SMTP_REGISTERED)
    send_mail2(YNS_SMTP_REGISTERED, generate_mail_content_nyscec(sample_notice))
    
    
    
    
    
    
    
    
