import unittest

class TopCounter:
   def __init__(self, capacity):
       self.capacity = capacity
       self.arr = [] # hold pairs of {value, cnt}

   def add(self, x):
       for i in range(len(self.arr)):
           if self.arr[i][0] == x:
               self.arr[i][1] += 1
               return
       
       if len(self.arr) < self.capacity:
           self.arr.append([x, 1])
       else:
           place=0
           for i in range(1, len(self.arr)):
               if self.arr[i][1] < self.arr[place][1]:
                   place = i
                   
           self.arr[place] = [x, 1]
           
   def get(self):
       return self.arr

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tc = TopCounter(3)
        for x in nums:
            tc.add(x)
        
        top_elems = dict()
        for x,n in tc.get():
            top_elems[x] = 0

        # do second scan to count top elements
        for x in nums:
            if x in top_elems:
                top_elems[x] += 1

        res = []
        for x, n in top_elems.items():
            if n > len(nums) // 3:
                res.append(x)

        return res


class Test(unittest.TestCase):
    @staticmethod
    def s(arr):
        return sorted(Solution().majorityElement(arr))

    def test_simple(self):
        self.assertEqual(self.s([1,1,2,3,3,1]), [1])
        self.assertEqual(self.s([1,1,1,2,3,4,5,6]), [1])
        self.assertEqual(self.s([2,3,4,5,6,1,1,1]), [1])
        self.assertEqual(self.s([1,2,3,1,3,4,5,1]), [1])
        self.assertEqual(self.s([1,1,2,2,3,3,4,1]), [1])

    def test_hard(self):
        self.assertEqual(self.s([1,2,2,3,2,1,1,3]), [1, 2])
        self.assertEqual(self.s([1,2,2,3,4,4,1,1]), [1])
    
    def test_two(self):
        self.assertEqual(self.s([1,1,1,2,2,2]), [1, 2])
        self.assertEqual(self.s([1,2,1,2,1,2]), [1, 2])

    def test_none(self):
        self.assertEqual(self.s([]), [])
        self.assertEqual(self.s([1,2,3]), [])
        self.assertEqual(self.s([1,2,3,4,5,6]), [])
        self.assertEqual(self.s([1,1,1,2,2,2,3,3,3]), [])
    
    def test_single(self):
        self.assertEqual(self.s([0]), [0])
        self.assertEqual(self.s([1000]), [1000])
        self.assertEqual(self.s([-1]), [-1])

unittest.main()
