def binarySearch(arr, item, beg, end):
    while beg <= end:
        mid = beg + (end - beg)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            beg = mid + 1
        else:
            end = mid - 1
    return -1

arr = [13, 45, 65, 16, 117, 82, 19]
item = int(input("the the element to serach in array : "))

ans = binarySearch(arr, item, 0, len(arr)-1)

if ans != -1:
    print("The Element " + str(item) + " is present")
else:
    print("The Element " + str(item) +" not present")