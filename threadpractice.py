import threading
import time

# def sleeper(name):
#     print("Before sleeping{}".format(name))
#     time.sleep(5)
#     print("After sleeping{}".format(name))
thread_object=[]
def sleeper():
    print("Before sleeping")
    time.sleep(5)
    print("After sleeping{}")
def loop():
    while True:
        print("loop running")
for i in range(10):
    t=threading.Thread(target=sleeper)
    thread_object.append(t)


# t1=threading.Thread(target=sleeper)
# t2=threading.Thread(target=sleeper)
# t3=threading.Thread(target=sleeper)

for thread in thread_object:
    thread.start()

for thread in thread_object:
    thread.join()

# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
print("finished")