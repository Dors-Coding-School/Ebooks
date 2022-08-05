import re
def text_match(text):
 if re.search(r' ^\w*z.\w*', text):
    return 'Found a match!'
 else:
    return('Not matched!')
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))
