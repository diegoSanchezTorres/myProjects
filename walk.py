# import os
# os.chdir("/home/diego/Home/Desktop/pythonscripts")
# print(os.getcwd())
# print(os.walk("/home/diego/Home/Desktop/pythonscripts/zipstest"))
import os
for root, dirs, files in os.walk("/home/diego/Home/Desktop/pythonscripts/zipstest"):
   for name in files:
      print(os.path.join(root, name))
      