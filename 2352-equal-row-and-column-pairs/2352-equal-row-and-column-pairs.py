class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = []
        count = 0
        n = len(grid)
        for i in range(n):
            ans=[]
            for j in range(n):
                ans.append(grid[j][i])
            transpose.append(ans)
        for i in range(n):
            for j in range(n):
                l=0
                for k in range(n):
                    if grid[i][k]!=transpose[j][k]:
                        break
                    else:
                        l+=1
                        if l==n:
                            count+=1
        return count