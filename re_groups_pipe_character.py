#! python3
import re

message ='(415)-555-1111'

phoneNumRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
mo = phoneNumRegex.search(message)


batRegex = re.compile(r'Bat(man|mobile|bat)')
mo = batRegex.search('Batman is awesome!!')
print(mo)

if mo:
    print(mo.group())   
    print(mo.group(1))  
else:
    print("No phone number found in the message")
