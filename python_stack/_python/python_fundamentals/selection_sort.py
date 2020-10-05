def sort(some_list):
    for i in range(len(some_list)):
        min_index = i
        for j in range(i+1, len(some_list)):
            if some_list[j] < some_list[min_index]:
                min_index = j
        some_list[i] , some_list[min_index] = some_list[min_index] , some_list[i]
    return some_list
x = sort([6,12,90,37,1,2])
print(x)