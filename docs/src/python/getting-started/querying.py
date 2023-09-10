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
print(f"{g}\n")
print(f"Earliest datetime: {g.earliest_date_time()}\n")
print(f"Latest datetime: {g.latest_date_time()}\n")
print(f"Unique layers: {g.get_unique_layers()}\n")
# --8<-- [end:new_graph]

# --8<-- [start:neighbours]
v = g.vertex("FELIPE")
print(v.neighbours())
print(
    f"Felipe has {v.in_degree()} incoming friendship edges and {v.out_degree()} outgoing friendship edges."
)

# --8<-- [end:neighbours]

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
