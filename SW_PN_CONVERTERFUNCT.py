#SW_PN_CONVERTER2
#Response type->[11:36:41 a. m.] -288    52.731 6    D_MF-RS     04C2      54      53 62 F1 22 36 38 34 35 33 35 31 38 41 41 36 38 34 35 33 35 31 38 41 41 36 38 34 35 33 35 31 38 41 41 36 38 
import os
import re
###################################################################################################################
#globals
declist=""

def asciihex2dec(gsaresponse):
    global declist
    pairregex=re.compile(r'\d\d')
    pairlist=re.findall(pairregex,gsaresponse)
    for x in pairlist:
        type(declist)
        declist=declist+(str(chr(int(x,16))))
def findpn():
    pnregex=re.compile(r'\d\d\d\d\d\d\d\d[A-Z]{2}')
    pnlist=re.findall(pnregex,declist)
    return pnlist
def pn2txt(pnlist):
    txt=""
    file=open('PNLIST.txt','a')
    for x in pnlist:
        txt=txt+x+'\n'
    file.write(str(txt))
    file.close()
    os.system('PNLIST.txt')
    os.system('del PNLIST.txt')

#main

gsaresponse=input('Enter the gsa response here\n')
asciihex2dec(gsaresponse)
pnlist=findpn()
pn2txt(pnlist)
