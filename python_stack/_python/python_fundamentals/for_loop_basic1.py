# Basic
for x in range(0,151):
    print(x)

# Multiples of Five
for x in range(5,1001):
    if x % 5 == 0:
        print(x)

# Counting the Dojo Way
for x in range(0,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else: print(x)

# Whoa.  That Sucker's Huge
sum = 0
for x in range(0,500001):
    if x % 2 != 0:
        sum = sum + x
print(sum)

# Countdown by fours
for x in range(2018,0,-4):
    print(x)

# Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)