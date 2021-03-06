import threading #Поток
import time

# def clock(interval):
#     while True:
#         print("Thread #{}. Текущее время: {}".format(threading.get_ident(),time.ctime()))
#         time.sleep(interval)
#
# if __name__ == '__main__':
#     t = threading.Thread(target=clock,args=(5,))
#     threads = (threading.Thread(target=clock, args=(5,))
#                for _ in range (10))
#         # t.daemon - True
#     for thread in threads:
#                 thread.start()
#                 # t.start()

# class ClockThread(threading.Thread):
#     def __init__(self, interval, daemon=True):
#         super().__init__()
#         self.daemon = daemon
#         self.interval = interval
#
#     def run(self):
#         while True:
#             print("Thread #{}. Текущее время: {}".format(threading.get_ident(), time.ctime()))
#             time.sleep(self.interval)
#
# if __name__ == '__main__':
#     t = ClockThread(15)
#     t.start()
#
#
# from threading import Lock
#
# lock = Lock()
# lock.acquire()
# lock.release()


# import threading
# protected_resource = 0
# unprotected_resource = 0
# NUM = 5000000
# mutex = threading.Lock()
#
#
# def safe_plus():
#     """  Потокобезопасный инкремент """
#     global protected_resource
#     for i in range(NUM):
#         mutex.acquire()
#         protected_resource += 1
#         mutex.release()
#
#
# def safe_minus():
#     """  Потокобезопасный декремент """
#     global protected_resource
#     for i in range(NUM):
#         mutex.acquire()
#         protected_resource -= 1
#         mutex.release()
#
#
# def risky_plus():
#     """  Инкремент без блокировки """
#     global unprotected_resource
#     for i in range(NUM):
#         unprotected_resource += 1
#
#
# def risky_minus():
#     """  Декремент без блокировки """
#     global unprotected_resource
#     for i in range(NUM):
#         unprotected_resource -= 1
#
#
# if __name__ == '__main__':
#     thread1 = threading.Thread(target=safe_plus)
#     thread2 = threading.Thread(target=safe_minus)
#     thread3 = threading.Thread(target=risky_plus)
#     thread4 = threading.Thread(target=risky_minus)
#     thread1.start()
#     thread2.start()
#     thread3.start()
#     thread4.start()
#     thread1.join()
#     thread2.join()
#     thread3.join()
#     thread4.join()
#     print('Результат при работе с блокировкой %s' % protected_resource)
#     print('Результат без блокировки %s' % unprotected_resource)


# import json
# import time
# from threading import Thread, Lock, RLock
#
# lock = RLock()
#
# people_from_first_db = [
#     {
#         "firstName" : "Leon",
#         "lastName" : "Mask",
#         "age" : 48
#     },
#     {
#         "firstName" : "Alan",
#         "lastName" : "Turning",
#         "age" : 41
#     }
# ]
#
# people_output = []
#
#
# def write_json():
#     lock.acquire()
#     with open("data.json", "w") as fp:
#         json.dump({"people": people_from_first_db}, fp)
#     lock.release()
#
#
# def get_first_part():
#     lock.acquire()
#     first_part = {}
#     with open("data.json", "r") as fp:
#         data = json.load(fp)
#         people = data.get('people', [])
#         if people:
#             try:
#                 first_part = people[0]
#             except (IndexError, ValueError) as ex:
#                 pass
#         lock.release()
#         return first_part
#
#
# def get_second_part():
#     lock.acquire()
#     second_part = {}
#     with open("l9_file.json", "r") as fp:
#         data = json.load(fp)
#         people = data.get('people', [])
#         if people:
#             try:
#                 second_part = people[1]
#             except (IndexError, ValueError) as ex:
#                 pass
#         lock.release()
#         return second_part
#
#
# def get_both_parts():
#     while people_output != people_from_first_db:
#         lock.acquire()
#         first = get_first_part()
#         if first:
#             people_output.append(first)
#         second = get_second_part()
#         if people_output and second:
#             people_output.append(second)
#             lock.release()
#             time.sleep(3)
#
#
# if __name__ == "__main__":
#     t1 = Thread(target=write_json(), daemon=True)
#     t2 = Thread(target=get_both_parts(), daemon=True)
#     t3 = Thread(target=get_both_parts(), daemon=True)
#     t2.start()
#     t3.start()
#     time.sleep(5)
#     print(people_output)
#
#
''''
    
    from threading import Semaphore
    
    s = Semaphore(5)
    #  Если не передавать в Semaphore параметр,
    # Семафор будет инициализирован 1
    # ( и таким образом станет обычной блокировкой)
    s.acquire() #  уменьшает счетчик на -1
    # ... доступ к общему ресурсу
    s.release() # увеличивает счетчик на +1
    '''
#
# from threading import  Event
# event = Event()
# event.wait()
# event.set()
# event.clear()

import  time
from threading import Thread, Event, get_ident

event = Event()
variable = ""

def producer():
    event.set()
    global variable
    variable += "Big data is my skill"
    print("Producer say: All whait, I'm busy!")
    time.sleep(5)


def consumer(thread_id):
    while True:
        event.wait()
        print("{} - Я взял! Вот что там было: {}".format(thread_id, variable))

if __name__ == '__main__':
    threads = (Thread(target=consumer, args=(thread_id,))
               for thread_id in range(10))
    producer()
    for t in threads:
        t.start()
    event.clear()


mutex = threading.RLock()

cond = threading.Condition(mutex)