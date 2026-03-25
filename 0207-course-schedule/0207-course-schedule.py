class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        adj = []
        q = []
        ans = []
        for i in range(n):
            adj.append([])

        for k,m in p:
            adj[k].append(m)
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
                ind[nd]-=1
                if ind[nd] == 0:
                    q.append(nd)
        if len(ans) == n:
            return True
        else:
            return False
