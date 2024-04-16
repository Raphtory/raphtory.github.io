# Exporting to Pyvis
For a more interactive visualisation you can export your graphs to [Pyvis](https://pyvis.readthedocs.io/en/latest/), a network visualisation library built on top of [VisJS](https://visjs.github.io/vis-network/examples/).

Due to the nature of Pyvis's model and API, the parameters for `to_pyvis()` are quite different to the other export functions discussed previously. These are split between Raphtory specific parameters and a `kwargs` (key word arguments) map which is passed directly to the pyvis graph during initialisation.

!!! info 
    The Raphtory specific parameters are used to explode the edges and for setting values which are immutable after an edge/node has been inserted into the pyvis model (such as an edges colour or weight). The description of these arguments can be found in the [functions documentation](https://docs.raphtory.com/en/master/reference/core/graph.html#raphtory.PersistentGraph.to_pyvis). 

    The `kwargs` for pyvis are described in their own [documentation](https://pyvis.readthedocs.io/en/latest/documentation.html). These values can also be dynamically set on the pyvis graph, allowing you to experiment with different values without reexporting. This is useful when fine turing elements such as the strength of the gravity in the physics engine.

In the code below we first call `to_pyvis()` on the network traffic graph. Within this we set two Raphtory arguments (`edge_weight` and `edge_color`), specifying that an edge's thickness should be based on the amount of data sent between the servers it links. We then set a pyvis keyword (`directed`) to add arrows to the output, showing the direction of this traffic.

Once the pyvis graph has been generated, we create and apply a style config, setting an appropriate layout algorithm.

Finally, calling the `.show()` function creates a html file where the graph can be interacted with. This is embedded in an iframe below for you to try.


{{code_block('getting-started/export','pyvis',['Graph'])}}
<iframe src="../nx.html" width="800" height="600"></iframe>