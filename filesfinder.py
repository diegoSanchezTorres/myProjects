import subprocess
def filesfindermod(path):
	print(path)
	result=subprocess.run("find "+path+" -mtime +180",stdout=subprocess.PIPE,shell=True,text=True)
	listresult=result.stdout.splitlines()
	print(listresult)
	print("Number of files modified more than 180 days ago: "+str(len(listresult)))

filesfindermod('/home/diego/Home/"ROMS snes"')

