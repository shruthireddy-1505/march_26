class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st_nxt=[]
        nxt_smaller=[]
        max_area=0
        for i in range(len(heights)-1,-1,-1):
            while st_nxt and heights[st_nxt[-1]]>=heights[i]:
                st_nxt.pop()
            if st_nxt:
                nxt_smaller.append(st_nxt[-1])
            else:
                nxt_smaller.append(len(heights))
            st_nxt.append(i)
        nxt_smaller=nxt_smaller[::-1]

        st_prev=[]
        prev_smaller=[]
        for i in range(len(heights)):
            while st_prev and heights[st_prev[-1]]>=heights[i]:
                st_prev.pop()
            if st_prev:
                prev_smaller.append(st_prev[-1])
            else:
                prev_smaller.append(-1)
            st_prev.append(i)

        for i in range(len(heights)):
            area=heights[i]*(nxt_smaller[i]-prev_smaller[i]-1)
            max_area=max(max_area,area)
        return max_area

            