# --8<-- [start:ingest_data]
from raphtory import Graph
import pandas as pd

edges_df = pd.read_csv("data/network_traffic_edges.csv")
edges_df["timestamp"] = pd.to_datetime(edges_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

vertices_df = pd.read_csv("data/network_traffic_vertices.csv")
vertices_df["timestamp"] = pd.to_datetime(vertices_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

print("Edge Dataframe:")
print(f"{edges_df}\n")
print("Vertex Dataframe:")
print(f"{vertices_df}\n")

g = Graph.load_from_pandas(
    edges_df=edges_df,
    src="source",
    dst="destination",
    time="timestamp",
    props=["data_size_MB"],
    layer_in_df="transaction_type",
    const_props=["is_encrypted"],
    shared_const_props={"datasource": "data/network_traffic_edges.csv"},
    vertex_df=vertices_df,
    vertex_col="server_id",
    vertex_time_col="timestamp",
    vertex_props=["OS_version", "primary_function", "uptime_days"],
    vertex_const_props=["server_name", "hardware_type"],
    vertex_shared_const_props={"datasource": "data/network_traffic_edges.csv"},
)

# --8<-- [end:ingest_data]


# --8<-- [start:vertex_df]
import raphtory.export as ex

df = ex.to_vertex_df(g) 
print(df)
# --8<-- [end:vertex_df]


# --8<-- [start:edge_df]
import raphtory.export as ex
df = ex.to_edge_df(g) 
print(df)
# --8<-- [end:edge_df]


# --8<-- [start:networkX]
import raphtory.export as ex
networkx_g = ex.to_networkx(g) 
print(networkx_g)
# --8<-- [end:networkX]

# --8<-- [start:pyvis]
import raphtory.export as ex
pyvis_g = ex.to_pyvis(g) 
print(pyvis_g.nodes)
# --8<-- [end:pyvis]