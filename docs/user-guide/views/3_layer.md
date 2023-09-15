# Layered graphs
!!!info 
    Edge layers have been discussed several times, notably in [Ingestion](../ingestion/direct-updates.md#edge-layers) and [Exploded Edges](../querying/edge-metrics.md#exploded-edges). Please check these before reading this section.

 As previously discussed, an edge object by default will contain information on all layers between its source and destination vertices. However, it is often the case that there are a subset of these relationships that we are interested in. To handle this the `Graph`, `Vertex` and `Edge` provide the `layers()` function. 

 This takes a list of layer names and returns a view with only edge updates that occurred on these layers. Layer views will pass their restrictions on to any object they return (as with the time views) and can be used in combination with any other view function.

 As an example of this, in the code below we look at the total edge weight over the full graph, then restrict this to the `Grooming` and `Resting` layers and then reduce this further by applying a window between the 13th and 20th of June.

{{code_block('getting-started/querying','layered',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:layered"
    ```
