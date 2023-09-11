# Querying your graph

After reading in data to Raphtory, we can now make use of the graph representation to ask some interesting questions. For this tutorial, we will use a dataset from [SocioPatterns](http://www.sociopatterns.org/datasets/baboons-interactions/), comprising different behavioural interactions between a group of 22 baboons over a month. 

!!! info 
    If you want to read more about the dataset, you can check it out in this paper: [V. Gelardi, J. Godard, D. Paleressompoulle, N. Claidière, A. Barrat, “Measuring social networks in primates: wearable sensors vs. direct observations”, Proc. R. Soc. A 476:20190737 (2020)](https://royalsocietypublishing.org/doi/10.1098/rspa.2019.0737). 

In the below code we load this dataset into a dataframe and do a small amount of preprocessing to prepare it for loading into Raphtory. This includes dropping rows with blank fields and mapping the values of the `behaviour category` into a `weight` which can be aggregated. The mapping consists of the following conversions:

* Affiliative (positive interaction) → `+1`
* Agonistic (negative interaction) → `-1` 
* Other (neutral interaction) → `0`

{{code_block('getting-started/querying','read_data',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:read_data"
    ```

Next we load this into a Raphtory graph using the `load_edges_from_pandas` function, modelling it as a weighted multi-layer graph, with a layer per unique `behaviour`. 

{{code_block('getting-started/querying','new_graph',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:new_graph"
    ```
 
## Graph metrics and functions

### Basic metrics
Now that we have our graph let's start probing it for some basic metrics, such as how many nodes and edges it contains and the time range over which it exists. 

Note, as the property APIs are the same for the graph, vertices and edges, these are discussed together in [property queries](#property-queries) below.

!!! info
    In the below code segment you will see the functions `num_edges` and `num_temporal_edges` being called and returning different results. This is because `num_edges` returns the number of unique edges (src,dst) which exist and `num_temporal_edges` returns the total edge updates which have occurred. 
    
    The second is useful if you want to imagine each edge update as a separate connection between the two nodes. The edges can be accessed in this manner via `edge.explode()`, as is discussed in [edge metrics](#edge-metrics) below.

{{code_block('getting-started/querying','graph_metrics',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:graph_metrics"
    ```

### Accessing vertices and edges  
Three types of functions are provided for accessing the vertices and edges within the graph: 

* **Existance check:** Via `has_vertex` and `has_edge` you can check if an entity is present within the graph.
* **Direct access:** `vertex` and `edge` will return a vertex/edge object if the entity is present and `None` if it is not.
* **Iterator access:** `vertices` and `edges` will return iterators for all vertices/edges which can be used within a for loop or as part of a [function chain](#chaining-functions).

All of these functions are shown in the code below and will appear in several other examples throughout this tutorial.

{{code_block('getting-started/querying','graph_functions',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:graph_functions"
    ```


## Vertex metrics and functions
Vertices can be accessed by storing the object returned from a call to `add_vertex()`, by directly asking for a specific node via `vertex()`, or by iterating over all nodes via `vertices()`. Once you have a vertex, we can start by asking it some questions. 

### Update history 

Vertices have functions for querying their earliest/latest update time, as an epoch or datetime, as well as their full history (`history()`). In the code below we create a vertex object for `Felipe` and see when their updates occurred. 

{{code_block('getting-started/querying','vertex_metrics',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:vertex_metrics"
    ```


### Neighbours, edges and paths
To investigate who a vertex is connected with we can ask for its `degree()`, `edges()`, or `neighbours()`. As Raphtory is a directed graph all of these functions also have an `in_` and `out_` variation, allowing you get only incoming and outgoing connections respectively. These functions return the following:

* **degree:** A count of the number of unique connections a vertex has.
* **edges:** An iterator (`Edges`) of edge objects, one for each unique `(src,dst)` pair.
* **neighbours:** An iterator of vertex objects (`PathFromVertex`), one for each node the vertex shares an edge with.

In the code below we call a selection of these functions to show the sort of questions you may ask. 

!!! info

    The final section of the code makes use of `v.neighbours().name().collect()` - this is a chain of functions which are run on each vertex in the `PathFromVertex` iterator. We will discuss these sort of operations more in [Chaining functions](#chaining-functions) below. 

{{code_block('getting-started/querying','vertex_neighbours',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:vertex_neighbours"
    ```

## Edge metrics and functions 
Edges can be accessed by storing the object returned from a call to `add_edge()`, by directly asking for a specific edge via `edge()`, or by iterating over all edge via `in-edges()`/`out-edges()`/`edges()`. 

 Here we can look at the connections between `FELIPE` and `MAKO`. While there were many interactions between the two baboons, these interactions are represented by just two edges, one for each direction, with each interaction marked as an update in the edge's history. Below, we can see the edge between Felipe and Mako and the times of each interaction.

### Basic metrics 
`dst()`
`src()`
`layer_name()`
`layer_names()`

### Update history 
`earliest_date_time()`, `latest_date_time()` `history()`

### Exploded edges
`date_time()`
`explode()`
`explode_layers()`
`time()`


## Property queries

### Temporal specific functions
{{code_block('getting-started/querying','friendship',['Edge'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:friendship"
    ```


## Chaining functions

When we called `v.neighbours()` earlier, a `PathFromVertex` was returned rather than a straightforward list. This is an example of the vectorised functionality that Raphtory makes use of. In the Vertex API, this allows for functions that take a vertex and return a PathfromVertex to be chained in sequence. 

For example, for a vertex object `v`, `v.neighbours().neighbours()` will return the two-hop neighbours of `v`. The first call of `neighbours()` returns the immediate neighbours of `v`, the second applies `neighbours()` to each of the vertices returned by the first call. These are flattened under the hood such that a single `PathFromVertex` is returned. Similarly, any functions that a vertex can call can sit within this chain.

The same is also true for edges. One important function for edge is `explode()` which returns an edge view for each interaction represented by that edge. When these interactions have properties like weight, we can combine these across different temporal instances to get some notion of strength of the connection. In the case below we sum the `Weight` value of each of Felipe's out-neighbours to rank them by the number of positive interactions he has initialted with them.

once you call `collect()`, turn it into a list via `list(iterator)` or iterate through it in a loop etc

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