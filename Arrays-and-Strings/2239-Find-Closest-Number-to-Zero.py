import sys

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        negative = sys.maxsize * -1
        positive = sys.maxsize
        for n in nums:
            if n < 0 and (negative == 0 or n > negative):
                negative = n
            elif n > 0 and (positive == 0 or n < positive):
                positive = n
            elif n == 0: return n
        
        return positive if abs(negative) >= abs(positive) else negative
