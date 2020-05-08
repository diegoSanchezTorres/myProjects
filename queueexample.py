import queue

shoppingline=queue.Queue()#first in first out, for stack use queue.LifoQueue()
for i in range (7):
    shoppingline.put(i)
print(shoppingline)
print(shoppingline.queue)
print(shoppingline.empty())
print(shoppingline.get())
print(shoppingline.queue)
while not shoppingline.empty():
    shoppingline.get()
print(shoppingline.queue)
