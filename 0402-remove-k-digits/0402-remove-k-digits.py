class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if len(nums)==k:
            return "0"
        st=[]
        for i in nums:
            while st and st[-1]>i and k>0:
                st.pop()
                k-=1
            st.append(i)
        if k!=0:
            n=len(st)
            st=st[:n-k]

        join_fun="".join(st)
        l_strip=join_fun.lstrip("0")

        return l_strip if len(l_strip) >0 else "0"