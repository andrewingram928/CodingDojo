#Coundtdown
def countdown(a):
    list= []
    for i in range (a, -1, -1):
        list.append(i)
    return list
x = countdown(10)
print(x)

#Print and Return
def print_return(a,b):
    print(a)
    return b
x = print_return(5,10)
print(x)

#First Plus Length
def fpl(a):
    x = len(a) + a[0]
    print(x)
z = fpl([1,2,3,4,5])

#Values Greater Than Second
def gts(a):
    new_list = []
    count = 0
    for i in range (0,len(a),1):
        if a[i] > a[1]:
            new_list.append(a[i])
            count = count + 1
    print(count)
    if count < 2:
        return False
    else:
        return new_list
x = gts([3,2,0,1])
print(x)

#This Length, That Value
def lv(size, value):
    new_list = []
    for i in range (size):
        new_list.append(value)
    return new_list
x = lv(5,4)
print(x)