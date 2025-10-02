from domain.graph import DirectedGraph
from service.graph_service import Service
from ui.ui import UI


if __name__ == '__main__':
    DirectedGraph.test_copy()
    service = Service()
    ui = UI(service)
    ui.run()
