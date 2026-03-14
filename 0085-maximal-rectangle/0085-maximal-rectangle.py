class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        pref=[[0]*m for i in range(n)]
        for i in range(m):
            
            pref[0][i]=int(matrix[0][i])

            
            for j in range(1,n):
                if int(matrix[j][i])!=0:
                    pref[j][i]=pref[j-1][i]+int(matrix[j][i])
        ans=0
        for i in range(n):
            ans=max(ans,self.hist(pref[i]))
        return ans
    def hist(self,val):
        max_h=0
        n=len(val)
        nxt=[]
        st=[]
        for i in range(n-1,-1,-1):
            while st and val[st[-1]]>=val[i]:
                st.pop()
            if len(st)==0:
                nxt.append(n)
            else:
                nxt.append(st[-1])
            st.append(i)
        nxt=nxt[::-1]
        
        prev=[]
        st1=[]
        for i in range(n):
            while st1 and val[st1[-1]]>=val[i]:
                st1.pop()
            if len(st1)==0:
                prev.append(-1)
            else:
                prev.append(st1[-1])
            st1.append(i)
        
        for i in range(n):
            area=val[i]*(nxt[i]-prev[i]-1)
            max_h=max(max_h,area)
        return max_h