def bubble(arr):

    for i in range(len(arr)-1):
        #print(arr)
        check = 0

        for j in range(len(arr)-1):
            print(arr)
            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                check+=1
                #print(check)

        print(check)
        if check == len(arr)-1:
            return arr

    return arr

array = [1,2,3,4,5]

#array = [5,2,4,3]
arr = bubble(array)

print()
print(arr)
