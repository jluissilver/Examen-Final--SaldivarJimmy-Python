import re
regex = r'^[a-zA-Z0-9\-_\.]+[@][a-z]+[.][c][o][m]$'

emails = ['n.john.smith@gmail.com', '87Victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    
    if re.match(regex, example):
        
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))