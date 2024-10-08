# Edge metrics and functions 
Edges can be accessed by storing the object returned from a call to `add_edge()`, by directly asking for a specific edge via `edge()`, or by iterating over all edges via `in-edges`/`out-edges`/`edges`. 

## Edge structure and update history
An edge object in Raphtory will by default contain all updates over all layers between the given source and destination nodes. As an example of this, we can look at the two edges between `FELIPE` and `MAKO` (one for each direction). 

In the code below we create the two edge objects by requesting them from the graph and then print out the layers each is involved in via `layer_names`. We can see here that there are multiple behaviours in each direction represented within the edges.

Following this we access the history and earliest/latest update time, as we have previously with the graph and nodes. This update history consists all interactions across all the aforementioned layers.

!!!info 
    Note that we call `e.src.name` because `src` and `dst` return a node object, instead of just an id/name.

{{code_block('getting-started/querying','edge_history',['Node'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:edge_history"
    ```

## Exploded edges
The very first question you may have after reading this is "What if I don't want all of the layers?". For this Raphtory offers you three different ways to split the edge, depending on your use case:

* `.layers()`: which takes a list of layer names and returns a new `Edge View` which only contains updates for the specified layers - This is discussed in more detail in the [Layer views](../views/3_layer.md) chapter.
* `.explode_layers()`: which returns an iterable of `Edge Views`, each containing the updates for one layer.
* `.explode()`: which returns an `Exploded Edge` containing only the information from one call to `add_edge()` i.e. an edge object for each update. 

In the code below you can see usage of all of these functions. We first call `explode_layers()`, seeing which layer each edge object represents and output its update history. Next we fully `explode()` the edge and see each update as an individual object. Thirdly we use the `layer()` function to look at only the `Touching` and `Carrying` layers and chain this with a call to `explode()` to see the separate updates. 

!!! info
    Within the examples and in the API documentation you will see singular and plural versions what appear to be the same function (i.e. `.layer_names/.layer_name` `.history()/.time`). 
    
    For clarity - singular functions (`.layer_name/.time`) can be called on exploded edges and plural functions (`.layer_names/.history()`) can be called on standard edges.

{{code_block('getting-started/querying','edge_explode_layer',['Node'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:edge_explode_layer"
    ```
