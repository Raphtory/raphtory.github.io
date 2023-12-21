# Layered graphs
!!!info 
    Edge layers have been discussed several times, notably in [Ingestion](../ingestion/2_direct-updates.md#edge-layers) and [Exploded Edges](../querying/4_edge-metrics.md#exploded-edges). Please check these before reading this section.

 As previously discussed, an edge object by default will contain information on all layers between its source and destination nodes. However, it is often the case that there are a subset of these relationships that we are interested in. To handle this the `Graph`, `Node` and `Edge` provide the `layers()` function. This takes a list of layer names and returns a view with only edge updates that occurred on these layers. 

Layer views can also be used in combination with any other view function. As an example of this, in the code below we look at the total edge weight over the full graph, then restrict this to the `Grooming` and `Resting` layers and then reduce this further by applying a window between the 13th and 20th of June.

{{code_block('getting-started/querying','layered',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:layered"
    ```

## Traversing the graph with layers

As with the time based filters (discussed [here](2_time.md#traversing-the-graph-with-views)), if a layer view is applied to the graph, all extracted entities will have this view applied to them. If, however, the layer view is applied to a node or edge, it will only last until you have hoped to a new node.

Expanding on the example from [the time views](2_time.md#traversing-the-graph-with-views), if we wanted to look at LOME's neighbours who he has groomed, followed by who those monkeys have rested with, we could write the following query.

{{code_block('getting-started/querying','layered_hopping',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:layered_hopping"
    ```
