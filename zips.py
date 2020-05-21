# import os
# zipDirs=["/home/diego/Home/Desktop/pythonscripts/zipstest"]
# for folder in zipDirs:
# 	pathfolder=str(folder)
# 	while len(pathfolder) > 255:
# 		x=pathfolder.rfind('/',0,255)
# 		os.popen("cd"+(pathfolder[:x]))
# 		pathfolder= pathfolder[x:]
# 	os.popen("gzip -fr  " +pathfolder)

# import os
# zipDirs=["/home/diego/Home/Desktop/pythonscripts/zipstest"]
# for folder in zipDirs:
# 	pathfolder=str(folder)
# 	while len(pathfolder) > 255:
# 		x=pathfolder.rfind('/',0,255)
# 		os.popen("cd"+(pathfolder[:x]))
# 		pathfolder= pathfolder[x:]
# 	popen("gzip -fr  " +pathfolder)
	



# import os
# zipDirs=["/home/diego/Home/Desktop/pythonscripts/zipstest"]
# for folder in zipDirs:
# 	pathfolder=str(folder)
# 	os.popen("gzip -fr  " +pathfolder)

import os
for root, dirs, files in os.walk("/home/diego/Home/Desktop/pythonscripts/zipstest"):
   for name in files:

      if "Capitulo 17.pdf" in name:
      	continue
      pathfile=os.path.join(root,"'"+name+"'")
      print(pathfile)
      os.popen("gzip -f "+pathfile)


	
