import pprint
text=input('Write the text whose characters you want to count:')
count={}
for character in text.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint (count)
