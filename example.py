from main import read_graphs

input_file = "../2019/sample/amr/wsj_with_int_gold.mrp"

graphs, _ = read_graphs(open(input_file, "r"), format="mrp")

for graph in graphs:
    print([(node.id, node.label) for node in graph.intermediate_gold])
    print(graph.gold_indexes)
    print("-------------------")
