# Querying your graph

After reading in data to Raphtory, we can now make use of this graph representation to ask some interesting questions. For this section, we will study a dataset from [SocioPatterns](http://www.sociopatterns.org/datasets/baboons-interactions/) of interactions between baboons. It comprises different behavioural interactions between a group of 22 baboons over a month. This dataset was analysed in the paper [V. Gelardi, J. Godard, D. Paleressompoulle, N. Claidière, A. Barrat, “Measuring social networks in primates: wearable sensors vs. direct observations”, Proc. R. Soc. A 476:20190737 (2020)](https://royalsocietypublishing.org/doi/10.1098/rspa.2019.0737). 

The features we focus on in this dataset are the time, actor and recipient of an interaction, the behaviour type and behaviour category (affiliative, agonistic or other). In addition, we add a weight column which quantifies the three categories into +1, -1 and 0 respectively.

{{code_block('getting-started/querying','read_data',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:read_data"
    ```

Below we model this as a Raphtory graph using the `load_edges_from_pandas` function (see the previous section for details), conceptualising it as a weighted multi-layer graph through the `Weight` and `Behaviour` fields. Note that calling `print` on the graph will return some basic metrics on the number of vertices and edges.

{{code_block('getting-started/querying','new_graph',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:new_graph"
    ```
 
## Graph metrics

## Vertex metrics

## Edge metrics

## Property queries

### Temporal specific functions

## Vectorised functions

## Querying the graph over time

### At and Windowing

### Rolling and Expanding

## Graph views

### Layered graphs

### Subgraph

### Materialize