# https://leetcode.com/problems/is-subsequence/submissions/1373697987

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s): return False
        if s == '': return True
        i = 0

        for c in t:
            if s[i] == c: 
                i += 1
            if i == len(s): 
                return True
        return False