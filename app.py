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

