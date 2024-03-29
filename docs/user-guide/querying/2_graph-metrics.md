
# Graph metrics and functions

## Basic metrics
Now that we have our graph let's start probing it for some basic metrics, such as how many nodes and edges it contains and the time range over which it exists. 

Note, as the property APIs are the same for the graph, nodes and edges, these are discussed together in [Property queries](../querying/5_properties.md).

!!! info
    In the below code segment you will see the functions `count_edges()` and `count_temporal_edges()` being called and returning different results. This is because `count_edges()` returns the number of unique edges and `count_temporal_edges()` returns the total edge updates which have occurred. 
    
    The second is useful if you want to imagine each edge update as a separate connection between the two nodes. The edges can be accessed in this manner via `edge.explode()`, as is discussed in [edge metrics and functions](../querying/4_edge-metrics.md).

{{code_block('getting-started/querying','graph_metrics',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:graph_metrics"
    ```

## Accessing nodes and edges  
Three types of functions are provided for accessing the nodes and edges within the graph: 

* **Existance check:** Via `has_node()` and `has_edge()` you can check if an entity is present within the graph.
* **Direct access:** `node()` and `edge()` will return a node/edge object if the entity is present and `None` if it is not.
* **Iterable access:** `nodes` and `edges` will return iterables for all nodes/edges which can be used within a for loop or as part of a [function chain](../querying/6_chaining.md).

All of these functions are shown in the code below and will appear in several other examples throughout this tutorial.

{{code_block('getting-started/querying','graph_functions',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:graph_functions"
    ```
