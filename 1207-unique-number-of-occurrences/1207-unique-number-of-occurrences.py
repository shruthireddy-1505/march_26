class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}

        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=[]
        for i in d:
            ans.append(d[i])
        if len(set(arr))==len(set(ans)):
            return True
        else:
            return False
