import sys
a = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


def recursive(arr):
    print("TODO REC")
    def bin_search(arr, low, high, x):

        if high >= low:
            mid = (high + low) // 2
            print("mid = ", mid)

            if x == arr[mid]:
                print("Found in index", mid)
                return mid
            elif x > arr[mid]:
                bin_search(arr, mid+1, high, x)
            elif x < arr[mid]:
                bin_search(arr, low, mid+1, x)


        else:
            print("Not Found")
            return -1

    bin_search(a, 0, len(a)-1, 1)
    
        
    


def iterative(arr):
    print("TODO ITE")

    def bin_search(arr, low, high, x):
        
        while (low <= high):

            mid = (high+low) // 2
            print("Mid = ", mid)

            if x == arr[mid]:
                print("Found in index: ", mid)
                return mid
            elif x > arr[mid]:
                low = mid+1
            elif x < arr[mid]:
                high = mid + 1

        print("Not Found")

    bin_search(a, 0, len(a)-1, 14)


recursive(a)

iterative(a)