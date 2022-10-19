a = [2, 4, 6, 1, 9, 3, 7, 5, 8, 0]


def selection(arr):
    print(a)
    lenth = len(a)

    for i in range(lenth):
        
        min_num_ind = arr[i]

        for j in range(i, len(arr)):

            if arr[j] < arr[min_num_ind]:
                min_num_ind = j

        arr[i], arr[min_num_ind] = arr[min_num_ind], arr[i]
        
    #print(a)
    return arr
    

new_arr = selection(a)

print(new_arr)