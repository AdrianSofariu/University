from service.graph_service import Service


class UI:

    def __init__(self, service: Service):
        self._service = service

    @staticmethod
    def print_menu():
        print("------------------------------------------------")
        print("1. Add vertex")
        print("2. Remove vertex")
        print("3. Add edge")
        print("4. Remove edge")
        print("5. Initialize graph with n vertices")
        print("6. Get number of vertices")
        print("7. Get vertices")
        print("8. Get in degree")
        print("9. Get out degree")
        print("10. Get outbound edges")
        print("11. Get inbound edges")
        print("12. Get cost of edge")
        print("13. Set cost of edge")
        print("14. Search edge")
        print("15. Read graph from file")
        print("16. Write graph to file")
        print("17. Create random graph")
        print("18. Shortest path")
        print("19. Lowest cost walk")
        print("20. Highest cost path in a dag")
        print("21. Hamiltonian cycle in an undirected graph")
        print("0. Exit")
        print("------------------------------------------------")

    def run(self):
        while True:
            self.print_menu()
            try:
                command = input("Enter command: ")
                if command == "1":
                    self.add_vertex_ui()
                elif command == "2":
                    self.remove_vertex_ui()
                elif command == "3":
                    self.add_edge_ui()
                elif command == "4":
                    self.remove_edge_ui()
                elif command == "5":
                    self.init_graph_with_n_vertices_ui()
                elif command == "6":
                    self.number_of_vertices_ui()
                elif command == "7":
                    self.parse_vertices_ui()
                elif command == "8":
                    self.in_degree_ui()
                elif command == "9":
                    self.out_degree_ui()
                elif command == "10":
                    self.parse_outbound_neighbours_ui()
                elif command == "11":
                    self.parse_inbound_neighbours_ui()
                elif command == "12":
                    self.get_cost_of_edge_ui()
                elif command == "13":
                    self.set_cost_of_edge_ui()
                elif command == "14":
                    self.search_edge_ui()
                elif command == "15":
                    self.read_graph_from_file_ui()
                elif command == "16":
                    self.write_graph_to_file_ui()
                elif command == "17":
                    self.create_random_graph_ui()
                elif command == "18":
                    self.shortest_path_ui()
                elif command == "19":
                    self.lowest_cost_walk_ui()
                elif command == "20":
                    self.highest_cost_path_ui()
                elif command == "21":
                    self.ham_cycle_ui()
                elif command == "22":
                    self.nrpaths_ui()
                elif command == "0":
                    break
            except (ValueError, IndexError) as e:
                print(e)

    def add_vertex_ui(self):
        """
        Add vertex UI
        :return:
        """
        vertex = int(input("Enter vertex: "))
        self._service.add_vertex(vertex)

    def remove_vertex_ui(self):
        """
        Remove vertex UI
        :return:
        """
        vertex = int(input("Enter vertex: "))
        self._service.remove_vertex(vertex)

    def add_edge_ui(self):
        """
        Add edge UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        self._service.add_edge(start_vertex, end_vertex)

    def remove_edge_ui(self):
        """
        Remove edge UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        self._service.remove_edge(start_vertex, end_vertex)

    def init_graph_with_n_vertices_ui(self):
        """
        Initialize graph with n vertices UI
        :return:
        """
        n = int(input("Enter number of vertices: "))
        self._service.init_graph_with_n_vertices(n)

    def number_of_vertices_ui(self):
        """
        Get number of vertices UI
        :return:
        """
        print("Nr. vertices: " + str(self._service.get_number_of_vertices()))

    def parse_vertices_ui(self):
        """
        Parse vertices UI
        :return:
        """
        print("Parsing vertices:")
        for vertex in self._service.get_vertices():
            print(vertex)

    def in_degree_ui(self):
        """
        Get in degree UI
        :return:
        """
        vertex = int(input("Enter vertex: "))
        print("In degree is: " + str(self._service.get_in_degree(vertex)))

    def out_degree_ui(self):
        """
        Get out degree UI
        :return:
        """
        vertex = int(input("Enter vertex: "))
        print("Out degree is: " + str(self._service.get_out_degree(vertex)))

    def parse_inbound_neighbours_ui(self):
        """
        Parse inbound neighbours UI
        :return:
        """
        vertex = int(input("Enter vertex: "))
        print("Inbound neighbours are: ")
        for neighbour in self._service.get_inbound_neighbours(vertex):
            print(neighbour)

    def parse_outbound_neighbours_ui(self):
        """
        Parse outbound neighbours UI
        :return:
        """
        vertex = int(input("Enter vertex: "))
        print("Outbound neighbours are: ")
        for neighbour in self._service.get_outbound_neighbours(vertex):
            print(neighbour)

    def set_cost_of_edge_ui(self):
        """
        Set cost of edge UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        cost = int(input("Enter cost: "))
        self._service.set_edge_cost(start_vertex, end_vertex, cost)

    def get_cost_of_edge_ui(self):
        """
        Get cost of edge UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        print("Cost of edge is: " + str(self._service.get_edge_cost(start_vertex, end_vertex)))

    def search_edge_ui(self):
        """
        Search edge UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        exists = self._service.search_edge(start_vertex, end_vertex)
        if exists:
            print("Edge exists")
        else:
            print("Edge does not exist")

    def read_graph_from_file_ui(self):
        """
        Read graph from file UI
        :return:
        """
        filename = input("Enter filename: ")
        self._service.read_from_file(filename)

    def write_graph_to_file_ui(self):
        """
        Write graph to file UI
        :return:
        """
        filename = input("Enter filename: ")
        self._service.write_to_file(filename)

    def create_random_graph_ui(self):
        """
        Create random graph UI
        :return:
        """
        n = int(input("Enter number of vertices: "))
        m = int(input("Enter number of edges: "))
        self._service.create_random_graph(n, m)

    def shortest_path_ui(self):
        """
        Shortest path UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        path = self._service.shortest_path_using_bfs(start_vertex, end_vertex)
        if path is None:
            print("No path")
        else:
            print("Path is: ")
            for vertex in path:
                print(vertex, end=" ")
            print(end="\n")

    def lowest_cost_walk_ui(self):
        """
        Lowest cost walk UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        walk, cost = self._service.lowest_cost_walk(start_vertex, end_vertex)
        if walk is None:
            print("No walk")
        else:
            print("Walk is: ")
            for vertex in walk:
                print(vertex, end=" ")
            print(end="\n")
            print("Cost is: " + str(cost))

    def highest_cost_path_ui(self):
        """
        Highest cost path in a DAG UI
        :return:
        """
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        path = self._service.highest_cost_path(start_vertex, end_vertex)
        if path is None:
            print("No path")
        else:
            print("Path is: ")
            for vertex in path:
                print(vertex, end=" ")
            print(end="\n")

    def ham_cycle_ui(self):
        """
        Hamiltonian cycle in an undirected graph UI
        :return:
        """
        cycle = self._service.find_ham_cycle()
        if cycle is None:
            print("No cycle")
        else:
            print("Cycle is: ")
            for vertex in cycle:
                print(vertex, end=" ")
            print(cycle[0], end=" ")
            print(end="\n")

    def nrpaths_ui(self):
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        path = self._service.nrpaths(start_vertex, end_vertex)
        print(path)
