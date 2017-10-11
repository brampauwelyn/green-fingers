
# Function to send email via SMTP

# In order to make this function work you need to make a config file
# with the credentials of your gmail address (username & password)
# you also need to add the variables fromEmail & toEmail

def notify():
    import smtplib
    # import variables from config file
    from config import USERNAME, PASSWORD, FROM_EMAIL, TO_EMAIL
    msg = "\r\n".join([
      "From:" + FROM_EMAIL,
      "To:" + TO_EMAIL,
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


# Function to send email via Mailgun

def notify_mailgun():
    import requests
    from config import MAILGUN_API_KEY, MAILGUN_SANDBOX, MAILGUN_SANDBOX_EMAIL, TO_EMAIL
    return requests.post(
        "https://api.mailgun.net/v3/sandbox"+ MAILGUN_SANDBOX +".mailgun.org/messages",
        auth=("api", MAILGUN_API_KEY),
        files=[("attachment", ("plant.png", open("images/plant.png","rb").read()))],
        data={"from": "Green Fingers" + MAILGUN_SANDBOX_EMAIL,
              "to": TO_EMAIL,
              "subject": "You're plants got water",
              "text": "You're plants got water!",
              "html": "<html> &#x1F331; HTML version of the body</html>"})

notify_mailgun()
