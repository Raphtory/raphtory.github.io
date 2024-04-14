# --8<-- [start:ingest_data]
from raphtory import Graph
import pandas as pd

server_edges_df = pd.read_csv("data/network_traffic_edges.csv")
server_edges_df["timestamp"] = pd.to_datetime(server_edges_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

server_nodes_df = pd.read_csv("data/network_traffic_nodes.csv")
server_nodes_df["timestamp"] = pd.to_datetime(server_nodes_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

print("Network Traffic Edges:")
print(f"{server_edges_df}\n")
print("Network Traffic Servers:")
print(f"{server_nodes_df}\n")

traffic_graph = Graph.load_from_pandas(
    edge_df=server_edges_df,
    edge_src="source",
    edge_dst="destination",
    edge_time="timestamp",
    edge_properties=["data_size_MB"],
    edge_layer="transaction_type",
    edge_const_properties=["is_encrypted"],
    edge_shared_const_properties={"datasource": "data/network_traffic_edges.csv"},
    node_df=server_nodes_df,
    node_id="server_id",
    node_time="timestamp",
    node_properties=["OS_version", "primary_function", "uptime_days"],
    node_const_properties=["server_name", "hardware_type"],
    node_shared_const_properties={"datasource": "data/network_traffic_edges.csv"},
)

monkey_edges_df = pd.read_csv(
    "data/OBS_data.txt", sep="\t", header=0, usecols=[0, 1, 2, 3, 4], parse_dates=[0]
)
monkey_edges_df["DateTime"] = pd.to_datetime(monkey_edges_df["DateTime"]).astype(
    "datetime64[ms]"
)
monkey_edges_df.dropna(axis=0, inplace=True)
monkey_edges_df["Weight"] = monkey_edges_df["Category"].apply(
    lambda c: 1 if (c == "Affiliative") else (-1 if (c == "Agonistic") else 0)
)

print("Monkey Interactions:")
print(f"{monkey_edges_df}\n")

monkey_graph = Graph()
monkey_graph.load_edges_from_pandas(
    df=monkey_edges_df,
    src="Actor",
    dst="Recipient",
    time="DateTime",
    layer="Behavior",
    properties=["Weight"],
)


# --8<-- [end:ingest_data]


# --8<-- [start:node_df]

df = traffic_graph.nodes.to_df()
print("Dataframe with full history:")
print(f"{df}\n")
print("The properties of ServerA:")
#TODO FIX THIS AND BELOW
#print(f"{df[df['name'] == 'ServerA'].properties.iloc[0]}\n")

df = traffic_graph.nodes.to_df()
print("Dataframe with no history:")
print(f"{df}\n")
print("The properties of ServerA:")
#print(f"{df[df['name'] == 'ServerA'].properties.iloc[0]}\n")

# --8<-- [end:node_df]


# --8<-- [start:edge_df]

subgraph = monkey_graph.subgraph(["ANGELE", "FELIPE"])
df = subgraph.edges.to_df()
print("Interactions between Angele and Felipe:")
print(f"{df}\n")

grunting_graph = subgraph.layer("Grunting-Lipsmacking")
df = grunting_graph.edges.to_df(explode=True)
print("Exploding the grunting-Lipsmacking layer")
print(df)
# --8<-- [end:edge_df]


# --8<-- [start:networkX]
nx_g = traffic_graph.to_networkx()

print("Networkx graph and the full property history of ServerA:")
print(nx_g)
print(nx_g.nodes["ServerA"])
print()

nx_g = traffic_graph.to_networkx()

print("Only the latest properties of ServerA:")
print(nx_g.nodes["ServerA"])

# --8<-- [end:networkX]

# --8<-- [start:networkX_vis]
# mkdocs: render
import matplotlib.pyplot as plt
import networkx as nx

from raphtory import Graph
import pandas as pd

server_edges_df = pd.read_csv("data/network_traffic_edges.csv")
server_edges_df["timestamp"] = pd.to_datetime(server_edges_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

traffic_graph = Graph.load_from_pandas(
    edge_df=server_edges_df,
    edge_src="source",
    edge_dst="destination",
    edge_time="timestamp",
)

nx_g = traffic_graph.to_networkx()
nx.draw(nx_g, with_labels=True, node_color="lightblue", edge_color="gray")

# --8<-- [end:networkX_vis]


# --8<-- [start:pyvis]
import json

pyvis_g = traffic_graph.to_pyvis(
    edge_weight="data_size_MB", edge_color="#8e9b9e", directed=True
)

options = {
    "edges": {
        "scaling": {
            "min": 1,
            "max": 10,
        },
    },
    "physics": {
        "barnesHut": {
            "gravitationalConstant": -30000,
            "centralGravity": 0.3,
            "springLength": 100,
            "springConstant": 0.05,
        },
        "maxVelocity": 50,
        "timestep": 0.5,
    },
}

pyvis_g.set_options(json.dumps(options))

pyvis_g.show("nx.html")
# --8<-- [end:pyvis]
