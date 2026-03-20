class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        pref_sum=0
        count=0
        for i in nums:
            pref_sum+=i
            if pref_sum%k in d:
                count+=d[pref_sum%k]
            if pref_sum%k in d:
                d[pref_sum%k]+=1
            else:
                d[pref_sum%k]=1
        return count        