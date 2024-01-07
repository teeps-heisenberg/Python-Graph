from graph import Graph

my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)

my_graph.add_edge(1,2) 
my_graph.add_edge(2,3)
my_graph.add_edge(3,1)  
my_graph.add_edge(3,4)  
my_graph.add_edge(1,4)
my_graph.add_edge(2,4)    


#my_graph.remove_edge(1,2) 

my_graph.remove_vertex(4)

my_graph.print_graph() 