# Direct Updates

Now that we have a graph we can directly update it with the `add_node()` and `add_edge()` functions.

## Adding nodes
To add a node we need a unique `id` to represent it and an update `timestamp` to specify when in the history of your data this node addition took place. In the below example we are going to add node `10` at timestamp `1`. 

!!! info

    If your data doesn't have any timestamps, don't fret! You can just set a constant value like `1` for all additions into the graph.  

{{code_block('getting-started/ingestion','node_add',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/node_add"
    --8<-- "python/getting-started/ingestion.py:node_add"
    ```

Printing out the graph and the returned node we can see the update was successful and the earliest/latest time has been updated.

## Adding edges
All graphs in raphtory are [directed](https://en.wikipedia.org/wiki/Directed_graph), meaning edge additions must specify a `timestamp` (the same as a `node_add()`), the `source` node the edge starts from and the `destination` node the edge ends at. 

As an example of this below we are adding an edge to the graph from `15` to `16` at timestamp `1`.

!!! info
    You will notice in the output that the graph says that it has two nodes as well as the edge. This is because Raphtory automatically creates the source and destination nodes at the same time if they are yet to exist in the graph. This is to keep the graph consistent and avoid `hanging edges`.

{{code_block('getting-started/ingestion','edge_add',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/edge_add"
    --8<-- "python/getting-started/ingestion.py:edge_add"
    ```

## Accepted ID types
The data you want to use for node IDs may not always be integers, they can often be unique strings like a person's username or a blockchain wallet hash. As such `add_node()` and `add_edge()` will also accept strings for their `id`, `src` & `dst` arguments. 

Below you can see we are adding two nodes to the graph `User 1` and `User 2` and an edge between them. 

{{code_block('getting-started/ingestion','id_types',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/id_types"
    --8<-- "python/getting-started/ingestion.py:id_types"
    ```

!!! warning
    Note: A graph can index nodes by either integers or strings, not both at the same time.This means, for example, you cannot have `User 1` (a string) and `200` (an integer) as ids in the same graph. 

## Accepted timestamps
While integer based timestamps (like in the above examples) can represent both [logical time](https://en.wikipedia.org/wiki/Logical_clock) and [epoch time](https://en.wikipedia.org/wiki/Unix_time), datasets can often have their timestamps stored in human readable formats or special datetime objects. As such, `add_node()` and `add_edge()` can accept integers, datetime strings and datetime objects interchangeably. 

Below we can see node `10` being added into the graph at `2021-02-03 14:01:00` and `2021-01-01 12:32:00`. The first timestamp is kept as a string, with Raphtory internally handling the conversion, and the second has been converted into a python datetime object before ingestion. This datetime object can also have a timezone, with Raphtory storing everything internally in UTC.

{{code_block('getting-started/ingestion','different_time_types',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/different_time_types"
    --8<-- "python/getting-started/ingestion.py:different_time_types"
    ```

In our output we can see the `history` of node `10` contains the two times at which we have added it into the graph (maintained in ascending order), returned in both unix epoch (integer) and datetime format.

## Properties
Alongside the structural update history, Raphtory can maintain the changing value of properties associated with nodes and edges. Both the `add_node()` and `add_edge()` functions have an optional parameter `properties` which takes a dictionary of key value pairs to be stored at the given timestamp. 

The graph itself may also have its own `global properties` via the `add_property()` function which takes only a `timestamp` and a `properties` dictionary. 

Properties can consist of primitives (`Integer`, `Float`, `String`, `Boolean`, `Datetime`) and structures (`Dictionary`, `List`, `Graph`). This allows you to store both basic values as well as do complex hierarchical modelling depending on your use case.

In the example below we are using all of these functions to add a mixture of properties to a node, an edge and the graph.


!!! warning
    Please note that once a `property key` is associated to one of the above types for a given node/edge/graph, attempting to add a value of a different type under the same key will result in an error. 

{{code_block('getting-started/ingestion','property_types',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/property_types"
    --8<-- "python/getting-started/ingestion.py:property_types"
    ```

!!! info
    You will see in the output that when we print these, only the latest values are shown. The older values haven't been lost, in fact the history of all of these different property types can be queried, explored and aggregated, as you will see in [Property Queries](../querying/5_properties.md).

### Constant Properties

Alongside the `temporal` properties which have a value history, Raphtory also provides `constant` properties which have an immutable value. These are useful when you know a value won't change or are adding `meta data` to your graph which doesn't make sense to happen at a specific time in the given context. To add these into your model the `graph`, `node` and `edge` have the `add_constant_properties()` function, which takes a single properties dict argument.

You can see in the example below three different constant properties being added to the `graph`, `node` and `edge`. 

{{code_block('getting-started/ingestion','constant_properties',[])}}

```python exec="on" result="text" session="getting-started/constant_properties"
--8<-- "python/getting-started/ingestion.py:constant_properties"
```    

## Edge Layers
If you have worked with other graph libraries you may be expecting two calls to `add_edge()` between the same nodes to generate two distinct edge objects. As we have seen above, in Raphtory, these calls will append the information together into the history of a single edge. 

These edges can be `exploded` to interact with all updates independently (as you shall see in [Exploded edges](../querying/4_edge-metrics.md/#exploded-edges)), but Raphtory also allows you to represent totally different relationships between the same nodes via `edge layers`.

The `add_edge()` function takes a second optional parameter, `layer`, allowing the user to name the type of relationship being added. All calls to `add_edge` with the same `layer` value will be stored together allowing them to be accessed separately or merged with other layers as required.

You can see this in the example below where we add five updates between `Person 1` and `Person 2` across the layers `Friends`, `Co Workers` and `Family`. When we query the history of the `weight` property on the edge we initially get all of the values back. However, after applying the [`layers()` graph view](../views/3_layer.md) we only return updates from `Co Workers` and `Family`. 

{{code_block('getting-started/ingestion','edge_layers',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/edge_layers"
    --8<-- "python/getting-started/ingestion.py:edge_layers"
    ```