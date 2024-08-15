import numpy as np
import matplotlib.pyplot as plt


def generate_maze_prim(width, height):
    maze = np.ones((height, width), dtype=int)

    def add_frontier(frontier, x, y):
        if x >= 0 and x < width and y >= 0 and y < height:
            if maze[y][x] == 1:
                maze[y][x] = 2
                frontier.append((x, y))

    def mark(x, y):
        maze[y][x] = 0
        frontier = []
        add_frontier(frontier, x + 2, y)
        add_frontier(frontier, x - 2, y)
        add_frontier(frontier, x, y + 2)
        add_frontier(frontier, x, y - 2)
        while frontier:
            fx, fy = frontier.pop(np.random.randint(0, len(frontier)))
            if maze[fy][fx] == 2:
                neighbours = []
                if fx >= 2 and maze[fy][fx - 2] == 0:
                    neighbours.append((fx - 2, fy))
                if fx < width - 2 and maze[fy][fx + 2] == 0:
                    neighbours.append((fx + 2, fy))
                if fy >= 2 and maze[fy - 2][fx] == 0:
                    neighbours.append((fx, fy - 2))
                if fy < height - 2 and maze[fy + 2][fx] == 0:
                    neighbours.append((fx, fy + 2))
                if neighbours:
                    nx, ny = neighbours[np.random.randint(0, len(neighbours))]
                    maze[(fy + ny) // 2][(fx + nx) // 2] = 0
                    maze[fy][fx] = 0
                    add_frontier(frontier, fx + 2, fy)
                    add_frontier(frontier, fx - 2, fy)
                    add_frontier(frontier, fx, fy + 2)
                    add_frontier(frontier, fx, fy - 2)

    mark(1, 1)
    maze[0][1] = 0
    maze[height - 1][width - 2] = 0
    return maze


width, height = 31, 31
maze = generate_maze_prim(width, height)

fig, ax = plt.subplots(figsize=(20, 20))
ax.imshow(maze, cmap="binary", interpolation="none")
ax.axis("off")
plt.title("The Maze")
plt.show()
