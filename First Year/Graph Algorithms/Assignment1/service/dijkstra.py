from domain.graph import DirectedGraph
import queue


def backwards_dijkstra(g: DirectedGraph, s: int, d: int):
    """
    Backwards dijkstra to find the lowest cost walk between s and d
    :param g: directed graph with positive costs
    :param s: source vertex
    :param d: destination vertex
    :return: a tuple with two dictionaries: parent, dist
    """
    q = queue.PriorityQueue()
    next = dict()
    dist = dict()

    q.put((0, d))
    dist[d] = 0
    found = False

    while not q.empty() and not found:
        x = q.get()[1]
        for y in g.parse_inbound_edges(x):
            if y not in dist or dist[x] + g.get_cost_of_edge(y, x) < dist[y]:
                dist[y] = dist[x] + g.get_cost_of_edge(y, x)
                next[y] = x
                q.put((dist[y], y))
        if x == s:
            found = True

    return next, dist


def lowest_cost_walk(g: DirectedGraph, s: int, d: int):
    """
    Finds the lowest cost walk from node s to node d in the graph using backwards Dijkstra
    :return: the path
    """
    next, dist = backwards_dijkstra(g, s, d)
    path = []
    cost = 0
    if s not in dist:
        return None, cost
    else:
        vertex = s
        while vertex != d:
            path.append(vertex)
            prev = vertex
            vertex = next[vertex]
            cost += g.get_cost_of_edge(prev, vertex)
        path.append(d)
        return path, cost
