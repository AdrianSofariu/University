from domain.graph import DirectedGraph
from service.bfs import shortest_path
from service.dijkstra import lowest_cost_walk
from service.dag_topological_sort import highest_cost_path, numberpaths
from service.ham_cycle import find_ham_cycle


class Service:

    def __init__(self):
        self.__graph = DirectedGraph()

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph
        :param vertex: vertex to be added
        """
        self.__graph.add_vertex(vertex)

    def remove_vertex(self, vertex):
        """
        Remove a vertex from the graph
        :param vertex: vertex to be removed
        """
        self.__graph.remove_vertex(vertex)

    def add_edge(self, start_vertex, end_vertex):
        """
        Add an edge to the graph
        :param start_vertex: starting vertex
        :param end_vertex: ending vertex
        """
        self.__graph.add_edge(start_vertex, end_vertex)

    def remove_edge(self, start_vertex, end_vertex):
        """
        Remove an edge from the graph
        :param start_vertex: starting vertex
        :param end_vertex: ending vertex
        """
        self.__graph.remove_edge(start_vertex, end_vertex)

    def init_graph_with_n_vertices(self, n):
        """
        Initialize the graph with n vertices
        :param n: number of vertices
        """
        self.__graph.make_graph(n)

    def get_number_of_vertices(self):
        """
        Return the number of vertices in the graph
        :return: nr of vertices
        """
        return self.__graph.get_number_of_vertices()

    def get_vertices(self):
        """
        Return the list of vertices
        :return: list of vertices
        """
        return self.__graph.parse_vertices()

    def get_in_degree(self, vertex):
        """
        Return the in degree of a vertex
        :param vertex:
        :return: in-degree of the given vertex
        """
        return self.__graph.in_degree(vertex)

    def get_out_degree(self, vertex):
        """
        Return the out degree of a vertex
        :param vertex:
        :return: out-degree of the given vertex
        """
        return self.__graph.out_degree(vertex)

    def search_edge(self, start_vertex, end_vertex):
        """
        Search for an edge
        :param start_vertex: starting vertex
        :param end_vertex: ending vertex
        :return: True if the edge exists, False otherwise
        """
        return self.__graph.edge_exists(start_vertex, end_vertex)

    def get_outbound_neighbours(self, vertex):
        """
        Return the outbound neighbours of a vertex
        :param vertex:
        :return: list of outbound neighbours
        """
        return self.__graph.parse_outbound_edges(vertex)

    def get_inbound_neighbours(self, vertex):
        """
        Return the inbound neighbours of a vertex
        :param vertex:
        :return: list of inbound neighbours
        """
        return self.__graph.parse_inbound_edges(vertex)

    def get_edge_cost(self, start_vertex, end_vertex):
        """
        Return the cost of an edge
        :param start_vertex: starting vertex
        :param end_vertex: ending vertex
        :return: cost of the edge
        """
        return self.__graph.get_cost_of_edge(start_vertex, end_vertex)

    def set_edge_cost(self, start_vertex, end_vertex, cost):
        """
        Set the cost of an edge
        :param start_vertex: starting vertex
        :param end_vertex: ending vertex
        :param cost: cost of the edge
        """
        self.__graph.set_cost_of_edge(start_vertex, end_vertex, cost)

    def write_to_file(self, filename):
        """
        Write the graph to a file
        :param filename: name of the file
        """
        self.__graph.write_graph_to_file(filename)

    def read_from_file(self, filename):
        """
        Read the graph from a file
        :param filename: name of file
        """
        self.__graph = DirectedGraph()
        self.__graph.read_graph_from_file(filename)

    def create_random_graph(self, vertices, edges):
        """
        Create a random graph
        If the number of edges is higher than the number of vertices * (vertices - 1), then the graph is not so random anymore
        as not to wait for a long time to generate the graph
        :param vertices: number of vertices
        :param edges: number of edges
        """
        self.__graph = DirectedGraph.create_random_graph(vertices, edges)

    def shortest_path_using_bfs(self, s, d):
        """
        Finds the shortest path from node s to node d in the graph using BFS
        :return: the path as a sequence of vertices, or None if there is no path
        """
        if s not in self.__graph.parse_vertices() or d not in self.__graph.parse_vertices():
            raise ValueError("Invalid vertices")
        path = shortest_path(self.__graph, s, d)
        return path

    def lowest_cost_walk(self, s, d):
        """
        Finds the lowest cost walk from node s to node d in the graph using backwards Dijkstra
        :return: a tuple with two dictionaries: parent, dist
        """
        if s not in self.__graph.parse_vertices() or d not in self.__graph.parse_vertices():
            raise ValueError("Invalid vertices")
        path = lowest_cost_walk(self.__graph, s, d)
        return path

    def highest_cost_path(self, s, d):
        """
        Finds the highest cost path from node s to node d in the graph if it a DAG
        :return: path or None if not a DAG
        """
        if s not in self.__graph.parse_vertices() or d not in self.__graph.parse_vertices():
            raise ValueError("Invalid vertices")
        path = highest_cost_path(self.__graph, s, d)
        return path

    def nrpaths(self, s, d):
        """
        Finds the highest cost path from node s to node d in the graph if it a DAG
        :return: path or None if not a DAG
        """
        if s not in self.__graph.parse_vertices() or d not in self.__graph.parse_vertices():
            raise ValueError("Invalid vertices")
        path = numberpaths(self.__graph, s, d)
        return path

    def find_ham_cycle(self):
        """
        Find a Hamiltonian cycle in the graph if it exists
        :return: the cycle or None if it does not exist
        """
        cycle = find_ham_cycle(self.__graph)
        return cycle
