# Ingesting from dataframes
If you prefer to initially manipulate your data in a `dataframe` before converting into a graph, you can easily hand this directly to Raphtory once your preprocessing is complete.

## Creating a graph from dataframes
The all-in-one way to do this is via the `load_from_pandas()` function on the `Graph` which will take a dataframe for your edges (and optionally for vertices) and return a graph built from these. This function has optional arguments to cover everything we have seen in the prior [direct updates tutorial](2_direct-updates.md).

In the example below we are ingesting some network traffic data looking at different types of interactions between servers. In the first half of the code we ingest information about the servers and their interactions into two dataframes and make some changes to the timestamp column such that its handled in milliseconds not nanoseconds. The two dataframes are then printed out so you can see the headers and values.

{{code_block('getting-started/ingestion','server_data',[])}}

!!! Output

    ```python exec="on" result="text" session="dataframes"
    --8<-- "python/getting-started/ingestion.py:server_data"
    ```

Next we call the `load_from_pandas()` function, specifying for the edges:

* The dataframe we are ingesting (`edges_df`).
* The source, destination and time columns within the dataframe (`source`,`destination`,`timestamp`).
* The temporal properties (`data_size_MB`), constant properties (`is_encrypted`), and the layer (`transaction_type`) .
* An additional set of constant properties which will be added to all edges, specifying where these edges come from (useful for when we merge more data in).

This is followed by the information for the vertices:

* The dataframe we are ingesting (`vertices_df`).
* The vertex ID and time columns (`server_id`,`timestamp`).
* The temporal properties (`OS_version`,`primary_function`,`uptime_days`) and constant properties (`server_name`,`hardware_type`).
* A shared constant property labelling the source of this information.

The resulting graph and an example vertex/edge are then printed to show the data fully converted.

{{code_block('getting-started/ingestion','graph_from_dataframe',[])}}

!!! Output

    ```python exec="on" result="text" session="dataframes"
    --8<-- "python/getting-started/ingestion.py:graph_from_dataframe"
    ```

## Adding dataframes into an existing graph
It may well be the case that you already have a graph which has some data in it or you have several dataframes you wish to merge together into one graph. To handle this, the graph has the `load_vertices_from_pandas()` and `load_edges_from_pandas()` functions which can be called on an already established graph. 

Below we break the above example into a two stage process, first adding the edges and then adding in the vertices. As you can see in the output the same graph has been created, and can now be updated with direct updates or further datasets.

{{code_block('getting-started/ingestion','adding_dataframe',[])}}

!!! Output

    ```python exec="on" result="text" session="dataframes"
    --8<-- "python/getting-started/ingestion.py:adding_dataframe"
    ```

## Adding constant properties via dataframes
As with the direct updates, there may be instances where you are adding a dataset which has no timestamps within it. To handle this when ingesting via dataframes the graph has the `load_edge_props_from_pandas()` and `load_vertex_props_from_pandas()` functions.

Below we break the ingestion into a four stage process, adding the constant properties at the end. These are all done from the same two dataframes for brevity of the example, in real instances these would probably be four different dataframes, one for each function call.

!!! warning 
    Constant properties can only be added to vertices and edges which are part of the graph. If you attempt to add a constant property without first adding the vertex/edge an error will be thrown.

{{code_block('getting-started/ingestion','const_dataframe',[])}}

!!! Output

    ```python exec="on" result="text" session="dataframes"
    --8<-- "python/getting-started/ingestion.py:const_dataframe"
    ```
