#!/usr/bin/python
""" A solution to a variation of a knights tour on a telephone keypad """

def find_paths(graph, node, length, repeat=False):
    """ Function to find all possible paths for the phone keypad graph """
    if length not in graph:
        return []
    if length == 0:
        return [[node]]
    paths = []
    for neighbor in graph[node]:
        for path in find_paths(graph, neighbor, length-1, repeat):
            if repeat:
                paths.append([node] + path)
            else:
                if node not in path:
                    paths.append([node] + path)
    return paths

if __name__ == '__main__':
    KNIGHT_GRAPH = {0: [4, 6], 1: [8, 6], 2: [9, 7], 3: [8, 4], 4: [0, 9, 3],
                    5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
    for i in range(0, 10):
        numbers = find_paths(KNIGHT_GRAPH, i, 9, repeat=True)
        for i in numbers:
            print ''.join([str(x) for x in i])
