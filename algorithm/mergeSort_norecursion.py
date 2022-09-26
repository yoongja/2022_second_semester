def seq_mere_sort(arr):
    right = 0; wid = 0; rend = 0; left = 0
    k = 1

    num = len(arr)
    temp = [0] * num

    while(k < num):
        left = 0
        while(left + k < num):
            right = left + k
            rend = right + k
            if(rend > num):
                rend = num
            m = left; i = left; j = right

            while(i < right and j < rend):
                if (arr[i] <= arr[j]):
                    temp[m] = arr[i]
                    i += 1
                else:
                    temp[m] = arr[j]
                    j += 1
                m += 1

            while(i < right):
                temp[m] = arr[i]
                i += 1; m += 1
            while(j < rend):
                temp[m] = arr[j]
                j += 1; m += 1
            m = left
            while(m < rend):
                arr[m] = temp[m]
                m += 1
            left += k * 2
        k *= 2
    return arr
arr = [3, 5, 2, 9, 10, 14, 4, 8]
arr = seq_mere_sort(arr)
print(arr)