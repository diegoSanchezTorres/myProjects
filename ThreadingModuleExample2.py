import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')  
##t1= threading.Thread(target=do_something)
##t2= threading.Thread(target=do_something)
threadlist=[]
for _ in range(10):
    t=threading.Thread(target=do_something)
    t.start()
    threadlist.append(t)
for thr in threadlist:
    thr.join()
##t1.start()
##t2.start()
##t1.join()
##t2.join()
##do_something()
##do_something()

finish= time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
