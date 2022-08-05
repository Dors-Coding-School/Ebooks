import re
def text_match(text):
 if re.search(r'ab+?', text):
 return 'Found a match!'
 else:
 return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))
