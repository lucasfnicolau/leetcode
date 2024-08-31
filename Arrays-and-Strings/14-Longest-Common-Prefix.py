# https://leetcode.com/problems/longest-common-prefix/submissions/1374356035

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstStr = strs[0]
        prefix = ''
        
        for i in range(len(firstStr)):
            hasPrefix = True
            for s in strs[1:]:
                if i >= len(s):
                    return prefix
                elif s[i] != firstStr[i]:
                    return prefix
            if hasPrefix:
                prefix += firstStr[i]

        return prefix