# Exporting and visualising your graph
As with Raphtory's connectors for ingesting data, there are a host of different formats and libraries that you can export your graphs into. Below we explore three of these, namely Pandas dataframes, NetworkX graphs and Pyvis graphs.

All functions inside of the `export` module work on both `graphs` and `graph views`, allowing you to specify different windows, layers and subgraphs before conversion. 

By default exporting will include all properties and all update history. However, this can be modified via flags on each export function, depending on use case requirements. You can find a description of these flags in the [export API.](https://docs.raphtory.com/en/v0.5.6/#module-raphtory.export)

!!! Info
    This page doesn't contain an exhaustive list of all the different conversion methods - please feel free to check the [API documentation](https://docs.raphtory.com/) for this list. If we are missing a format that you believe to be important, please raise an [issue](https://github.com/Pometry/Raphtory/issues) and it will be available before you know it!

For the examples in this tutorial we are going to be reusing the network traffic dataset from the [ingestion tutorial](ingestion.md) and the monkey interaction network from [querying your graph](querying.md). In the below code segment you can get a refresher of what these datasets looks like. 

{{code_block('getting-started/export','ingest_data',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:ingest_data"
    ```

## Exporting to Pandas dataframes
As we are ingesting from a set of dataframes, let's kick off by looking at how to convert back into them. For this Raphtory provides two functions `to_vertex_df` and `to_edge_df` as part of the `export` module. As the names suggest, these extract information about the vertices and edges respectively. 

### Vertex Dataframe

To explore the use of `to_vertex_df` we first we call the function passing only our graph. As we don't set any flags this exports the full history, which can be seen within the printed dataframe. The `property` column for `ServerA` has been extracted and printed so this can be seen in full.

To demonstrate some of the flags which can be utilised, we call `to_vertex_df` again, this time disabling the update and property history. You can see in the second set of prints that now only the most recent property values are present and the `update_history` column has been removed.

{{code_block('getting-started/export','vertex_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:vertex_df"
    ```

### Edge Dataframe

   

Exporting to an Edge dataframe via `to_edge_df` works exactly the same as `to_vertex_df`. By default this will export the full update history for each edge, split by edge layer. The flags to remove the history are once again available, as well as a flag to explode the edges and view each update individually. 

In the below example we first create a subgraph of the monkey interactions, selecting some monkeys we are interested in (`ANGELE` and `FELIPE`). This isn't a required step, but is to demonstrate the export working on graph views. 

 We then call `to_edge_df` on the subgraph, setting no flags. In the output you can see the update/property history for each interaction type (layer) between `ANGELE` and `FELIPE`.

 Finally, we call `to_edge_df` again, turning off the property history and exploding the edges. In the output you can see each interaction which occurred between `ANGELE` and `FELIPE`.
 
!!! info 

    We have further reduced the graph to only one layer (`Grunting-Lipsmacking`) to reduce the output size.

{{code_block('getting-started/export','edge_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:edge_df"
    ```

## Exporting to NetworkX

For converting to a networkx graph there is only one function (`to_networkx`), which has flags for vertex/edge history and for exploding edges. By default all history is included and the edges are separated by layer. 

In the below code snippet we call `to_networkx` on the network traffic graph, keeping all the default arguments and, therefore, exporting the full history. We have extracted `ServerA` from this graph and printed it so that you may see how the history is modelled. 

!!! info 
    Note that the resulting graph is a networkx `MultiDiGraph` as Raphtory graphs are both directed and have multiple edges between nodes.

 We then call `to_networkx` again, disabling the property/update history and reprint `ServerA` allowing you to see the difference.   

{{code_block('getting-started/export','networkX',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:networkX"
    ```

### Visualisation
Once converted into a networkX graph you are free to use their full suite of functionality. One great use of this conversion is to make use of their [drawing](https://networkx.org/documentation/stable/reference/drawing.html) library for visualising graphs.

In the code snippet below we use this functionality to draw the network traffic graph, labelling the nodes with their Server ID. These visualisations can become as complex as your like, but we refer you to the [networkx]((https://networkx.org/documentation/stable/reference/drawing.html)) documentation for this.

{{code_block('getting-started/export','networkX_vis',['Graph'])}}


## Exporting to Pyvis
For a more interactive visualisation you can export your graphs to [Pyvis](https://pyvis.readthedocs.io/en/latest/), a network visualisation library built on top of [VisJS](https://visjs.github.io/vis-network/examples/).

Due to the nature of Pyvis's model and API, the parameters for `to_pyvis` are quite different to the other export functions discussed above. These are split between Raphtory specific parameters and a `kwargs` (key word arguments) map which is passed directly to the pyvis graph during initialisation.

!!! info 
    The Raphtory specific parameters are used to explode the edges and for setting values which are immutable after an edge/vertex has been inserted into the pyvis model (such as an edges colour or weight). The description of these arguments can be found in the [export API](https://docs.raphtory.com/en/master/#module-raphtory.export). 

    The `kwargs` for pyvis are described in their own [documentation](https://pyvis.readthedocs.io/en/latest/documentation.html). These values can also be dynamically set on the pyvis graph, allowing you to experiment with different values without reexporting. This is useful when fine turing elements such as the strength of the gravity in the physics engine.

In the code below we first call `to_pyvis` on the network traffic graph. Within this we set two Raphtory arguments (`edge_weight` and `edge_color`), specifying that an edge's thickness should be based on the amount of data sent between the servers it links. We then set a pyvis keyword (`directed`) to add arrows to the output, showing the direction of this traffic.

Once the pyvis graph has been generated, we create and apply a style config, setting an appropriate layout algorithm.

Finally, calling the `.show()` function creates a html file where the graph can be interacted with. This is embedded in an iframe below for you to try.


{{code_block('getting-started/export','pyvis',['Graph'])}}

<iframe src="../../src/output/nx.html" width="800" height="600"></iframe>