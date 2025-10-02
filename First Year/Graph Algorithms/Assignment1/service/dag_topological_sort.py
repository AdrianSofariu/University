from domain.graph import DirectedGraph
import queue


def toposort_predecessor_counting(g: DirectedGraph):
    """
    Topological sort of a directed graph using the predecessor counting algorithm
    :param g: DirectedGraph
    :return: a list of vertices in topological sorting order, or null if G has cycles
    """
    sorted = []
    q = queue.Queue()
    count = dict()

    # put all vertices with no predecessors in the queue
    for vertex in g.parse_vertices():
        count[vertex] = g.in_degree(vertex)
        if count[vertex] == 0:
            q.put(vertex)

    while not q.empty():
        vertex = q.get()
        sorted.append(vertex)
        for y in g.parse_outbound_edges(vertex):
            count[y] -= 1
            if count[y] == 0:
                q.put(y)

    if len(sorted) < g.get_number_of_vertices():
        return None

    return sorted


def highest_cost_path(g: DirectedGraph, s: int, d: int):
    """
    Finds the highest cost path from node s to node d in the graph if it a DAG
    :return: path or None if not a DAG
    """
    dist = dict()

    topo_order = toposort_predecessor_counting(g)
    if topo_order is None:
        return None

    for vertex in g.parse_vertices():
        dist[vertex] = -10**9
    dist[s] = 0
    prev = dict()
    prev[s] = None

    for vertex in topo_order:
        for adj in g.parse_outbound_edges(vertex):
            if dist[adj] < dist[vertex] + g.get_cost_of_edge(vertex, adj):
                dist[adj] = dist[vertex] + g.get_cost_of_edge(vertex, adj)
                prev[adj] = vertex

    path = []
    if dist[d] == -10**9:
        return None

    if s not in prev:
        return None
    path.append(d)
    vertex = d
    while vertex != s:
        if vertex not in prev:
            return None
        vertex = prev[vertex]
        path.append(vertex)
    path.reverse()
    return path


def numberpaths(g: DirectedGraph, s: int, d: int):
    dist = dict()
    paths = dict()
    visited = set()
    q = queue.Queue()

    for vertex in g.parse_vertices():
        dist[vertex] = -100
    dist[s] = 0
    paths[s] = 1
    q.put(s)

    while not q.empty():
        x = q.get()
        if x not in visited:
            for y in g.parse_outbound_edges(x):
                if dist[y] < dist[x] + 1:
                    dist[y] = dist[x] + 1
                    paths[y] = paths[x]
                    q.put(y)
                elif dist[y] == dist[x] + 1:
                    paths[y] += paths[x]
                    q.put(y)
            visited.add(x)

    if d in paths.keys():
        return paths[d]
    else:
        return 0


