class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        pref_sum=0
        max_len=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
            pref_sum+=nums[i]
            if pref_sum in d:
                max_len=max(max_len,i-d[pref_sum])
            if pref_sum not in d:
                d[pref_sum]=i
        return max_len