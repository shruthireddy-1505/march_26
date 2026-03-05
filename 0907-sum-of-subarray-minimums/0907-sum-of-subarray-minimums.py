class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        st=[]
        n=len(arr)
        nxt_small=[0]*n
        for i in range(len(arr)-1,-1,-1):
            count=1
            while st and st[-1][0]>=arr[i]:
                count+=st.pop()[1]
            nxt_small[i]=count
            st.append((arr[i],count))
        
        st1=[]
        prev_small=[0]*n
        for i in range(len(arr)):
            count=1
            while st1 and st1[-1][0]>arr[i]:
                count+=st1.pop()[1]
            prev_small[i]=count
            st1.append((arr[i],count))
        
        res=0
        for i in range(len(arr)):
            res+=arr[i]*nxt_small[i]*prev_small[i]
        return res % mod
        
        

        