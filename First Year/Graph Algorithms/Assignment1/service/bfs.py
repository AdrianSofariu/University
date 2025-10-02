from domain.graph import DirectedGraph


def bfs(g: DirectedGraph, s: int):
    """
    Breadth-first search in graph g from vertex s
    :param g: a DirectedGraph
    :param s: source vertex
    :return: a tuple with two dictionaries: parent, dist
    the first is a dictionary mapping each vertex to its parent in the BFS tree
    the second is a dictionary mapping each vertex to the distance from s
    """
    parent = {s: None}
    dist = {s: 0}

    queue = [s]
    while len(queue) != 0:
        vertex = queue.pop(0)
        for neighbour in g.parse_outbound_edges(vertex):
            if neighbour not in dist:
                queue.append(neighbour)
                parent[neighbour] = vertex
                dist[neighbour] = dist[vertex] + 1
    return parent, dist


def shortest_path(g, s, t):
    """
    Find and returns the shortest path in graph g from vertex s to vertex t
    :return: the path as a sequence of vertices, or None if there is no path
    """
    parent, dist = bfs(g, s)
    path = []
    if len(parent) == 1:
        return None
    elif t not in parent:
        return None
    else:
        vertex = t
        while vertex != s:
            path.insert(0, vertex)
            vertex = parent[vertex]
        path.insert(0, s)
        return path
