import smtplib
# stands for Simple Mail Transfer Protocol

my_email = "yongyetan1209@gmail.com"
password = "khurjsfbgdystvlg"

'''
correct smtp address for email provider
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com
'''


try:
    # Create SMTP session
    connection = smtplib.SMTP('smtp.gmail.com', port=587,timeout=30)

    # Use TLS to add security
    connection.starttls()

    # User Authentication
    connection.login(my_email, password)

    # Sending the email
    connection.sendmail(my_email, "Jefzen28@gmail.com", "Hi")

    # Terminating the session
    connection.quit()
    print("Email sent successfully!")
except Exception as error:
    print("Something went wrong....", error)



