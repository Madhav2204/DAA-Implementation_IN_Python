def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(a, start, end):
    pivot = a[end]
    pIndex = start
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1

    swap(a, end, pIndex)
    return pIndex

def quicksort(a, start, end):
    # base condition
    if start >= end:
        return
    pivot = partition(a, start, end)
    quicksort(a, start, pivot - 1)
    quicksort(a, pivot + 1, end)
 
if __name__ == '__main__':
    n = int(input("Enter the number of element to be sorted : "))
    unsorted_list = []
    for i in range(n):
        ele = int(input(f"Enter element {i+1} : "))
        unsorted_list.append(ele)
    quicksort(unsorted_list, 0, len(unsorted_list) - 1)
    # print the sorted list
    print(f"sorted_list is {unsorted_list}")