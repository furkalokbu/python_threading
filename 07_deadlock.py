import threading

lock_obj = threading.RLock()

print('Acquaire 1st:')
lock_obj.acquire()

print('Acquire 2nd:')
lock_obj.acquire()

print('Releasing')
lock_obj.release()

# def reentrance():
#     print('start')
#     lock_obj.acquire()
#     print('required')
#     reentrance()

# reentrance()