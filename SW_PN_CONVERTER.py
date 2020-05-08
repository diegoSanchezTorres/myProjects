#HEX2DEC
#Response type->[11:36:41 a. m.] -288    52.731 6    D_MF-RS     04C2      54      53 62 F1 22 36 38 34 35 33 35 31 38 41 41 36 38 34 35 33 35 31 38 41 41 36 38 34 35 33 35 31 38 41 41 36 38 
import os
import re
gsaresponse=input('Enter the gsa response here\n')
pnregex=re.compile(r'(\d\d \d\d \d\d \d\d \d\d \d\d \d\d \d\d 4\d 4\d)')
pnlist=re.findall(pnregex,gsaresponse)
print(pnlist)
for x in pnlist:
    pnfile=open('PNLIST.txt','a')
    pnlistdec=x[1]+x[4]+x[7]+x[10]+x[13]+x[16]+x[19]+x[22]+chr(int(x[24:26],16))+chr(int(x[27:29],16))+'\n'
    pnfile.write(pnlistdec)
    pnfile.close()
os.system('PNLIST.txt')
os.system('del PNLIST.txt')





