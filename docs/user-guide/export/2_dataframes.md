
# Exporting to Pandas dataframes
As we are ingesting from a set of dataframes, let's kick off by looking at how to convert back into them. For this Raphtory provides the `to_df()` function on both the `Nodes` and `Edges`. 

## Node Dataframe

To explore the use of `to_df()` on the nodes we can first we call the function with default parameters. This exports only the latest property updates and utilises epoch timestamps - the output from this can be seen below. 

To demonstrate the flags which can be utilised, we call `to_df()` again, this time enabling the property history and utilising datetime timestamps. The output for this can also be seen below.

{{code_block('getting-started/export','node_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:node_df"
    ```

## Edge Dataframe
Exporting to an edge dataframe via `to_df()` works the same as for the nodes. The only difference is by default this will export the property history for each edge, split by edge layer. This is because this function has an alternative flag to explode the edges and view each update individually (which will then ignore the `include_property_history` flag). 

In the below example we first create a subgraph of the monkey interactions, selecting some monkeys we are interested in (`ANGELE` and `FELIPE`). This isn't a required step, but is to demonstrate the export working on graph views. 

 We then call `to_df()` on the subgraph edges, setting no flags. In the output you can see the property history for each interaction type (layer) between `ANGELE` and `FELIPE`.

 Finally, we call `to_df()` again, turning off the property history and exploding the edges. In the output you can see each interaction which occurred between `ANGELE` and `FELIPE`.
 
!!! info 

    We have further reduced the graph to only one layer (`Grunting-Lipsmacking`) to reduce the output size.

{{code_block('getting-started/export','edge_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:edge_df"
    ```
