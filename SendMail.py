from smtplib import SMTP

# Simple Name Transfer Protocol

try:
    subject = "Test"
    message = "content"
    content = "Subject: {0}\n\n{1}".format(subject,message)

    myMailAdress = "youremail"
    password = "yourpassword"

    sendTo = "any email"

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)
    mail.sendmail(myMailAdress,sendTo,content.encode("utf-8"))
    print("Commit")
except Exception as e:
    print("Error Handle\n {0}".format(e))