from base_of_maze import (
    level_one, level_two, level_three, moves, treasures    # Get helpers
)
# Imported ALL functions from the other file (base_of_maze.py)



# Display the maze fixed width (like col to col)
def display(maze, player_position, treasures_collected, total_treasures):
   
    # Loop every row number 
    for i in range(len(maze)):  # i = row index (0=top, 6=bottom for level1)
        build_row = ""  # Will build like "###P####"
        
        # Loop every column in this row
        for j in range(len(maze[i])):  # j = col index (0=left, 8=right)
            
            if (i, j) == player_position:  # Correct position (1,1) == (1,1) = True
                # Show P for player
                build_row += "P"  # moves the P to current position
            else:
                build_row += maze[i][j] #Show whatever is in maze[i][j] (characters)
        
        print(build_row)  # One row complete. Prints: #P....💎..#  (adjusts)
    
    # After maze, print treasure status
    print("Treasures: ", treasures_collected, "/", total_treasures)  # After maze, print treasure status(ex:2/2)



#Main game function to play one level and return win/lose
def levels(level_index, maze, max_moves):
    # Start: Find player 'P' and exit 'E' positions
    player_position = None  # Will be (row,col) like (1,1)
    exit_position = None    # Will be (5,5) for level 1
    
    # Scans the entire maze row by row, charcters too
    for i in range(len(maze)):      # Every row
        for j in range(len(maze[i])):  # Every column
            # Found player start
            if maze[i][j] == 'P':
                player_position = (i, j)     # Save position
                maze[i][j] = '.'        # Clear 'P' -> empty path
            # Found exit
            elif maze[i][j] == 'E':
                exit_position = (i, j)       # Save position (don't clear!)
    
    # Traack treasures collected
    total_treasures = treasures(maze)  # Scans maze for treasures
    treasures_collected = 0  # Start at zero
    move_count = 0           
    
    # Print level header
    print("\n" + "=" * 50)
    print("LEVEL", level_index)
    print("=" * 50)
    print("P:Player | E:Exit | 💎:Treasure | 💣:Bomb | #:Wall")
    print("w:up a:left s:down d:right")
    print("Max moves:",  max_moves, "|" , "Treasures: ", total_treasures)
    print("=" * 50 + "\n")

    # Infinite loop till win/lose
    while True:  # Runs forever until return/break
        # Show current maze + stats
        display(maze, player_position, treasures_collected, total_treasures)
        print("Moves: ", move_count, "/", max_moves)

        #Check all targets completed?
        if player_position == exit_position:  # Col and Row same?
            if treasures_collected == total_treasures:
                print("Level Completed!")
                print("Moves used: ", move_count, "/", max_moves)
                return True  # WIN! Exit function
            else:
                # At exit but missing treasures
                missing = total_treasures - treasures_collected
                print("Need ", missing, "more treasures")
                print()
                # Don't exit, allow for next move

        # Whether lost the game?
        if move_count >= max_moves:
            print("Out of moves. Level Failed!")
            return False  # Lost! Exit function

        # Get input from player (quit or move)
        move = input("\nMove (w/a/s/d) or 'q'quit: ").strip().lower()

        # Quit?
        if move == 'q':
            print("Thanks for playing!")
            return False

        # Invalid input?
        if move not in ('w', 'a', 's', 'd'):
            print("Invalid! Use w/a/s/d")
            continue  # Restart loop (ask again)

        # TRY MOVE (Person 1's function)
        new_position = moves(maze, player_position, move)
        
        # Invalid move?
        if new_position is None:
            print("Can't move! (wall)")
            continue  # Try again
        
        # If valid, update everything(position, moves, treasures, bombs)
        player_position = new_position      # New position
        move_count += 1           # +1 move
        r, c = new_position            # Another new row,col
        symbol = maze[r][c]         # symbol at new position

        # TREASURE?
        if symbol == '💎':
            treasures_collected += 1  # +1 treasure
            maze[r][c] = '.'          # Remove treasure
            print("Treasure collected!")
        # TRAP?
        elif symbol == '💣':
            move_count += 3           # Penalty: +3 moves
            maze[r][c] = '.'          # Remove bomb
            print("BOMB! -3 moves!")
        # Normal move
        else:
            print("Moved!")

        print()  #nothing

# Full game function to run all 3 levels
def main():
    # Welcome screen
    print("\n" + "=" * 50)
    print("MAZE EXPLORATION GAME!")
    print("=" * 50)
    print("\nWin all 3 levels!")
    print("Rules:")
    print("Collect ALL 💎 before E")
    print("💣 = +3 moves penalty")
    print("Stay under move limit")
    print("\nLet's get out!\n")
    input("Press Enter to start...") 

    # List of ALL levels: (number, maze, max_moves)
    game_levels = [
        (1, level_one(), 40),  
        (2, level_two(), 50), 
        (3, level_three(), 70)   
    ]

    total_score = 0  # Start score zero

    # Play all levels
    for lvl, maze, max_moves in game_levels:
        won = levels(lvl, maze, max_moves)  # Play 1 level
        if won:
            # Score = 100 * level number
            total_score += 100 * lvl
            if lvl < 3:  # Not final level?
                print(f"\nLevel {lvl}! +{100 * lvl} points")
                input("\nPress Enter for next...")
        else:
            # Failed/quit
            print(f"\nGame Over - Level {lvl}")
            print("Final Score: ", total_score)
            return  # END GAME

    # VICTORY! 
    print("\n" + "=" * 50)
    print("CONGRATULATIONS!")
    print("=" * 50)
    print("ALL LEVELS COMPLETEd!")
    print("Final Score: ", total_score)
    print("=" * 50)


if __name__ == "__main__":
    main()  # Start everything!