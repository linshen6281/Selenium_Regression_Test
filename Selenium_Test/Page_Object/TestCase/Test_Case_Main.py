import os
import smtplib
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

from BeautifulReport import BeautifulReport
import datetime
if __name__ == '__main__':
    # ts = unittest.TestSuite()
    # suit1 = unittest.TestLoader().discover(start_dir="./", pattern="Test_*.py")
    # ts.addTest(suit1)
    # result = BeautifulReport(ts)
    # report_dir = "../Report"
    # filename = "Report_" + datetime.datetime.now().strftime("%Y%m%d%H%M") + ".html"
    # result.report(filename=filename, report_dir=report_dir, description="This is the first report")


    file_name = "..\Report\Report_202011082224.html"
    f = open(file_name, "rb")
    with open(file_name, 'rb') as file:
        mail_body = file.read()
        text = MIMEText(mail_body.decode('utf-8'), 'html')
        msg = MIMEMultipart('mixed')
        msg.attach(MIMEText('Hi，all！附件是接口自动化测试报告，请查收，自动发送，无需回复~', 'plain', 'utf-8'))
        # msg.attach(MIMEText(mail_body.decode('utf-8'), 'html'))
        text.add_header("Content-Disposition", "attachment", filename=("utf-8", "", "接口自动化测试报告.html"))
        msg.attach(text)

    sender = "584143918@qq.com"
    receiver = "584143918@qq.com"
    # msg = MIMEText(mail_body.decode('utf-8'), 'html')
    msg['Subject'] = Header("自动化测试报告", "utf-8")
    msg['From'] = sender
    msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("584143918@qq.com", "lpkvtwbaylnsbbig")
    try:
        smtp.sendmail(sender, receiver, msg.as_string())
        print("发送成功")
    except:
        print("发送失败")
    finally:
        smtp.quit()


    # unittest.TextTestRunner().run(ts)
