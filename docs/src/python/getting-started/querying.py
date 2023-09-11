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
number_of_edges= g.num_edges()
total_interactions = g.num_temporal_edges()
unique_layers = g.get_unique_layers()

print("Number of vertices (Baboons):",number_of_vertices)
print("Number of unique edges (src,dst,layer):",number_of_edges)
print("Total interactions (edge updates):",total_interactions)
print("Unique layers:",unique_layers,"\n")


print("Stats on the graphs time range:")

earliest_datetime = g.earliest_date_time()
latest_datetime = g.latest_date_time()
earliest_epoch = g.earliest_time()
latest_epoch = g.latest_time()

print("Earliest datetime:",earliest_datetime)
print("Latest datetime:",latest_datetime)
print("Earliest time (Unix Epoch):",earliest_epoch)
print("Latest time (Unix Epoch):",latest_epoch)
# --8<-- [end:graph_metrics]

# --8<-- [start:graph_functions]
print("Checking if specific vertices and edges are in the graph:")
if(g.has_vertex("LOME")):
    print("Lomme is in the graph")
if(g.has_edge("LOME","NEKKE","Playing with")):
    print("Lomme has played with Nekke \n")

print("Getting individual vertices and edges:")  
print(g.vertex("LOME"))  
print(g.edge("LOME","NEKKE"),"\n")

print("Getting iterators over all vertices and edges:")
print(g.vertices())
print(g.edges())
# --8<-- [end:graph_functions]


# --8<-- [start:vertex_metrics]
v = g.vertex("FELIPE")
print(f"{v.name()}'s first interaction was at {v.earliest_date_time()} and their last interaction was at {v.latest_date_time()}\n")
print(f"{v.name()} had interactions at the following times: {v.history()}\n")

# --8<-- [end:vertex_metrics]

# --8<-- [start:vertex_neighbours]
v = g.vertex("FELIPE")
v_name = v.name()
in_degree = v.in_degree()
out_degree = v.out_degree()
in_edges= v.in_edges()
neighbours = v.neighbours()
neighbour_names = v.neighbours().name().collect()

print(
    f"{v_name} has {in_degree} incoming interactions and {out_degree} outgoing interactions.\n"
)
print(in_edges)
print(neighbours,"\n")
print(f"{v_name} interacted with the following baboons {neighbour_names}")
# --8<-- [end:vertex_neighbours]

# --8<-- [start:friendship]
e = g.edge("FELIPE", "MAKO")
e_reversed = g.edge("MAKO", "FELIPE")
print(e)
print(e_reversed)
print("Interaction times from FELIPE to MAKO: ")
print(e.history())
# --8<-- [end:frienship]

# --8<-- [start:exploded_edge]

neighbours_weighted = list(
    zip(
        v.out_edges().dst().name(),
        map(
            lambda u: sum(g.edge(v, u).explode().properties["Weight"]),
            v.out_edges().dst(),
        ),
    )
)
print(
    f"Felipe's favourite baboons in descending order are {sorted(neighbours_weighted,key= lambda v: v[1],reverse=True)}"
)

# --8<-- [end:exploded_edge]


#functions for graph views:
#g.end()
#g.end_date_time()
#g.start()
#g.start_date_time()
#g.window_size()