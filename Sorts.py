import random
import time

def generateRandomArray(start = 0, end = 1000, num = 25):
    ret = []
    for i in range(num):
        ret.append(random.randint(start, end))
    return ret

def isSorted(sortedArray):
    temp = sortedArray.copy()
    temp.sort()
    if sortedArray == temp:
        return True

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def insertionSort(arr):
    ret = arr.copy()
    i = 1
    while i < len(ret):
        j = i
        while j > 0 and ret[j - 1] > ret[j]:
            swap(ret, j, j - 1)
            j -= 1
        i += 1
    return ret

def mergeSort(arr):
    ret = arr.copy()
    mergeSortRecur(ret)
    return ret

def mergeSortRecur(arr):
    if len(arr) == 1:
        return
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSortRecur(L)
    mergeSortRecur(R)
    merge(arr, L, R)

def merge(arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def quickSort(arr):
    ret = arr.copy()
    quickSortRecur(ret, 0, len(arr) - 1)
    return ret

def quickSortRecur(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSortRecur(arr, low, pi -1)
        quickSortRecur(arr, pi + 1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i + 1],arr[high] = arr[high],arr[i + 1]
    return i + 1

def plotSort(sortMethods, methodNames):
    for i in range(len(sortMethods)):
        if i > 0:
            print()
        sortMethod = sortMethods[i]
        methodName = methodNames[i]
        sizes = [10, 25, 50, 100, 1000]
        for size in sizes:
            unsortedArray = generateRandomArray(num = size)
            startTime = time.time()
            sortedArray = sortMethod(unsortedArray)
            endTime = time.time()
            if isSorted(sortedArray):
                print( str(methodName) + " for " + str(size) + " elements takes \t" + str(endTime - startTime))
            else:
                print("There is a bug in " + str(methodName) )

def binarySearch(arr, val):
    return binarySearchRecur(arr, 0, len(arr), val)
def binarySearchRecur(arr, start, end, val):
    if end <= 0:
        return -1
    mid = (end - start)//2
    if val == arr[mid]:
        return mid
    elif val > arr[mid]:
        return binarySearchRecur(arr, mid - 1, end, val)
    else:
        return binarySearchRecur(arr, start, mid + 1, val)


plotSort([insertionSort, mergeSort, quickSort], ["Insertion Sort", "Merge Sort", "Quick Sort"])
