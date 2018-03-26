class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        # get all valid neighbors
        def getNeighbors(pt):
            nears = []
            for p in (pt[0]-1, pt[1]), (pt[0]+1, pt[1]), (pt[0], pt[1]-1), (pt[0], pt[1]+1):
                if 0 <= p[0] < len(image) and 0 <= p[1] < len(image[p[0]]):
                    nears.append(p)
                            
            return nears
        
        base_color = image[sr][sc]
        if base_color == newColor:
            return image
        
        image[sr][sc] = newColor
        frontier = set([(sr, sc)])
        
        while frontier:
            next_frontier = set()
            for pt in frontier:
                for near in getNeighbors(pt):
                    if image[near[0]][near[1]] == base_color:
                        image[near[0]][near[1]] = newColor
                        next_frontier.add(near)
                        
            frontier = next_frontier
            
        return image
                    
                
        
