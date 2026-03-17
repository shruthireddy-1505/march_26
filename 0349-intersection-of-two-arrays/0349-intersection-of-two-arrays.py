class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        res=[]
        while i<n and j<m:
            while i>0 and i<n and nums1[i]==nums1[i-1]:
                i+=1
            while j>0 and j<m and nums2[j]==nums2[j-1]:
                j+=1
            if i>=n or j>=m:
                break
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res