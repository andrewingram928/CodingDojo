import random
def randInt(min= 0, max= 100):
    if min == 0 and max == 100:
        num = random.random() * max
        return num
    elif min == 0:
        num = random.random() * max
        return num
    elif max == 100:
        num = random.random() * (max-min) + min
        return num
    elif min > 0 and max > 0:
        if min > max:
            num = random.random() * (min - max) + max
            return num
        else:
            num = random.random() * (max-min) + min
            return num
x = randInt(min=500, max=50)
print(x)

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

