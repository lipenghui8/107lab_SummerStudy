# import time
# import datetime
# import _thread
# date_time_format="%H:%M:%S"
# def get_time_str():
#     now=datetime.datetime.now()
#     return datetime.datetime.strftime(now,date_time_format)
# def thread_function(thread_id,lock):
#     print("Thread %d\t strat at %s"%(thread_id,get_time_str()))
#     print("Thread %d\t sleeping"%thread_id)
#     time.sleep(5)
#     print("Thread %d\t finish at %s"%(thread_id,get_time_str()))
#     lock.release()
#
# def main():
#     print("Main thread start at %s"%get_time_str())
#     # for i in range(6):
#     #     _thread.start_new_thread(thread_function,(i,))
#     #     time.sleep(1)
#     # time.sleep(5)
#     locks=[]
#     for i in range(5):
#         lock=_thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#     for i in range(5):
#             _thread.start_new_thread(thread_function,(i,locks[i]))
#             time.sleep(1)
#     for i in range(5):
#             while locks[i].locked():
#                 time.sleep(1)
#     print("Main thread finish at %s"%get_time_str())
# if __name__=="__main__":
#     main()
import time
import datetime
import threading
date_time_format="%H:%M:%S"
def get_time_str():
    now=datetime.datetime.now()
    return datetime.datetime.strftime(now,date_time_format)
def thread_function(thread_id):
    print("Thread %d\t strat at %s"%(thread_id,get_time_str()))
    print("Thread %d\t sleeping"%thread_id)
    time.sleep(5)
    print("Thread %d\t finish at %s"%(thread_id,get_time_str()))

def main():
    print("Main thread start at %s"%get_time_str())
    threads=[]
    for i in range(5):
        thread=threading.Thread(target=thread_function,args=(i,))
        threads.append(thread)
    for i in range(5):
        threads[i].start()
        time.sleep(1)
    for i in range(5):
        threads[i].join()
    print("Main thread finish at %s"%get_time_str())
if __name__=="__main__":
    main()