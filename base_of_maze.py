# Create the level 1
def level_one():
    
    return [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],  
        ['#', 'P', '.', '.', '.', '💎', '.', '.', '#'],  
        ['#', '.', '#', '#', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '#', '.', '#'], 
        ['#', '.', '#', '#', '#', '#', '#', '.', '#'],  
        ['#', '.', '.', '.', '💎', 'E', '.', '.', '#'],  
        ['#', '#', '#', '#', '#', '#', '#', '#', '#']   
    ]  
# Return creates lsits presenting the maze
# '#' = wall (cannot move), '.' = empty path(open path), 'P' = Player, 'E' = Exit, '💎' = treasure
# Level 1 is easy without traps and simple



#Create the Level 2
def level_two():
  
    return [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],    
        ['#', 'P', '.', '#', '.', '💎', '.', '#', '.', '.', '#'],    
        ['#', '.', '.', '#', '.', '#', '.', '#', '.', '💣', '#'],    
        ['#', '.', '#', '#', '.', '#', '.', '.', '.', '#', '#'],    
        ['#', '.', '.', '.', '.', '#', '#', '#', '.', '💎', '#'],   
        ['#', '#', '#', '💣', '.', '.', '.', '.', '.', '#', '#'],   
        ['#', '.', '.', '.', '#', '#', '.', '#', '.', '.', '#'],     
        ['#', '.', '💎', '.', '.', '.', '.', '#', '.', 'E', '#'],    
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']     
    ]
# Return creates lsits presenting the maze
# '#' = wall (cannot move), '.' = empty path(open path), 'P' = Player, 'E' = Exit, '💎' = treasure, '💣' = trap
# Level 2 is medium with traps and more steps




# Create the Level 3
def level_three():
    
    return [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],  
        ['#', 'P', '.', '.', '.', '💎', '#', '.', '.', '.', '.', '💣', '#'],  
        ['#', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#', '#', '#'], 
        ['#', '.', '💣', '.', '.', '.', '#', '.', '.', '.', '.', '💎', '#'],  
        ['#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],  
        ['#', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#'],  
        ['#', '#', '#', '.', '#', '.', '#', '#', '.', '#', '.', '💣', '#'],  
        ['#', '💎', '.', '.', '.', '.', '.', '💣', '.', '.', '.', '.', '#'],  
        ['#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#'],  
        ['#', '.', '.', '💎', '.', '.', '#', '.', '.', '.', '.', 'E', '#'],  
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']   
    ]
# Return creates lsits presenting the maze
# '#' = wall (cannot move), '.' = empty path(open path), 'P' = Player, 'E' = Exit, '💎' = treasure, '💣' = trap
# Level 3 is hard with more traps and the biggest maze




# Move function that regulates the movements
def moves(maze, positions, directions):
    
    row, col = positions  # row = current row number, col = current column number
    
    # Movement directions
    if directions == 'w':
        new_positions = (row - 1, col)  # 'w' = up: decrease ROW by 1 
   
    elif directions == 's':
        new_positions = (row + 1, col)  # 's' = down: INCREASE ROW by 1
    
    elif directions == 'a':
        new_positions = (row, col - 1) # 'a' = left: decrease COLUMN by 1
    
    elif directions == 'd':
        new_positions = (row, col + 1) # 'd' = right: increase COLUMN by 1
    
    else:
        return None  # Returns None for invalid move
    
    # Checking new position status and avaiqlability
    new_row, new_col = new_positions  # new_row = first number, new_col = second
    
    
    if new_row < 0:
        return None # First Check: new_row too small? (above top row 0)
    
    if new_row >= len(maze):  # len(maze) = number of rows
        return None # Second Check: new_row too big? (past bottom row)
    
    if new_col < 0:
        return None # Third Check: new_col too small? (left of column 0)
   
    if new_col >= len(maze[0]):  # len(maze[0]) = columns in row 0 (all rows same width)
        return None # Fourth Check: new_col too big? (right of last column)
    
    
    if maze[new_row][new_col] == '#':  # maze[row][col] gets 1 character
        return None  # Can't move to walls!
    # Final check: Is target character a wall '#'?


    return new_positions  # ALL checks passed - return new position


#count All treasures
def treasures(maze):
    
    
    count = 0  # Start at 0 and add 1 for each treasure found
    
    # Loop over all row in maze
    for row in maze:  # row = one list like ['#', 'P', '.']
        # Loop over all character in this row
        for character in row:  # character = diamond, wall, etc.
            
            if character == '💎':  # Exact match
                # Add 1 to total to treasure count
                count += 1  
    
   
    return count # Return total number of treasures found



# Find positions of symbols and characters
def finish(maze, symbol):
    
    # Loop rows with index (need numbers for return)
    for i in range(len(maze)):  # i = 0,1,2 ... (row numbers)
        # Loop columns in this row with index
        for j in range(len(maze[i])):  # j = 0,1,2 ... (column numbers)
            # Check whether symbol found
            if maze[i][j] == symbol:  # ex: maze[1][1] == 'P'
                # Return position (row, col)
                return (i, j)  
    
    return None  # Some symbols may be missing