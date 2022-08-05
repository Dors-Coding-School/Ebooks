import re
def is_allowed_specific_char(string):
 s = re.search(r'[^a-zA-Z0-9.]', string)
 return not bool(s)
print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))
