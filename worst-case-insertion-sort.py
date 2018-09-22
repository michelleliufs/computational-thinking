


import time


def create_data(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key
        

worst_list = list(range(1,10))
worst_list.sort(reverse=True)
start = time.time()
create_data(worst_list)
sum = 0
worst_time = sum + ( time.time() - start )
print(worst_time)





def create_data(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key
        

worst_list = list(range(1,100))
worst_list.sort(reverse=True)
start = time.time()
create_data(worst_list)
sum = 0
worst_time = sum + ( time.time() - start )
print(worst_time)




def create_data(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key
        

worst_list = list(range(1,1000))
worst_list.sort(reverse=True)
start = time.time()
create_data(worst_list)
sum = 0
worst_time = sum + ( time.time() - start )
print(worst_time)


def create_data(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key
        

worst_list = list(range(1,10000))
worst_list.sort(reverse=True)
start = time.time()
create_data(worst_list)
sum = 0
worst_time = sum + ( time.time() - start )
print(worst_time)

