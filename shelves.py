import shelve

def new_shelf():
    s = shelve.open('test_shelf.db')
    try:
        s['key1'] = { 'int': 12, 'float':9.5, 'string':'Sample data' }
    finally:
        s.close()
def open_shelf():
    s = shelve.open('test_shelf.db')
    try:
        existing = s['key1']
        print (existing)
    except:
        print('There is no shelf with that name')
    finally:
        s.close()
    
    
new_shelf()
open_shelf()
