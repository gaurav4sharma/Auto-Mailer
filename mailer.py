import smtplib
from email.message import EmailMessage


def email_sender(name, to_adr):
    msg = EmailMessage()
    msg['Subject']= 'Business Partnership with Trell'
    msg['From'] = 'collaboration@trell.in'
    msg['To'] = to_adr
    msg.set_content('')
    
    msg.add_alternative(f"""\
<!DOCTYPE html>
<html>
<body>
<p>Hi {name},<p>

<p>Message</p>

<p>Thanks & Regards,</p>
<p>Sender</p>

</body>
</html>
    """, subtype = 'html')
    
    sender(msg)


def sender(msg):    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
    
        smtp.login('Email_ID','Password')
    
        smtp.send_message(msg)
    
        print('Email Sent')


with open('address.txt', 'r') as f:
    for line in f:
        
        print(line.strip())
        lst = line.split()
        name = lst[0]
        to_adr = lst[1]
        email_sender(name, to_adr)