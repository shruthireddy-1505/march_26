class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
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
        """
        n = len(grid)
        d={}
        for i in grid:
            tr = tuple(i)
            if tr in d:
                d[tr]+=1
            else:
                d[tr] = 1

        count=0
        for i in range(n):
            col=[]
            for j in range(n):
                col.append(grid[j][i])

            tc = tuple(col)      

            if tc in d:
                count+=d[tc]
        return count