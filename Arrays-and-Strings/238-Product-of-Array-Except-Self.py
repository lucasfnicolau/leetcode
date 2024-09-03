# To be improved
# https://leetcode.com/problems/product-of-array-except-self/submissions/1377159725

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        zeros = []
        product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros.append(i)
            
        for i in range(len(nums)):
            if nums[i] == 0:
                answer.append(product if len(zeros) == 1 else 0)
            else:
                answer.append(0 if len(zeros) > 0 else int(product * 1/nums[i]))
        
        return answer
