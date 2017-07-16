array = [2,3,8,7,1,2,2,2,7,3,9,8,2,1,4,2,4,6,9,2]

def BubbleSort(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

def InsertionSort(array):
    for i in range(len(array) - 1):
        j = i + 1
        while j > 0:
            if(array[j - 1] > array[j]):
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
            j-=1
    return array

def Partition(array, left, right):
    pivot = right
    i = left
    for j in range(left, right):
        if array[j] < array[pivot]:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i +=1

    temp = array[pivot]
    array[pivot] = array[i]
    array[i] = temp
    return i



def QuickSort(array, left, right):
    if left < right:
        p = Partition(array, left, right)
        QuickSort(array, left, p-1)
        QuickSort(array, p+1, right)


def CountingSort(array):
    dict = {}
    for item in array:
        if item in dict:
            dict[item] +=1
        else:
            dict[item] = 1
    print dict
CountingSort(array)