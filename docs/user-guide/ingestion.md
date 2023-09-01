# Getting data into Raphtory

There are plenty of ways to get data into Raphtory and start running analysis. In this tutorial we are going to cover three of the most versatile - direct updating, loading from a Pandas Dataframe and loading from a saved Raphtory graph. 

## Creating a graph
To get started we first need to create a graph to store our data. Printing this graph will show it as empty with no vertices, edges or update times.

{{code_block('getting-started/ingestion','new_graph',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/ingestion"
    --8<-- "python/getting-started/ingestion.py:new_graph"
    ```

## Direct Updates

Now that we have a graph we can directly update it with the `add_vertex` and `add_edge` functions.

### Adding vertices
To add a vertex we need a unique `id` to represent it and an update `timestamp` to specify when in the history of your data this vertex addition took place. In the below example we are going to add vertex `10` at timestamp `1`. 

!!! info

    If your data doesn't have any timestamps, don't fret! You can just set a constant value like `1` for all additions into the graph.  

{{code_block('getting-started/ingestion','vertex_add',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/vertex_add"
    --8<-- "python/getting-started/ingestion.py:vertex_add"
    ```

Printing out the graph and the returned vertex we can see it has been added to the graph and the earliest/latest time has been updated.

### Adding edges
All graphs in raphtory are [directed](https://en.wikipedia.org/wiki/Directed_graph), meaning edge additions must specify a `timestamp` (the same as a `vertex_add`), a `source` vertex the edge starts from and a `destination` vertex the edge ends at. 

As an example of this below we are adding an edge to the graph from `15` to `16` at timestamp `1`.

!!! info
    You will notice in the output that the graph says that it has two vertices as well as the edge. This is because Raphtory automatically creates the source and destination vertices at the same time if they are yet to exist in the graph. This is to keep the graph consistent and avoid `hanging edges`.

{{code_block('getting-started/ingestion','edge_add',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/edge_add"
    --8<-- "python/getting-started/ingestion.py:edge_add"
    ```

### Accepted ID types
The data you want to use for vertex IDs may not always be integers, they can often be unique strings like a person's username or a blockchain wallet hash. As such `add_vertex` and `add_edge` will accept also accept strings for their `id`, `src` & `dst` arguments. 

Below you can see we are adding two vertices to the graph `User 1` and `200` and an edge between them. 
{{code_block('getting-started/ingestion','id_types',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/id_types"
    --8<-- "python/getting-started/ingestion.py:id_types"
    ```

### Accepted timestamps
While integer based timestamps (like in the above examples) can represent both [logical time](https://en.wikipedia.org/wiki/Logical_clock) and [epoch time](https://en.wikipedia.org/wiki/Unix_time), datasets can often have their timestamps stored in human readable formats or special datetime objects. As such, `add_vertex` and `add_edge` can accept integers, datetime strings and datetime objects interchangeably. 

Below we can see vertex `10` being added into the graph at `2021-02-03 14:01:00` and `2021-01-01 12:32:00`. The first timestamp is kept as a string, with Raphtory internally handling the conversion, and the second has been converted into a python datetime object before ingestion.

{{code_block('getting-started/ingestion','different_time_types',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/different_time_types"
    --8<-- "python/getting-started/ingestion.py:different_time_types"
    ```

In our output we can see the `history` of vertex `10`` contains the two times we have added it into the graph as unix epochs (maintained in ascending order). We can also request these times back in a human readable format as has been done for the graph's earliest time.

### Properties
Alongside the structural update history, Raphtory can maintain the changing value of properties associated with vertices and edges. Both the `add_vertex` and `add_edge` functions have an optional parameter `properties` which takes a dictionary of key value pairs to be stored at the given timestamp. 

The graph itself may also have its own `global properties` via the `add_property` function which takes only a `timestamp` and a `properties` dictionary. 

Properties can consist of primitives (`Integer`, `Float`, `String`, `Boolean`, `Datetime`) and structures (`Dictionary`, `List`, `Graph`). This allows you to store both basic values as well as do complex hierarchical modelling depending on your use case.

In the example below we are using all of these functions to add a mixture of properties to a vertex, an edge and the graph.


!!! warning
    Please note that once a `property key` is associated to one of the above types for a given vertex/edge/graph, attempting to add a value of a different type under the same key will result in an error. 

{{code_block('getting-started/ingestion','property_types',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/property_types"
    --8<-- "python/getting-started/ingestion.py:property_types"
    ```

!!! info
    You will see in the output that when we print these, only the latest values are shown. The older values haven't been lost, in fact the history of all of these different property types can be queried, explored and aggregated, as you will see in [Querying your graph](../user-guide/querying.md).

#### Constant Properties

Alongside the `temporal` properties which have a value history, Raphtory also provides `constant` properties which have an immutable value. These are useful when you know a value won't change or are adding `meta data` to your graph which doesn't make sense to happen at a specific time in the given context. To add these into your model the `graph`, `vertex` and `edge` have the `add_constant_properties` function, which takes a single properties dict argument.

You can see in the example below three different constant properties being added to the `graph`, `vertex` and `edge`. 

{{code_block('getting-started/ingestion','constant_properties',[])}}

```python exec="on" result="text" session="getting-started/constant_properties"
--8<-- "python/getting-started/ingestion.py:constant_properties"
```    

### Edge Layers
If you have worked with other graph libraries you may be expecting two calls to `add_edge` between the same vertices to generate two distinct edge objects. As we have seen above, in Raphtory, these calls will append the information together into the history of a single edge. 

These edges can be `exploded` to interact with all updates independently (as you shall see in [Querying your graph](querying.md)), but Raphtory also allows you to represent totally different relationships between the same nodes via `edge layers`.

The `add_edge` function takes a second optional parameter, `layer`, allowing the user to name the type of relationship being added. All calls to `add_edge` with the same `layer` value will be stored together allowing them to be accessed separately or merged with other layers as required.

You can see this in the example below were we add five updates between `Person 1` and `Person 2` across the layers `Friends`, `Co Workers` and `Family`. When we query the history of the `weight` property on the edge we initially get all of the values back. However, after applying the `layers` `graph view` we only return updates from `Co Workers` and `Family`. 

{{code_block('getting-started/ingestion','edge_layers',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/edge_layers"
    --8<-- "python/getting-started/ingestion.py:edge_layers"
    ```

## Ingesting from dataframes
If you prefer to first load your data into a `dataframe` for initial manipulation you can easily hand this directly to Raphtory once you are done to convert into a graph.

### Creating a graph from dataframes
The all-in-one way to do this is via the `load_from_pandas` function on the `Graph` which will take a dataframe for your edges (and optionally for vertices) and return a graph built from these. This function has optional arguments to cover everything we have seen in the above direct updates.

In the example below we are ingesting some network traffic data looking at different types of interactions between servers. In the first half of the code we ingest information about the servers and their interactions into two dataframes and make some changes to the timestamp column such that its handled in milliseconds not nanoseconds. The two dataframes are then printed out so you can see the headers and values.

Next we call the `load_from_pandas` function, specifying for the edges:

* The dataframe we are ingesting (`edges_df`)
* The source, destination and time columns within the dataframe (`source`,`destination`,`timestamp`)
* The temporal properties (`data_size_MB`), constant properties (`is_encrypted`), the layer (`transaction_type`) 
* An additional set of constant properties which will be added to all edges, specifying where these edges come from (useful for when we merge more data in)

This is followed by the following information for the vertices:

* The dataframe we are ingesting (`vertices_df`)
* The vertex ID and time columns (`server_id`,`timestamp`)
* The temporal properties (`OS_version`,`primary_function`,`uptime_days`), constant properties (`server_name`,`hardware_type`)
* An shared constant property labelling the source of this information, the same as the edges.

The resulting graph and an example vertex/edge are then printed to show the data fully converted.
{{code_block('getting-started/ingestion','graph_from_dataframe',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/graph_from_dataframe"
    --8<-- "python/getting-started/ingestion.py:graph_from_dataframe"
    ```

### Adding dataframes into an existing graph
It may well be the case that you already have a graph which has some data in it or you have several dataframes you wish to merge together into one graph. To handle this, the graph has the `load_vertices_from_pandas` and `load_edges_from_pandas` functions which can be called on an already established graph. 

Below we break the above example into a two stage process, first adding the edges and then adding in the vertices. As you can see in the output the same graph has been created, and can now be updated with direct updates or further datasets.

{{code_block('getting-started/ingestion','adding_dataframe',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/adding_dataframe"
    --8<-- "python/getting-started/ingestion.py:adding_dataframe"
    ```

### Adding constant properties via dataframes
As with the direct updates, there may be instances where you are adding a dataset which has no timestamps within it. To handle this when ingesting via dataframes the graph has the `load_edge_props_from_pandas` and `load_vertex_props_from_pandas` functions.

Below we further break down the ingestion into a four stage process, adding the constant properties at the end  - these are all done from the same two dataframes for brevity of the example, in real instances these would probably be four different dataframes, one for each function call.

!!! warning 
    Constant properties can only be added to vertices and edges which are part of the graph. If you attempt to add a constant property without first adding the vertex/edge an error will be thrown.

{{code_block('getting-started/ingestion','const_dataframe',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/const_dataframe"
    --8<-- "python/getting-started/ingestion.py:const_dataframe"
    ```

## Saving and loading graphs
The fastest way to ingest a graph is to load one from Raphtory's on-disk format using the `load_from_file` function on the graph. This does require first ingesting via one of the methods above and saving the produced graph via `save_to_file`, but means for large datasets you do not need to parse the data every time you run a Raphtory script.
!!! info
    This is similar to [pickling](https://docs.python.org/3/library/pickle.html) and can make a drastic difference on ingestion, especially if your datasets require a lot of preprocessing.

In the example below we ingest the edge dataframe from the last section, save this graph and reload it into a second graph. These are both printed to show they contain the same data.

!!! warning 
    Due to the ongoing development of Raphtory, a saved graph is not guaranteed to be consistent across versions.
{{code_block('getting-started/ingestion','save_load',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/save_load"
    --8<-- "python/getting-started/ingestion.py:save_load"
    ```
