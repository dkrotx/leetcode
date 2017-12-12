class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nbars = len(height)
        cur_bar = 0
        trapped = 0
        
        while cur_bar+1 < nbars:
            pair = None
            # find pair of at least the same height
            for i in range(cur_bar+1, nbars):
                if height[i] >= height[cur_bar]:
                    pair = i
                    break
            else:
                # or maximum height
                pair = cur_bar+1
                for i in range(cur_bar+2, nbars):
                    if height[i] > height[pair]:
                        pair = i

            water_level = min(height[cur_bar], height[pair])

            for i in range(cur_bar+1, pair):
                trapped += water_level - height[i]
            
            cur_bar = pair
            
        return trapped
