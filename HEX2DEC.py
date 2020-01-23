
#HEX2DEC.py
#Type of response: [11:02:32 a. m.] -142    13.298 8    D_RS        04C2      08      06 62 F1 53 11 1D 00 00
###########################################################################################################################################################

#Modules
import os
import re


#globals
declist=""


#functions
def asciihex2dec(gsaresponse):
    global declist
    pairregex=re.compile(r'[a-fA-F0-9]+')
    pairlist=re.findall(pairregex,gsaresponse)
    for x in pairlist:
        declist=declist+str(int(x,16))+' '   
    return declist

def pn2txt(declist):
    file=open('DECLIST.txt','w')
    file.write(str(declist))
    file.close()
    os.system('DECLIST.txt')
    os.system('del DECLIST.txt')

#main

gsaresponse=input('Enter the gsa response here\n')
declist=asciihex2dec(gsaresponse)
pn2txt(declist)


