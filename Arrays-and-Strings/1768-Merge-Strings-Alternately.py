class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        biggerWord = word1 if len(word1) >= len(word2) else word2
        smallerWord = word2 if biggerWord == word1 else word1
        mergedStr = ''

        for i in range(len(biggerWord)):
            if i >= len(word1) or i >= len(word2):
                mergedStr += biggerWord[i:]
                break
            if i < len(word1):
                mergedStr += word1[i]
            if i < len(word2):
                mergedStr += word2[i]
        
        return mergedStr
