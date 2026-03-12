class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res=""
        l=len(strs)
        n=len(strs[0])
        for i in range(n):

            if strs[0][i]!=strs[l-1][i]:
                break
            else:
                res+=strs[0][i]
        return res
                