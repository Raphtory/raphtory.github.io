# Node centric algorithms 
The second category of algorithms are `node centric` and return a value for each node in the graph. These results are stored within a `NodeState` object which has functions for sorting, grouping, top_k and conversion to dataframes. To demonstrate these functions below we have run [PageRank](https://en.wikipedia.org/wiki/PageRank) and [Weakly Connected Components](https://en.wikipedia.org/wiki/Component_(graph_theory)).

## Continuous Results (PageRank)
`PageRank` is an centrality metric developed by Google's founders to rank web pages in search engine results based on their importance and relevance. This has since become a standard ranking algorithm for a whole host of other usecases.

Raphtory's implementation returns the score for each node - these are continuous values, meaning we can discover the most important characters in our Lord of the Rings dataset via `top_k()`.

In the code below we first get the result of an individual character (Gandalf), followed by the values of the top 5 most important characters. 

{{code_block('getting-started/algorithms','pagerank',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="algorithms"
    --8<-- "python/getting-started/algorithms.py:pagerank"
    ```

## Discrete Results (Connected Components)

`Weakly connected components` in a directed graph are `subgraphs` where every node is reachable from every other node (if edge direction is ignored). 

This algorithm returns the id of the component each node is a member of - these are discrete values, meaning we can use `groups` to find additional insights like the size of the [largest connected component](https://en.wikipedia.org/wiki/Giant_component). 

In the code below we first run the algorithm and print the result so we can see what it looks like. 

!!! info

    The `component ID (value)` is generated from the lowest `node ID` in the component.

Next we take the results and group the nodes by these IDs and calculate the size of the largest component. 

!!! info 

    Almost all nodes are within this component (134 of the 139), as is typical for social networks.

{{code_block('getting-started/algorithms','connectedcomponents',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="algorithms"
    --8<-- "python/getting-started/algorithms.py:connectedcomponents"
    ```