#Biggie Size
def biggie(list):
    for i in range (0,len(list),1):
        if list[i] > 0:
            list[i] = "big"
    return list
x = biggie([1,0,3,])
print(x)

#Count Positives
def cp(list):
    count = 0
    for i in range (len(list)):
       if list[i] > 0:
           count = count + 1
    list[len(list)-1] = count
    return list
x = cp([1,2,10,10,10])
print(x)

#Sum Total
def total(list):
    sum = 0
    for i in range (len(list)):
        sum = sum + list[i]
    return sum
x = total([17,6,3,4])
print(x)

#Average
def average(list):
    avg = 0
    for i in range (len(list)):
        avg= list[i] + avg
    avg = avg / len(list)
    return avg
x = average([3,7,4,12])
print(x)

#Length
def length(list):
    return len(list)
x = length([5,4,3])
print(x)

#Minimum
def max(list):
    big = 0
    for i in range(len(list)):
        if list[i] > big:
            big = list[i]
    return big
x = max([5,4,45,100])
print(x)

#Minimum
def min(list):
    small = list[0]
    for i in range(len(list)):
        if list[i] < small:
            small = list[i]
    return small
x = min([5,4,45,100])
print(x)

#Ultimate Analysis
def ult(list):
    new_dict = {}
    sum = 0
    average = 0
    min = list[0]
    max = list[0]
    length = len(list)
    for i in range (len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
        sum = sum + list[i]
    average = sum / length
    new_dict['sum'] = sum
    new_dict['average'] = average
    new_dict['min'] = min
    new_dict['max'] = max
    new_dict['length'] = length
    return new_dict
x = ult([100,25,300,-1])
print(x)

#Reverse List
def reverse(list):
    import math
    holder = 0
    holder2 = 0
    count = 1
    alt_count = len(list) / 2
    math.floor(alt_count)
    for i in range (0, int(alt_count), 1):
        holder = list[i]
        holder2 = list[len(list)-count]
        list[len(list)-count] = holder
        list[i] = holder2
        count = count + 1
    return list
x = reverse([1,2,3,4,5,6,7,8,9])
print(x)

