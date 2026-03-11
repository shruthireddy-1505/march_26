class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        temp=[]
        found=False
        if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                temp.append(i)
        for i in temp:
            dup=haystack[i:i+n]
            if dup == needle:
                found=True
                return i
            
        if found==False:
            return -1