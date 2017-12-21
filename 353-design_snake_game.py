from collections import deque

class SnakeGame:
    dirmap = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.food_stk = list(reversed(list(map(tuple, food))))
        self.snake = deque()
        self.snake_coords = set()
        self.__AddHead((0, 0))
        self.score = 0
        
        
    def __AddHead(self, coord):
        if coord in self.snake_coords:
            return False
        self.snake.appendleft(coord)
        self.snake_coords.add(coord)
        return True
        
    def __RemoveTail(self):
        tail = self.snake.pop()
        self.snake_coords.remove(tail)
    
    @staticmethod
    def computeCoord(coord, direction):
        mv = SnakeGame.dirmap[direction]
        return (coord[0] + mv[0], coord[1] + mv[1])

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        
        """ 
        Moving snake is:
        - count new position of head depending on direction
        -   if we out of boundaries => return -1
        -   if snake' body already have this coordinate => return -1 (collide)
        - insert new head to self.snake beggining
        - cut tail unless our new head met food
        """
        new_head = SnakeGame.computeCoord(self.snake[0], direction)
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1 # out of boundaried
        
        if self.food_stk and new_head == self.food_stk[-1]:
            self.score += 1
            self.food_stk.pop()
        else:
            self.__RemoveTail()
            
        if not self.__AddHead(new_head):
            return -1 # collision
            
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
