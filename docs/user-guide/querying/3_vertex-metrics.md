
# Vertex metrics and functions
Vertices can be accessed by storing the object returned from a call to `add_vertex()`, by directly asking for a specific node via `vertex()`, or by iterating over all nodes via `vertices()`. Once you have a vertex, we can ask it some questions. 

## Update history 

Vertices have functions for querying their earliest/latest update time (as an epoch or datetime) as well as for accessing their full history (`history()`). In the code below we create a vertex object for the monkey `Felipe` and see when their updates occurred. 

{{code_block('getting-started/querying','vertex_metrics',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:vertex_metrics"
    ```

## Neighbours, edges and paths
To investigate who a vertex is connected with we can ask for its `degree()`, `edges()`, or `neighbours()`. As Raphtory is a directed graph all of these functions also have an `in_` and `out_` variation, allowing you get only incoming and outgoing connections respectively. These functions return the following:

* **degree:** A count of the number of unique connections a vertex has.
* **edges:** An iterable (`Edges`) of edge objects, one for each unique `(src,dst)` pair.
* **neighbours:** An iterable of vertex objects (`PathFromVertex`), one for each node the vertex shares an edge with.

In the code below we call a selection of these functions to show the sort of questions you may ask. 

!!! info

    The final section of the code makes use of `v.neighbours().name().collect()` - this is a chain of functions which are run on each vertex in the `PathFromVertex` iterable. We will discuss these sort of operations more in [Chaining functions](../querying/6_chaining.md). 

{{code_block('getting-started/querying','vertex_neighbours',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:vertex_neighbours"
    ```