class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        count=0
        while i<j:
            sum_x=nums[i]+nums[j]
            if sum_x==k:
                count+=1
                i+=1
                j-=1
            elif sum_x<k:
                i+=1
            else:
                j-=1
        return count

        