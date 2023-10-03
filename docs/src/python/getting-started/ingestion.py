# --8<-- [start:new_graph]
from raphtory import Graph

g = Graph()
print(g)
# --8<-- [end:new_graph]

# --8<-- [start:vertex_add]
from raphtory import Graph

g = Graph()
v = g.add_vertex(timestamp=1, id=10)

print(g)
print(v)
# --8<-- [end:vertex_add]

# --8<-- [start:edge_add]
from raphtory import Graph

g = Graph()
e = g.add_edge(timestamp=1, src=15, dst=16)

print(g)
print(e)
# --8<-- [end:edge_add]

# --8<-- [start:different_time_types]
from raphtory import Graph
from datetime import datetime

g = Graph()
g.add_vertex(timestamp="2021-02-03 14:01:00", id=10)

# Create a python datetime object
datetime_obj = datetime(2021, 1, 1, 12, 32, 0, 0)
g.add_vertex(timestamp=datetime_obj, id=10)

print(g)
print(g.vertex(id=10).history())
print(g.earliest_date_time)
# --8<-- [end:different_time_types]

# --8<-- [start:id_types]
from raphtory import Graph

g = Graph()

g.add_vertex(timestamp=123, id="User 1")
g.add_vertex(timestamp=456, id=200)
g.add_edge(timestamp=789, src="User 1", dst=200)

print(g.vertex("User 1"))
print(g.vertex(200))
print(g.edge("User 1", 200))
# --8<-- [end:id_types]

# --8<-- [start:property_types]
from raphtory import Graph
from datetime import datetime

g = Graph()

# Primitive type properties added to a vertex
g.add_vertex(
    timestamp=1,
    id="User 1",
    properties={"count": 1, "greeting": "hi", "encrypted": True},
)
g.add_vertex(
    timestamp=2,
    id="User 1",
    properties={"count": 2, "balance": 0.6, "encrypted": False},
)
g.add_vertex(
    timestamp=3,
    id="User 1",
    properties={"balance": 0.9, "greeting": "hello", "encrypted": True},
)

# Dictionaries and Lists added to a graph
g.add_property(
    timestamp=1,
    properties={
        "inner data": {"name": "bob", "value list": [1, 2, 3]},
        "favourite greetings": ["hi", "hello", "howdy"],
    },
)
datetime_obj = datetime.strptime("2021-01-01 12:32:00", "%Y-%m-%d %H:%M:%S")
g.add_property(
    timestamp=2,
    properties={
        "inner data": {
            "date of birth": datetime_obj,
            "fruits": {"apple": 5, "banana": 3},
        }
    },
)

# Graph property on an edge
g2 = Graph()
g2.add_vertex(timestamp=123, id="Inner User")

g.add_edge(timestamp=4, src="User 1", dst="User 2", properties={"i_graph": g2})

# Printing everything out
v = g.vertex(id="User 1")
e = g.edge(src="User 1", dst="User 2")
print(g)
print(v)
print(e)
# --8<-- [end:property_types]

# --8<-- [start:constant_properties]
from raphtory import Graph
from datetime import datetime

g = Graph()
v = g.add_vertex(timestamp=1, id="User 1")
e = g.add_edge(timestamp=2, src="User 1", dst="User 2")

g.add_constant_properties(properties={"name": "Example Graph"})
v.add_constant_properties(
    properties={"date of birth": datetime.strptime("1990-02-03", "%Y-%m-%d")},
)
e.add_constant_properties(properties={"data source": "https://link-to-repo.com"})

print(g)
print(v)
print(e)
# --8<-- [end:constant_properties]

# --8<-- [start:edge_layers]
from raphtory import Graph

g = Graph()
g.add_edge(
    timestamp=1,
    src="Person 1",
    dst="Person 2",
    properties={"weight": 10},
    layer="Friends",
)
g.add_edge(
    timestamp=2,
    src="Person 1",
    dst="Person 2",
    properties={"weight": 13},
    layer="Friends",
)
g.add_edge(
    timestamp=3,
    src="Person 1",
    dst="Person 2",
    properties={"weight": 20},
    layer="Co Workers",
)
g.add_edge(
    timestamp=4,
    src="Person 1",
    dst="Person 2",
    properties={"weight": 17},
    layer="Friends",
)
g.add_edge(
    timestamp=5,
    src="Person 1",
    dst="Person 2",
    properties={"weight": 35},
    layer="Family",
)

unlayered_edge = g.edge("Person 1", "Person 2")
layered_edge = g.layers(["Co Workers", "Family"]).edge("Person 1", "Person 2")
print(unlayered_edge.properties.temporal.get("weight").values())
print(layered_edge.properties.temporal.get("weight").values())
# --8<-- [end:edge_layers]

# --8<-- [start:server_data]
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

# --8<-- [end:server_data]


# --8<-- [start:graph_from_dataframe]
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

print("The resulting graphs and example vertex/edge:")
print(g)
print(g.vertex("ServerA"))
print(g.edge("ServerA", "ServerB"))
# --8<-- [end:graph_from_dataframe]

# --8<-- [start:adding_dataframe]
g = Graph()
g.load_edges_from_pandas(
    edge_df=edges_df,
    src_col="source",
    dst_col="destination",
    time_col="timestamp",
    props=["data_size_MB"],
    layer_in_df="transaction_type",
    const_props=["is_encrypted"],
    shared_const_props={"datasource": "data/network_traffic_edges.csv"},
)

g.load_vertices_from_pandas(
    vertices_df=vertices_df,
    vertex_col="server_id",
    time_col="timestamp",
    props=["OS_version", "primary_function", "uptime_days"],
    const_props=["server_name", "hardware_type"],
    shared_const_props={"datasource": "data/network_traffic_edges.csv"},
)

print(g)
print(g.vertex("ServerA"))
print(g.edge("ServerA", "ServerB"))

# --8<-- [end:adding_dataframe]

# --8<-- [start:const_dataframe]
g = Graph()
g.load_edges_from_pandas(
    edge_df=edges_df,
    src_col="source",
    dst_col="destination",
    time_col="timestamp",
    props=["data_size_MB"],
    layer_in_df="transaction_type",
)

g.load_vertices_from_pandas(
    vertices_df=vertices_df,
    vertex_col="server_id",
    time_col="timestamp",
    props=["OS_version", "primary_function", "uptime_days"],
)

g.load_edge_props_from_pandas(
    edge_df=edges_df,
    src_col="source",
    dst_col="destination",
    layer_in_df="transaction_type",
    const_props=["is_encrypted"],
    shared_const_props={"datasource": "data/network_traffic_edges.csv"},
)

g.load_vertex_props_from_pandas(
    vertices_df=vertices_df,
    vertex_col="server_id",
    const_props=["server_name", "hardware_type"],
    shared_const_props={"datasource": "data/network_traffic_edges.csv"},
)

print(g)
print(g.vertex("ServerA"))
print(g.edge("ServerA", "ServerB"))
# --8<-- [end:const_dataframe]

# --8<-- [start:save_load]
from raphtory import Graph
import pandas as pd

edges_df = pd.read_csv("data/network_traffic_edges.csv")
edges_df["timestamp"] = pd.to_datetime(edges_df["timestamp"]).astype(
    "datetime64[ms, UTC]"
)

g = Graph()
g.load_edges_from_pandas(
    edge_df=edges_df,
    src_col="source",
    dst_col="destination",
    time_col="timestamp",
    props=["data_size_MB"],
    layer_in_df="transaction_type",
)
g.save_to_file("/tmp/saved_graph")
loaded_graph = Graph.load_from_file("/tmp/saved_graph")
print(g)
print(loaded_graph)
# --8<-- [end:save_load]
