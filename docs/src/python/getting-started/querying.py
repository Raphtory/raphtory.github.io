# --8<-- [start:read_data]
import pandas as pd
edges_df = pd.read_csv("data/OBS_data.txt",sep="\t",header=0, usecols=[0,1,2,3,4], parse_dates=[0])
edges_df["DateTime"] = pd.to_datetime(edges_df["DateTime"]).astype(
    "datetime64[ms]"
)
edges_df.dropna(axis=0,inplace=True)
edges_df['Weight'] = edges_df['Category'].apply(lambda c: 1 if (c=='Affiliative') else (-1 if (c=='Agonistic') else 0))
print(edges_df.head())
# --8<-- [end:read_data]

# --8<-- [start:new_graph]
import raphtory as rp

g = rp.Graph()
g.load_edges_from_pandas(edge_df = edges_df, src_col="Actor", dst_col="Recipient", time_col="DateTime", layer_in_df="Behavior",props=["Weight"])
print(g)
print("Earliest datetime: ",g.earliest_date_time())
print("Latest datetime: ",g.latest_date_time())
print("Unique layers: ",g.get_unique_layers())
# --8<-- [end:new_graph]

# --8<-- [start:neighbours]
v = g.vertex("FELIPE")
print(v.neighbours())
print("Felipe has "+str(v.in_degree())+" incoming friendships and "+str(v.out_degree())+" outgoing friendships.")

# neighbours_sorted = sorted(v.out_edges(), key = lambda nb : nb.explode().weight().sum())
# --8<-- [end:neighbours]

# --8<-- [start:friendship]
e = g.edge("FELIPE","MAKO")
e_reversed = g.edge("MAKO","FELIPE")
print(e)
print(e_reversed)
print(e.history())
# neighbours_sorted = sorted(v.out_edges(), key = lambda nb : nb.explode().weight().sum())
# --8<-- [end:frienship]