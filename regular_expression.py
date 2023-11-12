#! python3
import re

message ='415-555-1111 415-555-1111'

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phoneNumRegex.search(message)
mo = phoneNumRegex.findall(message)
print(mo)
