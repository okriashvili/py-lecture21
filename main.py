# paralel programing
print("parallel programing")

import time


import threading


# def plan_project():
#     time.sleep(3)
#     print("planning project")
#
#
# def start_project():
#     time.sleep(4)
#     print("start project")
#
#
# def end_project():
#     time.sleep(3)
#     print("end project")
#
# t1 = time.perf_counter()
#
# thread1 = threading.Thread(target=plan_project)
# targetში უნდა გადავცეთ ის ფუნქცია რომელშიც უნდა შევქმნათ სრედები, შენაკადები
# thread2 = threading.Thread(target=start_project)
# thread3 = threading.Thread(target=end_project)
# # იმისათვის რომ პარალელურდ გაეშვას ბრძანებები, ამისათვის უნდა შევქმნათ სრედები/threading.thread რომელსაც ფჩხილებში უნდა გადავცეთ ის ბრძანება ან ფუქნცია
# # რომლის პარალელურად გაშვებაც გვინდა, targetის სახით
#
# thread1.start()
# thread2.start()
# thread3.start()
# # მაშ შემდეგ რაც შევქმნით ამ სრედებს ეს სრედები უნდა დავსტარტოთ, ანნუ უნდა გავუშათ ბრძანება
#
# # ხოლო ბრძანების გაშვების შემდეგ კი უნდა დავაჯოინოთ რათა ერთად მოხდეს ამ რძანების გაშვება
# thread1.join()
# thread2.join()
# thread3.join()
# # არ შეიძლება ერთად დავსტარტოთ და დავაჯოინოთ ბრძანებები, ჯერ უნდა დაისტარტოს ყველა და შემდეგ უნდა დაჯოინდეს
#
# t2 = time.perf_counter()
# print(t2 - t1)

#############################################################################################################################
# def print_task(i):
#     print(f"task {i} started")
#     time.sleep(1)
#     print(f"task {i} finished")
#
# time1 = time.perf_counter()
#
# threads = []
#
# for i in range(1, 11):
#     thread = threading.Thread(target=print_task, args=(i,))
#     # როდესაც ფუქნციას არგუმენტი უნდა გადავცეთ ამისათვის, target საკვანძო სიტყვის შემდეგ
#     # უნდა გავუწეროთ args საკვანძო სიტყვა(არგუმენტები) სადაც უნდა გადავცეთ არგუმნტები, რამდენი არგუმენტიც გადეცემა ფუქნციას იმის მიხედვით
#     thread.start()
#     # როგორც ვიცით სრედები ჯერ უნდა დაისტარტოს და შემდეგ დაჯოინდეს
#     # ამიტომ ცალკეულ for ციკლში ჯერ უნდა დავსტარტოთ
#     # დასაჯოინებლად კი უნდა შევქმნათ ახალი for ციკლი
#
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# time2 = time.perf_counter()
# print(time2 - time1)


# workers in threads
# # შეგვიძია ვმართოთ ის თუკი რამდენი სრედი უნდა გაეშვას ერთდროულად, რათა სრედების გადატვირთვა არ გამოიწვიოს
def print_tasks(i):
    print(f"task {i} started")
    time.sleep(1)
    print(f"task {i} finished")
# უშუალოდ სრედების შექმნას და გაშვებასაც სჭირდება დრო, ამისათვის ვიყენებთ workerებს
# შესაძლოა ყველა სრედის ერთდროულად გაშვებამ უფრო ცუდი შედეგი მოგვცეს ვიდრე
# სრედების ცალ-ცალკე ჯგუფებად გაშვება

# workerებს ვიყენებთ, ოპტიმიზაციისათვის რათა სრედები გავუშვად ჯგუფებად და ნაწილ-ნაწილ


# # ამისათვის ვაიმპორტებთ current.futeresდან ThreadPoolExecutorს
from concurrent.futures import ThreadPoolExecutor
#
# threads = []
#
# time1 = time.perf_counter()
# # # რომელასაც კონტექსტ-მენეჯერის დახმარებით ვქმნით, ფრჩხილებში კი უნდა გადავცეთ ციფრი, რამდენი სრედი უნდა გაეშვას ერთდროულად
# # # max-workes = 0
# with ThreadPoolExecutor(max_workers=3) as executor:
#     for i in range(1, 11):
#         # ხოლო იმ ცვლადს რომელშიც ვქმნით კონტექსტ-მენეჯერს უნდა გადავცეთ ის თასკი, ბრძანება ან ფუქნიცა რომელიც უნდა გაეშვას,
#         # ხოლო ფუნრქციის არგუმენტი კი მძიმის შედეგ უნდა გადავცეთ
#         thread = executor.submit(print_tasks, i)
#         # აქ არ ვიყენებთ target და args საკვანძო სიტყვებს
#         # ცვლადთან ვიძახეთ submit მეთოდს, რომლის დახმარებითაც სრედს ვქმნით executor ცვლადიდან
#         # ცვლადს კი with კონტექსტ მენეჯერის ბოლოში ვქმნით - ისევე როგორც ფაილებთან ვქმნიდით
#         threads.append(thread)
#
# # # განსხვავებით threading მოდულიდან, ამას არ სჭირდება დასტარტვა და დაჯოინება
# time2 = time.perf_counter()
# print(time2 - time1)





# პარალელური პროგრამირება რიგებთან და ხეებთან
# ######################################################################################################################################################################
import queue

import math
from concurrent.futures import ThreadPoolExecutor

# task_queue = queue.Queue()
#
# def worker():
#     while True:
#         task = task_queue.get()
#         if task is None:
#             break
#
#         print(f"processing {task}")
#         time.sleep(1)
#         task_queue.task_done()
#
# num_threads = 5
#
# threads = []
#
# t1 = time.perf_counter()
#
# for i in range(num_threads):
#
#     t = threading.Thread(target=worker)
#     t.start()
#     threads.append(t)
#
#
#
#
# for j in range(1, 11):
#     task_queue.put(j)
#
# for _ in range(num_threads):
#     task_queue.put(None)
#
#
# for thread in threads:
#     thread.join()
#
# t2 = time.perf_counter()
#
# print(f"code took {t2 - t1} seconds")




def new_worker(q):
    while True:
        task = q.get()

        if task is None:
            break

        print(f"start task: {task}")
        time.sleep(1)
        q.task_done()


q = queue.Queue()

t1 = time.perf_counter()
for i in range(1, 11):
    q.put(i)


with ThreadPoolExecutor(max_workers=3) as executor:
    for _ in range(3):
        executor.submit(new_worker, q)

    for i in range(3):
        q.put(None)


t2 = time.perf_counter()

print(f"All tasks completed in {t2 - t1} seconds")

















