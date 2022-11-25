
from redmail import EmailSender
def sendemail(msg,email):
 mail=[]
 message=msg
 mail.append(email)
 email = EmailSender(
 host="smtp-relay.sendinblue.com",
 port=587,
 username='trueboy2022@gmail.com',
 password='PjQwqcdRxB5vnE8A')
 email.send(
 subject="Alert For Expense Limit Crossing ",
 sender="noreply@expensetracker.com",
 receivers=mail,
 html=message)
