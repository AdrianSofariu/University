import copy
import random


class DirectedGraph:

    def __init__(self):
        """
        Initialize an empty graph
        """
        self.__Nout = dict()  # dictionary with the outbound neighbours of each vertex
        self.__Nin = dict()  # dictionary with the inbound neighbours of each vertex
        self.__costs = dict()  # dictionary with the cost of each edge

    def make_graph(self, nr_vertices):
        """
        Create a graph with a given number of vertices
        :param nr_vertices:
        :return:
        """
        for vertex in range(nr_vertices):
            self.__Nout[vertex] = set()
            self.__Nin[vertex] = set()

    def get_number_of_vertices(self):
        """
        Return the number of vertices in the graph
        :return: number of vertices
        """
        return len(self.__Nin)

    def parse_vertices(self):
        """
        Return an iterable containing the vertices of the graph
        :return: each vertex one by one
        """
        for vertex in self.__Nin:
            yield vertex

    def edge_exists(self, start_vertex, end_vertex):
        """
        Check if an edge exists between two vertices
        :param start_vertex: the start vertex
        :param end_vertex: the end vertex
        :return: true if it exists, false otherwise
        """
        if end_vertex in self.__Nout[start_vertex]:
            return True
        return False

    def in_degree(self, vertex):
        """
        Return the in degree of a vertex
        :param vertex: the vertex
        :return: the in degree of the vertex
        """
        if vertex in self.__Nin:
            return len(self.__Nin[vertex])
        return 0

    def out_degree(self, vertex):
        """
        Return the out degree of a vertex
        :param vertex: the vertex
        :return: the out degree of the vertex
        """
        if vertex in self.__Nout:
            return len(self.__Nout[vertex])
        return 0

    def parse_outbound_edges(self, vertex):
        """
        Return an iterable containing the outbound edges of a vertex
        :param vertex: the vertex
        :return: each outbound edge one by one
        """
        if vertex in self.__Nout:
            for neighbour in self.__Nout[vertex]:
                yield neighbour
        else:
            raise ValueError("Vertex does not exist")

    def parse_inbound_edges(self, vertex):
        """
        Return an iterable containing the inbound edges of a vertex
        :param vertex: the vertex
        :return: each inbound edge one by one
        """
        if vertex in self.__Nin:
            for neighbour in self.__Nin[vertex]:
                yield neighbour
        else:
            raise ValueError("Vertex does not exist")

    def set_cost_of_edge(self, start_vertex, end_vertex, cost):
        """
        Set the cost of an edge
        :param start_vertex: the start vertex
        :param end_vertex: the end vertex
        :param cost: the cost
        """
        self.__costs[(start_vertex, end_vertex)] = cost

    def get_cost_of_edge(self, start_vertex, end_vertex):
        """
        Return the cost of an edge
        :param start_vertex: the start vertex
        :param end_vertex: the end vertex
        :return: cost
        """
        if (start_vertex, end_vertex) in self.__costs:
            return self.__costs[(start_vertex, end_vertex)]
        raise ValueError("Edge does not exist")

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph
        :param vertex: vertex to be added
        """
        if vertex not in self.__Nin:
            self.__Nout[vertex] = set()
            self.__Nin[vertex] = set()
        else:
            raise ValueError("Vertex already exists")

    def remove_vertex(self, vertex):
        """
        Remove a vertex from the graph
        :param vertex: vertex to be removed
        """
        if vertex in self.__Nin:

            # remove all edges containing the vertex and their costs
            for edge in self.__costs:
                if vertex in edge:
                    del self.__costs[edge]

            # remove the vertex from the outbound neighbours of all other vertices
            for start_vertex in self.__Nout:
                if vertex in self.__Nout[start_vertex]:
                    self.__Nout[start_vertex].remove(vertex)
            # remove the vertices own outbound neighbours
            if vertex in self.__Nout:
                del self.__Nout[vertex]

            # remove the vertex from the inbound neighbours of all other vertices
            for end_vertex in self.__Nin:
                if vertex in self.__Nin[end_vertex]:
                    self.__Nin[end_vertex].remove(vertex)
            # remove the vertices own inbound neighbours
            if vertex in self.__Nin:
                del self.__Nin[vertex]
        else:
            raise ValueError("Vertex does not exist")

    def add_edge(self, start_vertex, end_vertex):
        """
        Add an edge to the graph
        :param start_vertex: starting vertex
        :param end_vertex: ending vertex
        """
        if start_vertex not in self.__Nout or end_vertex not in self.__Nin:
            raise ValueError("One or both of the vertices do not exist in the graph")
        if end_vertex in self.__Nout[start_vertex]:
            raise ValueError("Edge already exists")
        self.__Nout[start_vertex].add(end_vertex)
        self.__Nin[end_vertex].add(start_vertex)

    def remove_edge(self, start_vertex, end_vertex):
        """
        Remove an edge from the graph
        :param start_vertex: starting vertex
        :param end_vertex: ending vertex
        """
        if end_vertex in self.__Nout[start_vertex]:
            self.__Nout[start_vertex].remove(end_vertex)
            self.__Nin[end_vertex].remove(start_vertex)
        else:
            raise ValueError("Invalid edge")
        if (start_vertex, end_vertex) in self.__costs:
            del self.__costs[(start_vertex, end_vertex)]

    def __copy__(self):
        """
        Return a copy of the graph
        :return: copy of the graph
        """
        copy_graph = DirectedGraph()
        for vertex in self.__Nout:
            copy_graph.add_vertex(vertex)
            copy_graph.__Nin[vertex] = copy.deepcopy(self.__Nin[vertex])
            copy_graph.__Nout[vertex] = copy.deepcopy(self.__Nout[vertex])
        for edge in self.__costs:
            copy_graph.__costs = copy.deepcopy(self.__costs)
        return copy_graph

    def read_graph_from_file(self, filename):
        """
        Read the graph from a file
        The first line contains the number of vertices and the number of edges
        :param filename: name of the file where the graph is stored
        """
        with open(filename, "r") as file:
            try:
                line = file.readline().strip()
                words = line.split()
                number_of_vertices = int(words[0])
                number_of_edges = int(words[1])
                for i in range(number_of_vertices):
                    self.add_vertex(i)
                for i in range(number_of_edges):
                    line = file.readline().strip()
                    words = line.split()
                    start_vertex = int(words[0])
                    end_vertex = int(words[1])
                    self.add_edge(start_vertex, end_vertex)
                    if len(words) == 3:
                        cost = int(words[2])
                        self.set_cost_of_edge(start_vertex, end_vertex, int(words[2]))
            except (ValueError, IndexError):
                raise ValueError("Something went wrong. Check the file and try again")

    def write_graph_to_file(self, filename):
        """
        Write the graph to a file
        :param filename: name of the file where the graph will be stored
        """
        nr_edges = 0
        for vertex in self.__Nin:
            nr_edges += len(self.__Nin[vertex])
        with open(filename, "w") as file:
            file.write(str(len(self.__Nin)) + " " + str(nr_edges) + "\n")
            for vertex in self.__Nout:
                for neighbour in self.__Nout[vertex]:
                    if (vertex, neighbour) in self.__costs:
                        file.write(str(vertex) + " " + str(neighbour) + " " + str(self.get_cost_of_edge(vertex, neighbour)) + "\n")
                    else:
                        file.write(str(vertex) + " " + str(neighbour) + "\n")

    @staticmethod
    def create_random_graph(vertices, edges):
        """
        Create a random graph and return it
        If the number of edges is higher than the number of vertices * (vertices - 1), then the graph is not so random anymore
        as not to wait for a long time to generate the graph
        :param vertices: number of vertices
        :param edges: number of edges
        """
        vertex_list = []
        counter = 0
        graph = DirectedGraph()
        graph.make_graph(vertices)
        for vertex in graph.parse_vertices():
            vertex_list.append(vertex)
        if edges > vertices * (vertices - 1):
            possible_edges = set()
            for v in vertex_list:
                for w in vertex_list:
                    cost = random.randint(1, 10)
                    possible_edges.add((v, w, cost))
            while counter != edges:
                edge = random.choice(list(possible_edges))
                graph.add_edge(edge[0], edge[1])
                graph.set_cost_of_edge(edge[0], edge[1], edge[2])
                possible_edges.remove(edge)
                counter += 1
        else:
            while counter != edges:
                start_vertex = random.choice(vertex_list)
                end_vertex = random.choice(vertex_list)
                if not graph.edge_exists(start_vertex, end_vertex):
                    graph.add_edge(start_vertex, end_vertex)
                    graph.set_cost_of_edge(start_vertex, end_vertex, random.randint(1, 10))
                    counter += 1
        return graph

    @staticmethod
    def test_copy():
        """
        Test the copy method
        :return:
        """
        graph = DirectedGraph()
        graph.make_graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.set_cost_of_edge(0, 1, 5)
        graph.set_cost_of_edge(1, 2, 6)
        copy_graph = graph.__copy__()
        assert graph.get_number_of_vertices() == copy_graph.get_number_of_vertices()
        for vertex in graph.parse_vertices():
            assert copy_graph.in_degree(vertex) == graph.in_degree(vertex)
            assert copy_graph.out_degree(vertex) == graph.out_degree(vertex)
            for neighbour in graph.parse_outbound_edges(vertex):
                assert copy_graph.edge_exists(vertex, neighbour) is True
                assert copy_graph.get_cost_of_edge(vertex, neighbour) == graph.get_cost_of_edge(vertex, neighbour)

        graph.add_vertex(3)
        assert copy_graph.get_number_of_vertices() != graph.get_number_of_vertices()
