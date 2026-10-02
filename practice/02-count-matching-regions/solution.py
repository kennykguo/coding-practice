# Problem statement: README.md   |   Run tests: python3 test.py

def count_matching_regions(grid1: list[str], grid2: list[str]) -> int:
    
    rows = len(grid1)
    cols = len(grid1[0])

    num_grid1 = [[int(ch) for ch in row] for row in grid1]   
    num_grid2 = [[int(ch) for ch in row] for row in grid2]   
    grid1 = num_grid1
    grid2 = num_grid2

    # cells must start off with matching 1 cells

    visited1 = set()
    visited2 = set()
    grid1_set = set()
    grid2_set = set()

    def dfs_grid1(r,c):

        # treat like mini islands
        if (r,c) in visited1 or grid1[r][c] != 1:
            return

        visited1.add((r,c))
        grid1_set.add((r,c))
        
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]: # go all directions
            new_r = r + dr
            new_c = c + dc

            if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and grid1[new_r][new_c] == 1: # check in bounds, and a 1
                dfs_grid1(new_r, new_c)
        
    def dfs_grid2(r,c):

        # treat like mini islands
        if (r,c) in visited2 or grid2[r][c] != 1:
            return

        visited2.add((r,c))
        grid2_set.add((r,c))
        
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]: # go all directions
            new_r = r + dr
            new_c = c + dc

            if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and grid2[new_r][new_c] == 1: # check in bounds, and a 1
                dfs_grid2(new_r, new_c)
    
    res = 0
    for i in range(rows):
        for j in range(cols):
            if grid1[i][j] == 1 and grid2[i][j] == 1 and (i,j) not in visited1 and (i,j) not in visited2:
                grid1_set = set()
                grid2_set = set()
                dfs_grid1(i,j)
                dfs_grid2(i,j)
                # print(i,j)
                # print(grid1_set)
                # print(grid2_set)
                # print("grids")
                # print(grid1)
                # print(grid2)
                if grid1_set == grid2_set:
                    res +=1
    
    return res

    
    
