
# Exporting to NetworkX

For converting to a networkx graph there is only one function (`to_networkx()`), which has flags for vertex/edge history and for exploding edges. By default all history is included and the edges are separated by layer. 

In the below code snippet we call `to_networkx()` on the network traffic graph, keeping all the default arguments and, therefore, exporting the full history. We have extracted `ServerA` from this graph and printed it so that you may see how the history is modelled. 

!!! info 
    Note that the resulting graph is a networkx `MultiDiGraph` as Raphtory graphs are both directed and have multiple edges between nodes.

 We then call `to_networkx()` again, disabling the property/update history and reprint `ServerA` allowing you to see the difference.   

{{code_block('getting-started/export','networkX',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:networkX"
    ```

## Visualisation
Once converted into a networkX graph you are free to use their full suite of functionality. One great use of this conversion is to make use of their [drawing](https://networkx.org/documentation/stable/reference/drawing.html) library for visualising graphs.

In the code snippet below we use this functionality to draw the network traffic graph, labelling the nodes with their Server ID. These visualisations can become as complex as your like, but we refer you to the [networkx]((https://networkx.org/documentation/stable/reference/drawing.html)) documentation for this.

{{code_block('getting-started/export','networkX_vis',['Graph'])}}