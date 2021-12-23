from queue import PriorityQueue
from collections import defaultdict
import numpy as np

def dijkstra(matrix, start, dest):
    rows, cols = matrix.shape
    queue = PriorityQueue()

    queue.put((0, start))
    visited = {start}

    while queue:
        currentRisk, (i, j) = queue.get()
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

        if i == dest[0] and j == dest[1]:
            return currentRisk

        for row, col in neighbors:
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                risk = matrix[row, col]
                queue.put((currentRisk + risk, (row, col)))
                visited.add((row, col))


matrix = []
with open("input15.txt") as input:
    data = input.read().split("\n")[:-1]
    matrix = [[int(j) for j in i] for i in data]
rows = len(matrix)
cols = len(matrix[0])
print(dijkstra(np.array(matrix), (0, 0), (rows - 1, cols - 1)))
matrix = np.array(matrix)
matrix = np.block([[(matrix + i + j - 1) % 9 + 1 for i in range(5)] for j in range(5)])
rows = len(matrix)
cols = len(matrix[0])
print(dijkstra(np.array(matrix), (0, 0), (rows - 1, cols - 1)))
