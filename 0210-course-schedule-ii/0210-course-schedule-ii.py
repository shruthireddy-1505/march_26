class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        adj = []
        q = []
        ans = [] 
        for i in range(n):
            adj.append([])
        
        for i,j in p:
            adj[j].append(i)
        ind = [0]*n
        for i in range(n):
            for j in adj[i]:
                ind[j] += 1
        
        for i in range(n):
            if ind[i] == 0:
                q.append(i)
        while q:
            node = q.pop(0)
            ans.append(node)
            for nd in adj[node]:
                ind[nd] -= 1
                if ind[nd] == 0:
                    q.append(nd)
        if len(ans)!=n:
            return []
        return ans
        

        