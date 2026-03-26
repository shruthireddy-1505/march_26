class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        d = {}
        n_s = s+t
        for i in n_s:
            if i not in d:
                d[i]=1
            else:
                d[i] += 1
        for k,v in d.items():
            if v==1:
                return k
        """
        arr = [0]*26
        for i in s:
            ind = ord(i) - ord("a")
            arr[ind]+=1
        for i in t:
            ind = ord(i) - ord("a")
            arr[ind] -= 1
        for i in range(len(arr)):
            if arr[i]== -1:
                return chr(ord("a")+i)

        