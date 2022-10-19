def sort(arr):
    value = 'sorted'
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            pass
        else:
            value = 'Not sorted'
            break
    return value

a = [1,2,9,4,5,6,7]

b = sort(a)
if b == 'sorted':
    print("Sorted")
else:
    print("Notsorted")