# Querying your graph

After reading in data to Raphtory, we can now make use of this graph representation to ask some interesting questions. For this section, we will study a dataset from [SocioPatterns](http://www.sociopatterns.org/datasets/baboons-interactions/) of interactions between baboons. It comprises different behavioural interactions between a group of 22 baboons over a month. This dataset was analysed in the paper [V. Gelardi, J. Godard, D. Paleressompoulle, N. Claidière, A. Barrat, “Measuring social networks in primates: wearable sensors vs. direct observations”, Proc. R. Soc. A 476:20190737 (2020)](https://royalsocietypublishing.org/doi/10.1098/rspa.2019.0737). 

The features we focus on in this dataset are the time, actor and recipient of an interaction, the behaviour type and behaviour category (affiliative, agonistic or other). In addition, we add a weight column which quantifies the three categories into +1, -1 and 0 respectively.

{{code_block('getting-started/querying','read_data',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:read_data"
    ```

Below we model this as a Raphtory graph using the `load_edges_from_pandas` function (see the previous section for details), conceptualising it as a weighted multi-layer graph through the `Weight` and `Behaviour` fields. Note that calling `print` on the graph will return some basic metrics on the number of vertices and edges.

{{code_block('getting-started/querying','new_graph',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:new_graph"
    ```
 
## Graph metrics

## Vertex metrics

When we used the `load_edges_from_pandas` function, this created a vertex for each of the unique baboon names in our Actor and Recipient columns and gave them an `id` property accordingly. When we are then interacting with the graph, we can select them by name. For example, we can query the baboon `FELIPE` for his neighbours: the baboons he interacted with at some point during the collection period. 

As Raphtory models things as a directed graph, we can look also at incoming and outgoing interactions, as well as viewing these as combined.

{{code_block('getting-started/querying','neighbours',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:neighbours"
    ```

!!! info
    Why is PathFromVertex returned from `neighbours` rather than a simple list of vertices? We will discuss this in `Vectorised functions`, but if you need just a list you can wrap this in python's `list` function.

## Edge metrics

We can also investigate individual edges. Here we can look at the edges in both directions between `FELIPE` and `MAKO`. Here, while there were many interactions between the two baboons, these interactions are represented by just two edges, one for each direction, with each interaction marked as an update in the edge's history. Below, we can see the edge between Felipe and Mako and the times of each interaction.

{{code_block('getting-started/querying','friendship',['Edge'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:friendship"
    ```

## Property queries

### Temporal specific functions

## Vectorised functions

When we called `v.neighbours()` earlier, a `PathFromVertex` was returned rather than a straightforward list. This is an example of the vectorised functionality that Raphtory makes use of. In the Vertex API, this allows for functions that take a vertex and return a PathfromVertex to be chained in sequence. 

For example, for a vertex object `v`, `v.neighbours().neighbours()` will return the two-hop neighbours of `v`. The first call of `neighbours()` returns the immediate neighbours of `v`, the second applies `neighbours()` to each of the vertices returned by the first call. These are flattened under the hood such that a single `PathFromVertex` is returned. Similarly, any functions that a vertex can call can sit within this chain.

The same is also true for edges. One important function for edge is `explode()` which returns an edge view for each interaction represented by that edge. When these interactions have properties like weight, we can 

{{code_block('getting-started/querying','exploded_edge',['Edges'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:exploded_edge"
    ```

## Querying the graph over time

### At and Windowing

### Rolling and Expanding

## Graph views

### Layered graphs

### Subgraph

### Materialize