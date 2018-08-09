# EmailPhoneSearcher

import re
import pyperclip
mo = None  # declare 'noneType' var for if statement.
em = None  # declare 'noneType' var for if statement.
y = type(mo)  # do something with variables above to rid PEP-8 error
z = type(em)  # do something with variables above to rid PEP-8 error
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
emailRegex = re.compile(r'[a-zA-Z0-9.!@#$%^&*()?></]+@[a-zA-Z0-9.!@#$%^&*()?></]+')
print('Copy text in which you wish to find a phone number onto the clipboard, then hit enter.')
enter = input()
text = pyperclip.paste()
mo = phoneNumberRegex.findall(text)
em = emailRegex.findall(text)
if mo is None and em is None:
    print('There are no phone numbers or emails in inserted text.')
elif mo is None and em is not None:
    print('No phone numbers found.')
    for i in em:
        print('Email Found:', em)
elif mo is not None and em is None:
    print('No email addresses found')
    for j in mo:
        print('Phone Number Found:', mo)
else:
    for i in em:
        print('Emails Found: ', i)
    for j in mo:
        print('Phone Numbers Found: ', j)

# end
