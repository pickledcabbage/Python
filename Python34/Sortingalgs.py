# Sorting algorithms

from random import randrange
import time
def create_array(ran:int,length:int)->list:
    '''Generates list of size 'length' and filled with numbers 1->ran'''
    temp = []
    for i in range(length):
        temp.append(randrange(1,ran))
    return temp

def check_sorted(arr:list)->bool:
    '''Checks if list 'arr' is sorted'''
    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:
            return False
    return True

def print_array(l:list)->None:
    '''Prints a list'''
    for i in range(len(l)):
        print('{0:7}'.format(l[i]),end='')
        if (i+1)%10==0:
            print()
    print('\n\n')

def insertion_sort(start:list)->list:
    for i in range(1,len(start)):
        temp = i
        hold = start[temp]
        while hold<start[temp-1] and temp>0:
            start[temp]=start[temp-1]
            temp-=1
        start[temp]=hold
    return start

def insertion_sort2(start:list,inc:int)->list:
    for i in range(inc,len(start),inc):
        temp = i
        hold = start[temp]
        while hold<start[temp-inc] and temp>inc-1:
            start[temp]=start[temp-inc]
            temp-=inc
        start[temp]=hold
    return start

def insertion_sort3(start:list,inc:int,begin:int)->list:
    for i in range(begin,len(start),inc):
        temp = i
        hold = start[temp]
        while hold<start[temp-inc] and temp>inc-1:
            start[temp]=start[temp-inc]
            temp-=inc
        start[temp]=hold
    return start
def shellsort(arr:list,l:list,b:bool)->list:
    '''Sorts list "arr" with increments given in list "l", if 'b' is true then execution time is printed'''
    start_time = time.time()
    for i in l:
        arr = insertion_sort2(arr,i)
    if b:
        print("--- %s seconds ---" % (time.time() - start_time))
    print(check_sorted(arr))
    return arr
def shellsort2(arr:list,l:list,b:bool)->list:
    '''Sorts list "arr" with increments given in list "l", if 'b' is true then execution time is printed'''
    start_time = time.time()
    for i in l:
        for count in range(0,i):
            arr = insertion_sort3(arr,i,count)
    if b:
        print("--- %s seconds ---" % (time.time() - start_time))
    print(check_sorted(arr))
    return arr
def shellsort3(arr:list,l:list,b:bool)->list:
    '''Sorts list "arr" with increments given in list "l", if 'b' is true then execution time is printed'''
    k = len(arr)
    start_time = time.time()
    for i in l:
        for count in range(0,i):
            for i2 in range(count,k,i):
                temp = i2
                hold = arr[temp]
                while hold<arr[temp-i] and temp>i-1:
                    arr[temp]=arr[temp-i]
                    temp-=i
            arr[temp]=hold
    
    print("--- %s seconds ---" % (time.time() - start_time))
    print(check_sorted(arr))
    return arr
def next_inc(main:list,l:list,inc:int,end:int,incs:int)->list:
    if inc == incs:
        return main
    for i in range(l[inc-1]+1,end-(incs-inc)):
        main.append(next_inc(main,(l+[i]),inc+1,end,incs))
    return main

def generate_possibilities(end:int,incs:int)->list:
    start = 1
    temp = []
    for i in range(start,end):
        temp.append(next_inc(temp,[1],1,end,incs))
    return temp

#print(generate_possibilities(40,3))
arr = create_array(1000000,10000)
increments = [
1750,701,301,132,57,23,10,4,1]
arr = shellsort2(arr,increments,True)


arr2 = create_array(1000000,1000000)
start_time = time.time()
arr2.sort()
print("--- %s seconds ---" % (time.time() - start_time))
print(check_sorted(arr))
