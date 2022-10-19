import sys
a = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

def recursive(arr):
    def bin_search(arr, start, end, x):
        if end >= start:
            mid = (end + start) // 2

            if x == arr[mid]:
                print("Found in index", mid)
                return
            elif x > arr[mid]:
                bin_search(arr, mid+1, end, x)
            elif x < arr[mid]:
                bin_search(arr, start, mid-1, x)
        else:
            print("Not Found")
            return -1
    for i in a:
        print(f"{i} Is ", end="")
        bin_search(a, 0, len(a)-1, i)

def iterative(arr):

    def bin_search(arr, start, end, x):
        
        while (start <= end):

            mid = (end+start) // 2

            if x == arr[mid]:
                print("Found in index",mid)
                return mid
            elif x > arr[mid]:
                start = mid + 1
            elif x < arr[mid]:
                end = mid - 1

        print("Not Found")

    for i in a:
        print(f"{i} Is ", end="")
        bin_search(a, 0, len(a)-1, i)



recursive(a)
for i in range(3):
    print("")
iterative(a)