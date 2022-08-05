import re
def text_match(text):
 if re.search(r' ^[a-z]+_[a-z]+$', text):
 return 'Found a match!'
 else:
 return('Not matched!')
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc")
