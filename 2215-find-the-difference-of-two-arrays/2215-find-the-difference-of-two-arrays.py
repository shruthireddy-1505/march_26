class Solution:
    def findDifference(self, n1: List[int], n2: List[int]) -> List[List[int]]:
        
        n=set(n1)
        m=set(n2)

        return [list(n-m),list(m-n)]
        