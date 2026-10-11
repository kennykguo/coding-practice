# Problem statement: README.md   |   Run tests: python3 test.py


def can_repair(grid: list[str], program: str) -> bool:

    rows = len(grid)
    cols = len(grid[0])

    # [1, 0] up -> L -> left
    # -> R -> right
    # [0, 1] right
    # [-1, 0] down
    # [0, -1] left

    # grid is a list of strings

    # follow through
    def dfs(r,c, dir, string, idx):


        # total moves 
        if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == "#" or idx == len(string)+1:
            # print("hi")
            # print(idx)
            return False
        
        if idx == len(string):
            return grid[r][c] == "T" 
        
        # what is the current action at that index
        if string[idx] == "F":
            dr, dc = dir
            # print(r + dr)
            # print(c + dc)
            # print(idx)
            return dfs(r + dr, c + dc, dir, string, idx + 1)
        
        elif string[idx] == "B":
            dr, dc = dir
            dr *= -1
            dc *= -1
            # print(r + dr)
            # print(c + dc)
            # print(idx)
            return dfs(r + dr, c + dc, dir, string, idx + 1)
        
        elif string[idx] == "L":
            if dir == [-1,0]: # up
                dir = [0, -1] # left
            elif dir == [0, -1]: # left
                dir = [1, 0] # down
            elif dir == [1, 0]: # down
                dir = [0, 1] # right
            else:
                dir = [-1,0] # up
            
            return dfs(r,c,dir,string, idx+1)
        
        else: # right
            if dir == [-1,0]: # up
                dir = [0, 1] # right
            elif dir == [0, -1]: # left
                dir = [-1, 0] # up
            elif dir == [1, 0]: # down
                dir = [0, -1] # left
            else: # right
                dir = [1,0] # down
            
            return dfs(r,c,dir,string, idx+1)
    
    startr = 0
    startc = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                startr = i
                startc = j
    
    for ch in ["F", "B", "L", "R"]:
        for i in range(len(program)):
            if program[i] == ch:
                continue
            
            new_program = program[0:i] + ch + program[i+1:]
            # print(ch)
            # print(new_program)
            if dfs(startr, startc, [-1, 0], new_program, 0):
                return True
    
    return False








