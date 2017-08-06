# Function to send email

# In order to make this function work you need to make a config file
# with the credentials of your gmail address (username & password)
# you also need to add the variables fromEmail & toEmail

def notify():
    import smtplib
    # import variables from config file
    from config import USERNAME, PASSWORD, FROM_EMAIL, TO_EMAIL
    msg = "\r\n".join([
      "From:" + fromEmail,
      "To:" + toEmail,
      "Subject: You're plants got water",
      "",
      "You're plants got water"
      ])
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(USERNAME,PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg)
    server.quit()
