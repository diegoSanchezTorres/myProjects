import re
text='Charlie, eleventh st,telephone 555-232-1232'
telregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=telregex.search(text)
print(mo.group())
