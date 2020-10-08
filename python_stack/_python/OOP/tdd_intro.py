import math
import unittest

def reverse(L):
    temp = 0
    reverse = 1
    for i in range(0, int(math.floor(len(L)/2)), 1):
        temp = L[i]
        L[i] = L[len(L)-reverse]
        L[len(L)-reverse] = temp
        reverse += 1
    return L
x = reverse([1,2,3,4,5,6,7,8,9,10])
print(x)

class reverseTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverse([1,3,5]), [5,3,1])
        self.assertEqual(reverse([1,2,3,4,5,6,7,8,9,10]), [10,9,8,7,6,5,4,3,2,1])

    def setUp(self):
        print("Running setUp!")

    def tearDown(self):
        print("Running tearDown Tasks!")

if __name__ == '__main__':
    unittest.main()