import unittest
import random

# Input: 4, 14, 2
# 
# Output: 6
#
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0

        maxnum = max(nums)
        bits_cnt = [[0, 0] for _ in range(32)]
        for num in nums:
        	for ib in range(len(bits_cnt)):
        		mask = 1 << ib
        		if mask > maxnum: # optimization for case of many small numbers
        			break
        		b = (num & mask) >> ib
        		bits_cnt[ib][b] += 1

        total = 0
        for n0, n1 in bits_cnt:
        	total += n0 * n1

        return total


class Test(unittest.TestCase):
	def brute_force(self, nums):
		def count_bits(x):
			res = 0
			while x:
				x &= (x-1)
				res += 1
			return res

		total = 0
		for i in range(len(nums)-1):
			for j in range(i, len(nums)):
				diff = nums[i] ^ nums[j]
				total += count_bits(diff)

		return total

	def solution(self, arr):
		return Solution().totalHammingDistance(arr)

	def check(self, arr):
		answer = self.solution(arr)
		correct = self.brute_force(arr)
		self.assertEqual(answer, correct)

	def test_simple(self):
		self.check([2, 14, 4])
		self.check([1, 3, 2, 0])

		self.assertEqual(self.solution([]), 0)
		self.assertEqual(self.solution([0]), 0)
		self.assertEqual(self.solution([128921]*10), 0)

	def test_random(self):
		size = random.randint(20, 50)
		arr = [random.randint(0, 10**9) for _ in range(size)]
		self.check(arr)


unittest.main()