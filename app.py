class WeightedGraph:
    """A class that implements a Weighted graph data structure
    """
    def __init__(self) -> None:
        self.graph ={}
                
    def vertex(self, vertex):
        """a function that adds vertices to the graph

        Args:
            vertex (_type_): _description_
        """
        if vertex not in self.graph:
            self.graph[vertex]= []
            
    def add_edges(self, first, second, weight):
        """a function that adds edges to the graph

        Args:
            first (VAR): description of first vertex
            second (VAR): description of second vertex 
            weight (NUMBER): a number  indicating the distance from one vertex to the other
        """
        if first in self.graph and second in self.graph:
            self.graph[first].append((second, weight))
            self.graph[second].append((first, weight))


the_graph = WeightedGraph()

the_graph.vertex("Salima")
the_graph.vertex("Ntchisi")
the_graph.vertex("Kasungu")
the_graph.vertex("Dowa")
the_graph.vertex("mchinji")
the_graph.vertex("Lilongwe")
the_graph.vertex("Dedza")
the_graph.vertex("Ntcheu")
the_graph.vertex("Nkhotakota")
the_graph.add_edges("Nkhotakota", "Salima", 112)
the_graph.add_edges("Nkhotakota", "Ntchisi", 66)
the_graph.add_edges("Ntchisi", "Dowa", 38)
the_graph.add_edges("Ntchisi", "Kasungu", 66)
the_graph.add_edges("Kasungu", "Dowa", 117)
the_graph.add_edges("Kasungu", "Mchinji", 141)
the_graph.add_edges("Mchinji", "Lilongwe", 109)
the_graph.add_edges("Lilongwe", "Dowa", 55)
the_graph.add_edges("Lilongwe", "Dedza", 92)
the_graph.add_edges("Dedza", "Ntcheu", 74)
the_graph.add_edges("Dedza", "Salima", 96)
the_graph.add_edges("Dowa", "Salima", 67)
