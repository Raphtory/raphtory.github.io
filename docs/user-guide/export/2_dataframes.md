
# Exporting to Pandas dataframes
As we are ingesting from a set of dataframes, let's kick off by looking at how to convert back into them. For this Raphtory provides two functions `to_vertex_df()` and `to_edge_df()` as part of the `export` module. As the names suggest, these extract information about the vertices and edges respectively. 

## Vertex Dataframe

To explore the use of `to_vertex_df()` we first we call the function passing only our graph. As we don't set any flags this exports the full history, which can be seen within the printed dataframe. The `property` column for `ServerA` has been extracted and printed so this can be seen in full.

To demonstrate some of the flags which can be utilised, we call `to_vertex_df()` again, this time disabling the update and property history. You can see in the second set of prints that now only the most recent property values are present and the `update_history` column has been removed.

{{code_block('getting-started/export','vertex_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:vertex_df"
    ```

## Edge Dataframe
Exporting to an edge dataframe via `to_edge_df()` works exactly the same as `to_vertex_df()`. By default this will export the full update history for each edge, split by edge layer. The flags to remove the history are once again available, as well as a flag to explode the edges and view each update individually. 

In the below example we first create a subgraph of the monkey interactions, selecting some monkeys we are interested in (`ANGELE` and `FELIPE`). This isn't a required step, but is to demonstrate the export working on graph views. 

 We then call `to_edge_df()` on the subgraph, setting no flags. In the output you can see the update/property history for each interaction type (layer) between `ANGELE` and `FELIPE`.

 Finally, we call `to_edge_df()` again, turning off the property history and exploding the edges. In the output you can see each interaction which occurred between `ANGELE` and `FELIPE`.
 
!!! info 

    We have further reduced the graph to only one layer (`Grunting-Lipsmacking`) to reduce the output size.

{{code_block('getting-started/export','edge_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:edge_df"
    ```
