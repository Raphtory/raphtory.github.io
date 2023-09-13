# --8<-- [start:read_data]
import pandas as pd

edges_df = pd.read_csv(
    "data/OBS_data.txt", sep="\t", header=0, usecols=[0, 1, 2, 3, 4], parse_dates=[0]
)
edges_df["DateTime"] = pd.to_datetime(edges_df["DateTime"]).astype("datetime64[ms]")
edges_df.dropna(axis=0, inplace=True)
edges_df["Weight"] = edges_df["Category"].apply(
    lambda c: 1 if (c == "Affiliative") else (-1 if (c == "Agonistic") else 0)
)
print(edges_df.head())
# --8<-- [end:read_data]

# --8<-- [start:new_graph]
import raphtory as rp

g = rp.Graph()
g.load_edges_from_pandas(
    edge_df=edges_df,
    src_col="Actor",
    dst_col="Recipient",
    time_col="DateTime",
    layer_in_df="Behavior",
    props=["Weight"],
)
print(g)
# --8<-- [end:new_graph]

# --8<-- [start:graph_metrics]

print("Stats on the graph structure:")

number_of_vertices = g.num_vertices()
number_of_edges = g.num_edges()
total_interactions = g.num_temporal_edges()
unique_layers = g.get_unique_layers()

print("Number of vertices (Baboons):", number_of_vertices)
print("Number of unique edges (src,dst,layer):", number_of_edges)
print("Total interactions (edge updates):", total_interactions)
print("Unique layers:", unique_layers, "\n")


print("Stats on the graphs time range:")

earliest_datetime = g.earliest_date_time()
latest_datetime = g.latest_date_time()
earliest_epoch = g.earliest_time()
latest_epoch = g.latest_time()

print("Earliest datetime:", earliest_datetime)
print("Latest datetime:", latest_datetime)
print("Earliest time (Unix Epoch):", earliest_epoch)
print("Latest time (Unix Epoch):", latest_epoch)
# --8<-- [end:graph_metrics]

# --8<-- [start:graph_functions]
print("Checking if specific vertices and edges are in the graph:")
if g.has_vertex("LOME"):
    print("Lomme is in the graph")
if g.has_edge("LOME", "NEKKE", "Playing with"):
    print("Lomme has played with Nekke \n")

print("Getting individual vertices and edges:")
print(g.vertex("LOME"))
print(g.edge("LOME", "NEKKE"), "\n")

print("Getting iterators over all vertices and edges:")
print(g.vertices())
print(g.edges())
# --8<-- [end:graph_functions]


# --8<-- [start:vertex_metrics]
v = g.vertex("FELIPE")
print(
    f"{v.name()}'s first interaction was at {v.earliest_date_time()} and their last interaction was at {v.latest_date_time()}\n"
)
print(f"{v.name()} had interactions at the following times: {v.history()}\n")

# --8<-- [end:vertex_metrics]

# --8<-- [start:vertex_neighbours]
v = g.vertex("FELIPE")
v_name = v.name()
in_degree = v.in_degree()
out_degree = v.out_degree()
in_edges = v.in_edges()
neighbours = v.neighbours()
neighbour_names = v.neighbours().name().collect()

print(
    f"{v_name} has {in_degree} incoming interactions and {out_degree} outgoing interactions.\n"
)
print(in_edges)
print(neighbours, "\n")
print(f"{v_name} interacted with the following baboons {neighbour_names}")
# --8<-- [end:vertex_neighbours]

# --8<-- [start:edge_history]
e = g.edge("FELIPE", "MAKO")
e_reversed = g.edge("MAKO", "FELIPE")
print(
    f"The edge from {e.src().name()} to {e.dst().name()} covers the following layers: {e.layer_names()}"
)
print(
    f"and has updates between {e.earliest_date_time()} and {e.latest_date_time()} at the following times: {e.history()}\n"
)

print(
    f"The edge from {e_reversed.src().name()} to {e_reversed.dst().name()} covers the following layers: {e_reversed.layer_names()}"
)
print(
    f"and has updates between {e_reversed.earliest_date_time()} and {e_reversed.latest_date_time()} at the following times: {e_reversed.history()}"
)
# --8<-- [end:edge_history]

# --8<-- [start:edge_explode_layer]
print("Update history per layer:")
for e in g.edge("FELIPE", "MAKO").explode_layers():
    print(
        f"{e.src().name()} interacted with {e.dst().name()} with the following behaviour '{e.layer_name()}' at this times: {e.history()}"
    )

print()
print("Individual updates as edges:")
for e in g.edge("FELIPE", "MAKO").explode():
    print(
        f"At {e.date_time()} {e.src().name()} interacted with {e.dst().name()} in the following manner: '{e.layer_name()}'"
    )

print()
print("Individual updates for 'Touching' and 'Carrying:")
for e in g.edge("FELIPE", "MAKO").layers(["Touching", "Carrying"]).explode():
    print(
        f"At {e.date_time()} {e.src().name()} interacted with {e.dst().name()} in the following manner: '{e.layer_name()}'"
    )
    # --8<-- [end:edge_explode_layer]

# --8<-- [start:properties]
from raphtory import Graph

property_g = Graph()
# Create the vertex and add a variety of temporal properties
v = property_g.add_vertex(
    timestamp=1,
    id="User",
    properties={"count": 1, "greeting": "hi", "encrypted": True},
)
property_g.add_vertex(
    timestamp=2,
    id="User",
    properties={"count": 2, "balance": 0.6, "encrypted": False},
)
property_g.add_vertex(
    timestamp=3,
    id="User",
    properties={"balance": 0.9, "greeting": "hello", "encrypted": True},
)
# Add some constant properties
v.add_constant_properties(
    properties={
        "inner data": {"name": "bob", "value list": [1, 2, 3]},
        "favourite greetings": ["hi", "hello", "howdy"],
    },
)
# Call all of the functions on the properties object
properties = v.properties
print("Property keys:", properties.keys())
print("Property values:", properties.values())
print("Property tuples:", properties.items())
print("Latest value of balance:", properties.get("balance"))
print("Property keys:", properties.as_dict(), "\n")

# Access the keys of the constant and temporal properties individually
constant_properties = properties.constant
temporal_properties = properties.temporal
print("Constant property keys:", constant_properties.keys())
print("Constant property keys:", temporal_properties.keys())
# --8<-- [end:properties]


# --8<-- [start:temporal_properties]
properties = g.edge("FELIPE", "MAKO").properties.temporal
print("Property keys:", properties.keys())
weight_prop = properties.get("Weight")
print("Weight property history:", weight_prop.items())
print("Average interaction weight:", weight_prop.mean())
print("Total interactions:", weight_prop.count())
print("Total interaction weight:", weight_prop.sum())

# --8<-- [end:temporal_properties]

# --8<-- [start:function_chains]
vertex_names = g.vertices().name()
two_hop_neighbours = g.vertices().neighbours().neighbours().name().collect()
combined = zip(vertex_names, two_hop_neighbours)
for name, two_hop_neighbour in combined:
    print(f"{name} has the following two hop neighbours {two_hop_neighbour}")

# --8<-- [end:function_chains]


# --8<-- [start:friendship]
v = g.vertex("FELIPE")
neighbours_weighted = list(
    zip(
        v.out_edges().dst().name(),
        v.out_edges().properties.temporal.get("Weight").values().sum(),
    )
)
sorted_weights = sorted(neighbours_weighted, key=lambda v: v[1], reverse=True)
print(f"Felipe's favourite baboons in descending order are {sorted_weights}")

annoying_monkeys = list(
    zip(
        g.vertices.name(),
        g.vertices()
        .in_edges()
        .properties.temporal.get("Weight")
        .values()
        .sum() #sum the weights within each edge
        .mean() #average the summed weights for each monkey
        .collect(),
    )
)
most_annoying = sorted(annoying_monkeys,key= lambda v: v[1])[0]
print(f"{most_annoying[0]} is the most annoying monkey with an average score of {most_annoying[1]}")

# --8<-- [end:friendship]

# --8<-- [start:at]
v = g.vertex("LOME")
print(f"Across the full dataset {v.name()} interacted with {v.degree()} other monkeys.")
v_at = g.vertex("LOME").at("2019-06-14 9:07:31")
print(f"Between {v_at.start_date_time()} and {v_at.end_date_time()}, {v_at.name()} interacted with {v_at.degree()} other monkeys.")
v_at_2 = g.at(1560428239000).vertex("LOME") # 13/06/2019 12:17:19 as epoch
print(f"Between {v_at_2.start_date_time()} and {v_at_2.end_date_time()}, {v_at_2.name()} interacted with {v_at_2.degree()} other monkeys.")

print(f"Window start: {v_at_2.start_date_time()}, First update: {v_at_2.earliest_date_time()}, Last update: {v_at_2.latest_date_time()}, Window End: {v_at_2.end_date_time()}")

# --8<-- [end:at]

# --8<-- [start:window]
from datetime import datetime
start_day = datetime.strptime("2019-06-13", '%Y-%m-%d')
end_day = datetime.strptime("2019-06-14", '%Y-%m-%d')
e = g.edge("LOME","NEKKE")
print(f"Across the full dataset {e.src().name()} interacted with {e.dst().name()} {len(e.history())} times")
e = e.window(start_day,end_day)
print(f"Between {v_at_2.start_date_time()} and {v_at_2.end_date_time()}, {e.src().name()} interacted with {e.dst().name()} {len(e.history())} times")
print(f"Window start: {e.start_date_time()}, First update: {e.earliest_date_time()}, Last update: {e.latest_date_time()}, Window End: {e.end_date_time()}")

# --8<-- [end:window]

# --8<-- [start:taster]

# --8<-- [end:taster]
