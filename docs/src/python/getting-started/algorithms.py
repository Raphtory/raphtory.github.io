# --8<-- [start:data_loading]
from raphtory import Graph
import pandas as pd

df=pd.read_csv("data/lotr.csv")
print(df)

lotr_graph = Graph.load_from_pandas(edges_df=df,src="src",dst="dst",time="time")
# --8<-- [end:data_loading]

# --8<-- [start:global]
from raphtory import algorithms as rp
density = rp.directed_graph_density(lotr_graph)
clustering_coefficient = rp.global_clustering_coefficient(lotr_graph)
reciprocity = rp.global_reciprocity(lotr_graph)
print("The graph's density is",density)
print("The graph's clustering coefficient is",clustering_coefficient)
print("The graph's reciprocity is",reciprocity)
# --8<-- [end:global]

# --8<-- [start:connectedcomponents]
from raphtory import algorithms as rp
results = rp.weakly_connected_components(lotr_graph)

# Convert the results to a dataframe so we can have a look at them
df = results.to_df()
print(f"{df}\n")

#Group the components together
components = results.group_by()
print(f"{components}\n")

#Get the size of each component
component_sizes = {key: len(value) for key, value in components.items()}
#Get the key for the largest component
largest_component = max(component_sizes,key=component_sizes.get)
#Print the size of the largest component
print(f"The largest component contains {component_sizes[largest_component]} of the {lotr_graph.num_vertices()} vertices in the graph.")
# --8<-- [end:connectedcomponents]

# --8<-- [start:pagerank]
from raphtory import algorithms as rp
results = rp.pagerank(lotr_graph)

#Getting the results for an individual character (Gandalf)
gandalf_rank = results.get("Gandalf")
print(f"Gandalf's ranking is {gandalf_rank}\n")

#Getting the top 5 most important characters and printing out their scores
top_5 = results.top_k(5)
for rank, (name, score) in enumerate(top_5, 1):
    print(f"Rank {rank}: {name} with a score of {score:.5f}")
# --8<-- [end:pagerank]

# --8<-- [start:rolling]

import matplotlib.pyplot as plt

importance = []
time = []

for windowed_graph in lotr_graph.rolling(window=2000):
    result = rp.pagerank(windowed_graph)
    importance.append(result.get("Gandalf"))
    time.append(windowed_graph.earliest_time())

print("Outputting the results via matplotlib:")

plt.plot(time, importance, marker='o')
plt.xlabel('Sentence (Time)')
plt.ylabel('Pagerank Score')
plt.title("Gandalf's importance over time")
plt.grid(True)
plt.savefig("docs/output/gandalf_rank")
# --8<-- [end:rolling]


    