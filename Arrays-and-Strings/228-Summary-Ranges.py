# https://leetcode.com/problems/summary-ranges/submissions/1374505423

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        seq = []
        output = []
        if len(nums) == 0: return []
        for i in range(len(nums)):
            if len(seq) == 0:
                seq = [nums[i]]
            elif nums[i] == nums[i-1] + 1:
                seq.append(nums[i])
            else:
                handleOutput(output, seq)
                seq = [nums[i]]
        handleOutput(output, seq)
        return output

def handleOutput(output: [str], seq: [int]):
    if len(seq) == 1:
        output.append(str(seq[0]))
    else:
        output.append(str(seq[0]) + '->' + str(seq[-1]))