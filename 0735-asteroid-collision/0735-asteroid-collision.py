class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            while st and i<0 and st[-1]>0:
                if st[-1]<-i:
                    st.pop()
                elif st[-1]==-i:
                    st.pop()
                    break
                else:
                    break
            else:
                st.append(i)
        return st      