import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds(s)...\n')
    time.sleep(seconds)
    return 'Done Sleeping...'+str(seconds)
#Using concurrent.futures I can create a pool of threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,1,2,4,7]
    results=[executor.submit(do_something,sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
#using map would be:
#results = executor.map(do_something, secs)
#for result in results:
#       print(result)

finish= time.perf_counter()
print(f'Finished in {round(finish-start,2)}seconds(s)')
