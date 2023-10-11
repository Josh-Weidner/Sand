from copy import deepcopy

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None for i in range(width)] for j in range(height)]

    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'
    
    def __repr__(self):
        return f'Grid.build({self.array})'
    
    def __eq__(self, other):
        if isinstance(other, Grid):
            if self.array == other.array:
                print("They are the same!")
                return True
            else:
                print('They are different')
                return False
        elif isinstance(other, list):
            return self.array == other

    def get(self, x, y):
        if self.in_bounds(x, y):
            coordinate = self.array[y][x]
            return coordinate

    def set(self, x, y, val):
        if self.in_bounds(x, y):
            self.array[y][x] = val
  
    def in_bounds(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)
    
    @staticmethod
    def check_list_malformed(lst):
        if not isinstance(lst, list):
            raise ValueError("The object passed in should be a list object")
        if lst == []:
            raise ValueError("The top-level list should not be empty")
        for i in lst:
            if not isinstance(i, list):
                raise ValueError("Each element of the list object should also be a list object")
        for i in lst[1:]:
            if not len(i) == len(lst[0]):
                raise ValueError("Each element of the top-level list should have the same length")
        
    @staticmethod    
    def build(lst):
        if not Grid.check_list_malformed(lst):
            height = len(lst)
            width = len(lst[0])
            grid = Grid(width, height)
            grid.array = deepcopy(lst)
            print("this is the grid: ", grid)
            return grid
        
    def copy(self):
        return Grid.build(self.array)

# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# grid = Grid.build([[5, 4, 3, 3, 4], [4, 1, 5, 2, 2]])

# print(grid)
# print(str(grid))
# print(repr(grid))
