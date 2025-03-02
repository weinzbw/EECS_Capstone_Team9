"""
Program Name: dynamic_maze_solver.py
Description: Proof of concept for a dynamic maze solver using flood-fill algorithm.
             Assumes the solver does not have prior knowledge of the maze layout.
Programmer(s): Naran Bat
Date Made: 2/16/2025
Date(s) Revised:
Preconditions: 
Postconditions: 
Errors/Exceptions:
Side Effects:
Invariants: 
Known Faults:
"""
import time
from collections import deque

N = 8
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

class DynamicMazeSolver:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.robot_position = start
        self.known_walls = set()
        self.path = []
        self.explored = set()

    def heuristic(self, position):
        """Manhattan distance from position to goal."""
        return abs(position[0] - self.goal[0]) + abs(position[1] - self.goal[1])

    def bfs_recalculate_path(self):
        """Recalculates the best path using BFS based on discovered walls."""
        queue = deque([(self.robot_position, [])])
        visited = set()
        
        while queue:
            (r, c), path = queue.popleft()
            
            if (r, c) == self.goal:
                return path  # Return shortest path found
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in self.known_walls:
                    queue.append(((nr, nc), path + [(nr, nc)]))
        
        return []  # No path found

    def move_robot(self):
        """Moves the robot optimistically toward the goal."""
        while self.robot_position != self.goal:
            print("\nCurrent Robot Position:", self.robot_position)
            self.display_maze()
            time.sleep(0.5)  # Pause for visualization

            next_moves = sorted(
                [(self.robot_position[0] + dr, self.robot_position[1] + dc) for dr, dc in DIRECTIONS],
                key=lambda pos: self.heuristic(pos) if (0 <= pos[0] < N and 0 <= pos[1] < N) else float('inf')
            )

            for move in next_moves:
                if move in self.known_walls:
                    continue
                if 0 <= move[0] < N and 0 <= move[1] < N:
                    if self.maze[move[0]][move[1]] == '█':
                        self.known_walls.add(move)  # Discover new wall
                    else:
                        self.robot_position = move
                        self.explored.add(move)
                        break
            else:
                # No valid move found, recalculate path
                print("Recalculating path due to blockage...")
                self.path = self.bfs_recalculate_path()
                if not self.path:
                    print("No available path!")
                    return
                self.robot_position = self.path.pop(0)  # Move to next best step

        print("Robot reached the goal!")
        self.display_maze()

    def display_maze(self):
        """Displays the maze dynamically with known information."""
        for r in range(N):
            for c in range(N):
                if (r, c) == self.robot_position:
                    print("M ", end=" ")  # robot position
                elif (r, c) == self.start:
                    print("S ", end=" ")  # Start position
                elif (r, c) == self.goal:
                    print("G ", end=" ")  # Goal position
                elif (r, c) in self.known_walls:
                    print("██", end=" ")  # Discovered wall
                else:
                    print(". ", end=" ")  # Unexplored space
            print()

# Define a hidden 8x8 maze (robot does not initially know this layout)
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

start_position = (0, 0)
goal_position = (6, 7)

solver = DynamicMazeSolver(maze_grid, start_position, goal_position)
solver.move_robot()
