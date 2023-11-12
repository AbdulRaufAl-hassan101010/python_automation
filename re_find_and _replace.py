import re
 
message = "Agent Mike called Agent Smith yesterday."
messageRegex = re.compile(r'Agent (\w)\w*')
mo = messageRegex.findall(message)
print(mo)
print(messageRegex.sub(r'Agent \1****', message))
