#################################################################################
#  Name:         Burak Karataş
#  Student ID:   64200045
#  Department:   Computer Engineering
#  Assignment ID: A1
##################################################################################
# Sorting Questions
# Question I
# Question II
# Question III
###################################################################################
import random
import time
print("\n")
print("SOLUTION OF QUESTION I, II, III:")
print("********************************************************************************")

fileSizes = [1000, 5000, 10000, 25000, 50000, 100000, 200000]

def fillFile(fileSize, fileName):

    lst = [i for i in range(0, fileSize)]
    for k in range(0, int(len(lst) / 10)):
        i = random.randrange(0, len(lst))
        j = random.randrange(0, len(lst))
        lst[i], lst[j] = lst[j], lst[i]

    with open(str(fileName), 'w') as file:
        file.write(','.join(str(number) for number in lst))

stats = []
for i in fileSizes:
    start = time.time()
    fillFile(i, "file" + str(i))
    finish = time.time()
    runtime = finish - start
    stats.append(runtime)

print(stats)

def readFile(fileName):
    list_read = []
    with open(str(fileName), "r") as f:
        content = f.readlines()
    # print(content)
    for i in content:
        list_read.append(i)
    list_read = list_read[0].split(",")
    list_read = [int(nmb) for nmb in list_read]
    return list_read

ReadStats = []
for i in fileSizes:
    start = time.time()
    readFile("file" + str(i))
    finish = time.time()
    runtime = finish - start
    ReadStats.append(runtime)

print(ReadStats)

with open("fileStats.txt", "w") as f:
    f.write("fillFile " + ",".join(str(a) for a in stats) + "\n")
    f.write("readFile " + ",".join(str(b) for b in ReadStats))


def bubbleSort(arr):
	n = len(arr)

	for i in range(n-1):

		for j in range(0, n-i-1):

			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(L):

    for i in range(len(L)-1):
        min_index = i
        for j in range(i+1, len(L)-1):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]


def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def shellSort(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap /= 2


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]

	for j in range(low, high):

		if arr[j] <= pivot:

			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		pi = partition(arr, low, high)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)


timebuble = []
for i in fileSizes:
    start = time.time()
    name = "file"+str(i)
    sortList = readFile(name)
    bubbleSort(sortList)
    finish = time.time()
    timebuble.append(int(finish-start))

timeselect = []
for i in fileSizes:
    start = time.time()
    name = "file" + str(i)
    sortList = readFile(name)
    selection_sort(sortList)
    finish = time.time()
    timeselect.append(int(finish - start))

timeinsert = []
for i in fileSizes:
    start = time.time()
    name = "file" + str(i)
    sortList = readFile(name)
    insertionSort(sortList)
    finish = time.time()
    timeinsert.append(int(finish - start))

timeshell = []
for i in fileSizes:
    start = time.time()
    name = "file" + str(i)
    sortList = readFile(name)
    shellSort(sortList)
    finish = time.time()
    timeshell.append(int(finish - start))

timemerge = []
for i in fileSizes:
    start = time.time()
    name = "file" + str(i)
    sortList = readFile(name)
    mergeSort(sortList)
    finish = time.time()
    timemerge.append(int(finish - start))

timequick = []
for i in fileSizes:
    start = time.time()
    name = "file" + str(i)
    sortList = readFile(name)
    quickSort(sortList,0,len(sortList)-1)
    finish = time.time()
    timequick.append(int(finish - start))

timeheap = []
for i in fileSizes:
    start = time.time()
    name = "file" + str(i)
    sortList = readFile(name)
    heapSort(sortList)
    finish = time.time()
    timeheap.append(int(finish - start))

with open(str("sortStats.txt"), 'w') as f:
    f.write("Bubble_Sort " + ",".join(str(x) for x in timebuble) + "\n")
    f.write("Selection_Sort " + ",".join(str(x) for x in timeselect) + "\n")
    f.write("Insertion_Sort " + ",".join(str(x) for x in timeinsert) + "\n")
    f.write("Shell_Sort " + ",".join(str(x) for x in timeshell) + "\n")
    f.write("Merge_Sort " + ",".join(str(x) for x in timemerge) + "\n")
    f.write("Quick_Sort " + ",".join(str(x) for x in timequick) + "\n")
    f.write("Heap_Sort " + ",".join(str(x) for x in timeheap) + "\n")


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1


class HashTable():
    def __init__(self):
        self.size = 1100017
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

srt = readFile("file100000")
heapSort(srt)
start = time.time()
for i in range(1000):
    a = random.randint(0, 100000)
    sequentialSearch(srt, a)
finish = time.time()
timelinear = finish - start

srt = readFile("file100000")
heapSort(srt)
start = time.time()
for i in range(1000):
    a = random.randint(0, 100000)
    binarySearch(srt, a)
finish = time.time()
timeBinary = finish - start

srt = readFile("file100000")
heapSort(srt)
H = HashTable()
start = time.time()
for key in srt:
    H[key] = "Data" + str(key)
for i in range(1000):
    a = random.randint(0,100000)
    H[a]
finish = time.time()
timehash = finish-start

with open(str("searchStats.txt"), 'w') as file:
    file.write("Linear_Search" + str(timelinear) + "\n")
    file.write("Binary_Search" + str(timeBinary) + "\n")
    file.write("Hashing" + str(timehash) + "\n")

##################################################################################
# Question IV: By using nested loops, write the code of this triangularshape.
###################################################################################
print("\n")
print("SOLUTION OF QUESTION IV:")
print("********************************************************************************")
print("\n")
def exponential_triangle(n) :
    for i in range(n) :

        for j in range(n-1-i) :
            print(" ", end = " ")

        for j in range(i+1) :
            print(2**j, end = " ")

        for j in range(i-1, -1, -1) :
            print(2**j, end = " ")
        print(" ")

exponential_triangle(9)

########################################################################################################################################################
# Question V: You will have an orthogonal triangle input from a file and you need to find the maximum sum of the numbers according to given rules below;
# 1. You will start from thetop and move downwards to an adjacent number as in below.
# 2. You are only allowed to walk downwards and diagonally.
# 3. You can only walk over NON PRIME NUMBERS.
# 4. You have to reach at the end of the pyramid as much as possible.
# 5. You have to treat the input as pyramid.
########################################################################################################################################################
print("\n")
print("SOLUTION OF QUESTION V:")
print("********************************************************************************")
print("\n")
def primeCheckingfunction(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    else:
        return True

with open("number triangle.txt", "r") as f:
    lst = []
    for i in range(15):
        b = f.readline()
        lst.append(b.strip())
    lst1 = []
    for i in lst:
        b = [int(j) for j in i.split()]
        lst1.append(b)
a = 0
trianglenumber = []
for i in range(len(lst1)):
    tmptrngle = []
    if a>0:
        tmptrngle.append(lst1[i][a])
        tmptrngle.append(lst1[i][a-1])
        tmptrngle.append(lst1[i][a+1])
    else:
        tmptrngle.append(lst1[i][a])
        if len(lst1[i]) > 1:
            tmptrngle.append(lst1[i][a+1])
    tmp2tri = sorted(tmptrngle)
    if not primeCheckingfunction(tmp2tri[-1]):
        trianglenumber.append(tmp2tri[-1])
    elif not primeCheckingfunction(tmp2tri[-2]):
        trianglenumber.append(tmp2tri[-2])
    else:
        trianglenumber.append(tmp2tri[-3])
    a = lst1[i].index(trianglenumber[i])

print(trianglenumber)
print(sum(trianglenumber))
########################################################################################################################################################



