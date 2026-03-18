class Solution:
    def largestAltitude(self, nums: List[int]) -> int:
        n=len(nums)
        pref=[0]*(n+1)
        pref[0]=0
        pref[1]=0+nums[0]
        for i in range(1,n):
            pref[i+1]=pref[i]+nums[i]
        return max(pref)
            