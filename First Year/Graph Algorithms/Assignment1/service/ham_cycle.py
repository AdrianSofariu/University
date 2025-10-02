from domain.graph import DirectedGraph


def find_ham_cycle(g: DirectedGraph):
    """
    Find a Hamiltonian cycle in the graph if it exists
    :return: the cycle or None if it does not exist
    """
    n = g.get_number_of_vertices()
    visited = [False] * n
    cycle = [-1]*n
    cycle[0] = 0

    return ham_cycle_util(g, cycle, 1)


def is_valid(g: DirectedGraph, vertex: int, pos: int, cycle: list):
    """
    Check if a vertex can be added to the cycle
    :param g: the graph
    :param vertex: the vertex to be added
    :param pos: the current position in the cycle
    :param cycle: the current cycle
    :return: True if the vertex can be added, False otherwise
    """
    if not g.edge_exists(cycle[pos - 1], vertex):
        return False

    for i in range(pos):
        if cycle[i] == vertex:
            return False

    return True


def ham_cycle_util(g: DirectedGraph, cycle: list, pos: int):
    """
    Utility function for finding a Hamiltonian cycle
    :param g: the graph
    :param cycle: the current cycle
    :param pos: the current position in the cycle
    :return: a cycle
    """
    if pos == g.get_number_of_vertices():
        if g.edge_exists(cycle[pos - 1], cycle[0]):
            return cycle
        else:
            return None

    for vertex in g.parse_vertices():
        if is_valid(g, vertex, pos, cycle):
            cycle[pos] = vertex
            if ham_cycle_util(g, cycle, pos + 1):
                return cycle
            cycle[pos] = -1

    return None
