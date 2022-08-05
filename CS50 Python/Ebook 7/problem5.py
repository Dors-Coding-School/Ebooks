import re
def text_match(text):
 if re.search(r'ab{2,3}?', text):
 return 'Found a match!'
 else:
 return('Not matched!')
print(text_match("abbb"))
print(text_match("aabbbbbc"))
