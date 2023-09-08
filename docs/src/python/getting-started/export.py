# --8<-- [start:ingest_data]
from raphtory import Graph
import pandas as pd

server_edges_df = pd.read_csv("data/network_traffic_edges.csv")
server_edges_df["timestamp"] = pd.to_datetime(server_edges_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

server_vertices_df = pd.read_csv("data/network_traffic_vertices.csv")
server_vertices_df["timestamp"] = pd.to_datetime(server_vertices_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

print("Network Traffic Edges:")
print(f"{server_edges_df}\n")
print("Network Traffic Servers:")
print(f"{server_vertices_df}\n")

traffic_graph = Graph.load_from_pandas(
    edges_df=server_edges_df,
    src="source",
    dst="destination",
    time="timestamp",
    props=["data_size_MB"],
    layer_in_df="transaction_type",
    const_props=["is_encrypted"],
    shared_const_props={"datasource": "data/network_traffic_edges.csv"},
    vertex_df=server_vertices_df,
    vertex_col="server_id",
    vertex_time_col="timestamp",
    vertex_props=["OS_version", "primary_function", "uptime_days"],
    vertex_const_props=["server_name", "hardware_type"],
    vertex_shared_const_props={"datasource": "data/network_traffic_edges.csv"},
)

monkey_edges_df = pd.read_csv("data/OBS_data.txt",sep="\t",header=0, usecols=[0,1,2,3,4], parse_dates=[0])
monkey_edges_df["DateTime"] = pd.to_datetime(monkey_edges_df["DateTime"]).astype(
    "datetime64[ms]"
)
monkey_edges_df.dropna(axis=0,inplace=True)
monkey_edges_df['Weight'] = monkey_edges_df['Category'].apply(lambda c: 1 if (c=='Affiliative') else (-1 if (c=='Agonistic') else 0))

print("Monkey Interactions:")
print(f"{monkey_edges_df}\n")

monkey_graph = Graph()
monkey_graph.load_edges_from_pandas(edge_df = monkey_edges_df, src_col="Actor", dst_col="Recipient", time_col="DateTime", layer_in_df="Behavior",props=["Weight"])


# --8<-- [end:ingest_data]


# --8<-- [start:vertex_df]
import raphtory.export as ex

df = ex.to_vertex_df(traffic_graph)
print("Dataframe with full history:") 
print(f"{df}\n")
print("The properties of ServerA:")
print(f"{df[df['id'] == 'ServerA'].properties.iloc[0]}\n")

print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")

df = ex.to_vertex_df(traffic_graph,include_update_history=False,include_property_histories=False)
print("Dataframe with no history:") 
print(f"{df}\n")
print("The properties of ServerA:")
print(f"{df[df['id'] == 'ServerA'].properties.iloc[0]}\n")

# --8<-- [end:vertex_df]


# --8<-- [start:edge_df]
import raphtory.export as ex

subgraph = monkey_graph.subgraph(["ANGELE","FELIPE"])
df = ex.to_edge_df(subgraph)
print("Interactions between Angele and Felipe:") 
print(f"{df}\n")

grunting_graph = subgraph.layer("Grunting-Lipsmacking")
df = ex.to_edge_df(grunting_graph,explode_edges=True,include_property_histories=False) 
print("Exploding the grunting-Lipsmacking layer")
print(df)
# --8<-- [end:edge_df]


# --8<-- [start:networkX]
import raphtory.export as ex
nx_g = ex.to_networkx(traffic_graph) 

print("Networkx graph and the full property history of ServerA:")
print(nx_g)
print(nx_g.nodes["ServerA"])
print()

nx_g = ex.to_networkx(traffic_graph,include_property_histories=False,include_update_history=False) 

print("Only the latest properties of ServerA:")
print(nx_g.nodes["ServerA"])

# --8<-- [end:networkX]

# --8<-- [start:networkX_vis]
# mkdocs: render
import raphtory.export as ex
import matplotlib.pyplot as plt
import networkx as nx

from raphtory import Graph
import pandas as pd

server_edges_df = pd.read_csv("data/network_traffic_edges.csv")
server_edges_df["timestamp"] = pd.to_datetime(server_edges_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

traffic_graph = Graph.load_from_pandas(
    edges_df=server_edges_df,
    src="source",
    dst="destination",
    time="timestamp"
)

nx_g = ex.to_networkx(traffic_graph) 
nx.draw(nx_g, with_labels=True, node_color='lightblue', edge_color='gray')

# --8<-- [end:networkX_vis]


# --8<-- [start:pyvis]
import raphtory.export as ex
pyvis_g = ex.to_pyvis(g) 
print(pyvis_g.nodes)
# --8<-- [end:pyvis]


