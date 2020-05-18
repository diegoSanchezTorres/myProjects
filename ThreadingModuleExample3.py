import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds(s)...\n')
    time.sleep(seconds)
    return 'Done Sleeping'
#Using concurrent.futures I can create a pool of threads
with concurrent.futures.ThreadPoolExecutor() as executor:
#for multiple tasks you can also use loops
    f1= executor.submit(do_something,3)
    f2= executor.submit(do_something,2)
    f3= executor.submit(do_something,1)
    f4= executor.submit(do_something,4)
    print(f1.result())
    print(f2.result())
    print(f3.result())
    print(f4.result())

finish= time.perf_counter()
print(f'Finished in {round(finish-start,2)}seconds(s)')
