import yedextended as yed

# Reading of graphml file into python objects # Under Construction
graph1 = yed.Graph().from_existing_graph("examples/test.graphml")
graph1.persist_graph("abc.graphml", overwrite=True).open_with_yed()

# graph1 = yed.Graph().from_existing_graph("examples/test.graphml")
# print(graph1.stringify_graph())