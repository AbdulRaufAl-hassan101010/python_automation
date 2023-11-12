#! python3

import re
import pyperclip


# TODO: create a regex from phone number
phoneNumRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
    (\(\d{3}\)|\d{3})? #area code (optional) 
    (-|\s)? #first separator
    \d{3} # 3 digits
    - # separator
    \d{4} # 4 digits
    (\s(ext(\s?\.)?|x)\s?\d{2,5})?
) #extension (optional)
''', re.VERBOSE)


# TODO: create a regex from email
emailRegex = re.compile(r'[A-Za-z0-9_.+]+@[A-Za-z0-9_.+]+\.com')


# TODO: get text off the clipboard
text = pyperclip.paste()


# TODO: extract phone/email from this text
extractedPhones = phoneNumRegex.findall(text)
phoneList = [phone[0] for phone in extractedPhones]

extractedEmails = emailRegex.findall(text)


# TODO: copy the extracted text unto the clipboard
results = '\n'.join(phoneList) + '\n' + '\n'.join(extractedEmails)
pyperclip.copy(results)
