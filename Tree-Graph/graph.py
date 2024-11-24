class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    def add_edge(self, source, target):
        self.vertices[source].append(target)
    

class WeightedGraph(Graph):        
    def add_edge(self, source, target, weight):
        # Set the weight
        self.vertices[source].append([target, weight])

if __name__ == '__main__':
    my_graph = WeightedGraph()
    # Create the vertices
    my_graph.add_vertex('Paris')
    my_graph.add_vertex('Toulouse')
    my_graph.add_vertex('Biarritz')

    # Create the edges
    my_graph.add_edge('Paris', 'Toulouse', 678)
    my_graph.add_edge('Toulouse', 'Biarritz', 312)
    my_graph.add_edge('Biarritz', 'Paris', 783)
    print(my_graph.vertices)