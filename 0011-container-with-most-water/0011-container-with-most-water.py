class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        max_ans=float('-inf')
        while i<j:
            area=(j-i)*min(height[i],height[j])
            max_ans=max(max_ans,area)
            
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_ans
            
        
    
        