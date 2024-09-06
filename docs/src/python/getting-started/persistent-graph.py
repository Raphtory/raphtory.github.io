# --8<-- [start:simple_graph]
from raphtory import PersistentGraph

G = PersistentGraph()

# new friendship
G.add_edge(1, "Alice", "Bob")

# additional friend
G.add_edge(3, "Bob", "Charlie")

# a dispute
G.delete_edge(5, "Alice", "Bob")

# a resolution
G.add_edge(10, "Alice", "Bob")

print(f"G's edges are {G.edges}")
print(f"G's exploded edges are {G.edges.explode()}")
# --8<-- [end:simple_graph]

# --8<-- [start:hanging_deletions]
G = PersistentGraph()

G.delete_edge(5, "Alice", "Bob")

print(G.edges.explode())
# --8<-- [end:hanging_deletions]

# --8<-- [start:behaviour_1]
G = PersistentGraph()

G.add_edge(1, "Alice", "Bob")
G.delete_edge(5, "Alice", "Bob")
G.add_edge(3, "Alice", "Bob")
G.delete_edge(7, "Alice", "Bob")

print(G.edges.explode())
# --8<-- [end:behaviour_1]

# --8<-- [start:behaviour_2]
G1 = PersistentGraph()

G1.add_edge(1, 1, 2, properties={"message":"hi"})
G1.delete_edge(1, 1, 2)

G2 = PersistentGraph()

G2.delete_edge(1, 1, 2)
G2.add_edge(1, 1, 2, properties={"message":"hi"})

print(f"G1's edges are {G1.edges.explode()}")
print(f"G2's edges are {G2.edges.explode()}")

# --8<-- [end:behaviour_2]

# --8<-- [start:behaviour_3]
G = PersistentGraph()

G.add_edge(1, "Alice", "Bob", layer="colleagues")
G.delete_edge(5, "Alice", "Bob", layer="colleagues")
G.add_edge(3, "Alice", "Bob", layer ="friends")
G.delete_edge(7, "Alice", "Bob", layer="friends")

print(G.edges.explode())
# --8<-- [end:behaviour_3]