class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stk = []
        for a in asteroids:
            if a > 0 or not stk:
                stk.append(a)
                continue
            
            speed = -a
            while stk and stk[-1] > 0:
                if stk[-1] < speed:
                    stk.pop()
                elif stk[-1] == speed:
                    stk.pop()
                    break
                else:
                    break
            else:
                stk.append(a)
                
        return stk
