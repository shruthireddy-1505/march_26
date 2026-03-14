class Solution:
    def trap(self, h: List[int]) -> int:
        n_m=[0]*len(h)
        p_m=[0]*len(h)
        for i in range(len(h)-1,-1,-1):
            if i==len(h)-1:
                n_m[i]=h[i]
            else:
                n_m[i]=max(h[i],n_m[i+1])
        for i in range(len(h)):
            if i==0:
                p_m[i]=h[i]
            else:
                p_m[i]=max(h[i],p_m[i-1])
        res=0

        for i in range(len(h)):
            min_x=min(n_m[i],p_m[i])
            res+=min_x-h[i]
        return res
                