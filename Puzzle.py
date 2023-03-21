# Name: Julian Peterson
# CS325: Analysis of Algorithms
# Homework 8: Graph Algorithms II
# 3/6/2023

import copy
import heapq
import math


def solve_puzzle(Board, Source, Destination):
    """
    Solves a puzzle given a board (a nxm matrix where spaces are either roads, "-", or blockades, "#") a Source point
    (coordinates on the board) and a Destination point (coordinates on the board). The user must traverse from Source
    to Destination by only using the road spaces. The algorithm outputs the minimum path possible.
    """
    x, y = Source
    if Board[x][y] == "#":
        return None
    if Destination[0] == x and Destination[1] == y:
        return [Source]
    # initialize a mxn matrix that holds minimum number of traversals AND pathways to get to each square
    path_matrix = [[(math.inf, []) for _ in range(len(Board[0]))] for _ in range(len(Board))]
    # initialize a mxn matrix that checks which squares we've visited
    visited = [[False for _ in range(len(Board[0]))] for _ in range(len(Board))]
    # initialize starting square as 0 traversals
    temp_route = path_matrix[x][y][1]
    temp_traversal = 0
    path_matrix[x][y] = (temp_traversal, temp_route)

    path_matrix[x][y][1].append((x, y))
    # priority queue with (traversals, x coordinate, y coordinate)
    pq = [(0, x, y)]

    while pq:
        traversals, x, y = heapq.heappop(pq)
        if x == Destination[0] and y == Destination[1]:
            return path_matrix[x][y][1]
        if visited[x][y] is False:
            #up
            if x - 1 >= 0:
                if visited[x - 1][y] is False:
                    if Board[x - 1][y] == '-':
                        if path_matrix[x - 1][y][0] > path_matrix[x][y][0] + 1:
                            distance_to_here = path_matrix[x][y][0] + 1
                            path_to_here = copy.deepcopy(path_matrix[x][y][1])
                            path_to_here.append((x - 1, y))
                            path_matrix[x - 1][y] = (distance_to_here, path_to_here)
                        heapq.heappush(pq, (distance_to_here, x - 1, y))

            #down
            if x + 1 < len(Board):
                if visited[x + 1][y] is False:
                    if Board[x + 1][y] == '-':
                        if path_matrix[x + 1][y][0] > path_matrix[x][y][0] + 1:
                            distance_to_here = path_matrix[x][y][0] + 1
                            path_to_here = copy.deepcopy(path_matrix[x][y][1])
                            path_to_here.append((x + 1, y))
                            path_matrix[x + 1][y] = (distance_to_here, path_to_here)
                        heapq.heappush(pq, (distance_to_here, x + 1, y))

            #left
            if y - 1 >= 0:
                if visited[x][y - 1] is False:
                    if Board[x][y - 1] == '-':
                        if path_matrix[x][y - 1][0] > path_matrix[x][y][0] + 1:
                            distance_to_here = path_matrix[x][y][0] + 1
                            path_to_here = copy.deepcopy(path_matrix[x][y][1])
                            path_to_here.append((x, y - 1))
                            path_matrix[x][y - 1] = (distance_to_here, path_to_here)
                        heapq.heappush(pq, (distance_to_here, x, y - 1))


            #right
            if y + 1 < len(Board[0]):
                if visited[x][y + 1] is False:
                    if Board[x][y + 1] == '-':
                        if path_matrix[x][y + 1][0] > path_matrix[x][y][0] + 1:
                            distance_to_here = path_matrix[x][y][0] + 1
                            path_to_here = copy.deepcopy(path_matrix[x][y][1])
                            path_to_here.append((x, y + 1))
                            path_matrix[x][y + 1] = (distance_to_here, path_to_here)
                        heapq.heappush(pq, (distance_to_here, x, y + 1))

            visited[x][y] = True
    return None


# TEST CASES

#Puzzle = [
#    ['-', '-', '-', '-', '-'],
#    ['-', '#', '#', '-', '-'],
#    ['-', '-', '#', '-', '-'],
#    ['#', '-', '#', '#', '-'],
#    ['-', '#', '-', '-', '-']
#]

#Puzzle1 = [
#    ['#'],
#    ['-'],
#    ['-'],
#    ['-'],
#    ['-']
#]

#print(solve_puzzle(Puzzle, (0, 3), (3, 1)))
#print(solve_puzzle(Puzzle, (0, 2), (4, 2)))
#print(solve_puzzle(Puzzle1, (1, 0), (1, 0)))
#print(solve_puzzle(Puzzle, (0, 2), (2, 2)))
#print(solve_puzzle(Puzzle, (4, 2), (2, 2)))
#print(solve_puzzle(Puzzle, (2, 1), (4, 2)))