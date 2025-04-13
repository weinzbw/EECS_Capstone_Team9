"""
Program Name: maze_solver_static.py
Description: Proof of concept for a static maze solver using flood-fill algorithm. 
Programmer(s): Naran Bat
Date Made: 2/11/2025
Date(s) Revised:
2/16/2025: Added comments and cleaned up code.
Preconditions:
Postconditions:
Errors/Exceptions:
Side Effects:
Invariants:
Known Faults:
"""
# Maze size
N = 8
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

class MazeSolver:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal
        # Initialize distance map
        self.distances = [[-1 for _ in range(N)] for _ in range(N)]  # Distance map

    def flood_fill(self):
        """Assigns distance values using flood-fill algorithm."""
        queue = [self.goal]
        self.distances[self.goal[0]][self.goal[1]] = 0  # Goal is at distance 0
        
        while queue:
            r, c = queue.pop(0) # Dequeue

            # Visit all neighbors
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc # Neighbor position
                
                # Check if neighbor is within bounds and not a wall
                if 0 <= nr < N and 0 <= nc < N and self.maze[nr][nc] != '█':
                    if self.distances[nr][nc] == -1:  # Unvisited cell
                        self.distances[nr][nc] = self.distances[r][c] + 1 # Update distance
                        queue.append((nr, nc)) # Enqueue

    def find_path(self):
        """Finds the shortest path from start to goal."""
        path = []
        current = self.start
        
        # Traverse the maze from start to goal
        while current != self.goal:
            path.append(current) # Add current position to path
            r, c = current # Current position
            min_value = float('inf') # Initialize minimum distance
            next_move = None # Next move
            
            # Find the neighbor with the smallest distance
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc # Neighbor position

                # Check if neighbor is within bounds and not a wall
                if 0 <= nr < N and 0 <= nc < N and self.maze[nr][nc] != '█':

                    # Check if neighbor has a smaller distance
                    if self.distances[nr][nc] < min_value:
                        min_value = self.distances[nr][nc] # Update minimum distance
                        next_move = (nr, nc) # Update next move
            
            # Move to the next position
            if next_move:
                current = next_move # Update current position
            else:
                print("No path found!") # No path found
                return []
        
        path.append(self.goal) # Add goal position to path
        return path # Return path

    def display_maze(self):
        """Displays the maze with flood-fill distances."""
        for r in range(N):
            for c in range(N):
                if self.maze[r][c] == '█':
                    print("██", end=" ")  # Wall
                elif (r, c) == self.start:
                    print("S ", end=" ")  # Start
                elif (r, c) == self.goal:
                    print("G ", end=" ")  # Goal
                else:
                    print(f"{self.distances[r][c]:2}", end=" ")
            print()

# Define 8x8 solvable maze
maze_grid = [
    ['S', '.', '█', '█', '█', '█', '█', '█'],
    ['.', '.', '█', '.', '.', '.', '.', '█'],
    ['█', '.', '█', '.', '█', '█', '.', '█'],
    ['█', '.', '.', '.', '█', '█', '.', '█'],
    ['█', '█', '█', '.', '.', '.', '.', '█'],
    ['█', '.', '.', '.', '█', '█', '.', '█'],
    ['█', '.', '█', '█', '█', '█', '.', 'G'],
    ['█', '█', '█', '█', '█', '█', '█', '█']
]

# Set start and goal positions
start_position = (0, 0)
goal_position = (6, 7)

# Solve the maze
solver = MazeSolver(maze_grid, start_position, goal_position)
solver.flood_fill()
path = solver.find_path()

# Display the Flood-Filled Maze
solver.display_maze()

# Show the path
print("Path from start to goal:", path)
