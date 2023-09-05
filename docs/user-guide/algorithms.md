# Running algorithms 

Within Raphtory we have implemented many of the standard algorithms you may expect within a graph library, but have also added several temporal algorithms such as `Temporal Reachability` and `Temporal Motifs`. You can check out the full list of available algorithms [here](https://docs.raphtory.com/en/master/#module-raphtory.algorithms) and edit the code snippets below in your own notebook to test them out.

Before we look at the different types of algorithms, let's first load in some data. For these examples we are going to use the [One graph to rule them all](https://arxiv.org/abs/2210.07871) dataset, which maps the co-occurrence of characters within the Lord of The Rings books. This dataset is a simple edge list, consisting of the source character, destination character and the sentence they occurred together in (which we shall use as a timestamp). The dataframe for this can be seen in the output below.

{{code_block('getting-started/algorithms','data_loading',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="algorithms"
    --8<-- "python/getting-started/algorithms.py:data_loading"
    ```

## Graph wide algorithms
The first category of algorithms we can run are `graph wide`, returning one value for the whole graph. There are many useful metrics that fall into this category, of which we run three in the code below:

* [Graph Density](https://en.wikipedia.org/wiki/Dense_graph) - which represents the ratio between the edges present in a graph and the maximum number of edges that the graph could contain.
* [Clustering coefficient](https://en.wikipedia.org/wiki/Clustering_coefficient) - which is a measure of the degree to which vertices in a graph tend to cluster together e.g. how many of your friends are also friends.
* [Reciprocity](https://en.wikipedia.org/wiki/Reciprocity_(network_science)) - which is a measure of the likelihood of vertices in a directed network to be mutually connected e.g. if you follow someone on twitter, whats the change of them following you back.

As you can see below, to run an algorithm you simply need to import the algorithm package, choose an algorithm to run and hand it your graph.

{{code_block('getting-started/algorithms','global',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="algorithms"
    --8<-- "python/getting-started/algorithms.py:global"
    ```


## Vertex centric algorithms 
The second category of algorithms are `vertex centric` and return a value for each node in the graph. These results are stored within a [AlgorithmResult](https://docs.raphtory.com/en/master/api/raphtory.html#raphtory.AlgorithmResultStrU64) object which has functions for sorting, grouping, top_k and conversion to dataframes. To demonstrate these functions below we have run [PageRank](https://en.wikipedia.org/wiki/PageRank) and [Weakly Connected Components](https://en.wikipedia.org/wiki/Component_(graph_theory)).

### Continuous Results (PageRank)
`PageRank` is an centrality metric developed by Google's founders to rank web pages in search engine results based on their importance and relevance. This has since become a standard ranking algorithm for a whole host of other usecases.

Raphtory's implementation returns the score for each node - these are continuous values, meaning we can discover the most important characters via `top_k`.

In the code below we first get the result of an individual character (Gandalf), followed by the values of the top 5 most important characters. 

{{code_block('getting-started/algorithms','pagerank',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="algorithms"
    --8<-- "python/getting-started/algorithms.py:pagerank"
    ```

### Discrete Results (Connected Components)

`Weakly connected components` in a directed graph are `subgraphs` where every vertex is reachable from every other vertex (if edge direction is ignored). 

This algorithm returns the id of the component each vertex is a member of - these are discrete values, meaning we can use `group_by` to find additional insights like the size of the [largest connected component](https://en.wikipedia.org/wiki/Giant_component). 

In the code below we first run the algorithm and turn the results into a dataframe so we can see what they look like. 

!!! info

    The `component ID (value)` is generated from the lowest `vertex ID` in the component, hence why they look like a random numbers in the print out.

Next we take the results and group the vertices by these IDs and calculate the size of the latest component. 

!!! info 

    Almost all vertices are within this component (134 of the 139), as is typical for social networks.

{{code_block('getting-started/algorithms','connectedcomponents',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="algorithms"
    --8<-- "python/getting-started/algorithms.py:connectedcomponents"
    ```
## Running algorithms on graph views 

As with all the queries we saw in the [previous tutorial](querying.md), both `graphwide` and `vertex centric` algorithms can be run on `graph views`. This allows us to see how results change over time, run algorithms on subsets of the layers or remove specific vertices from the graph to see the impact this has. 

Below is an example looking at how Gandaf's importance changes over the course of the books by splitting the graph into 1000 sentence rolling windows and running the algorithm on each one.

Within each windowed graph we use the [AlgorithmResult](https://docs.raphtory.com/en/master/api/raphtory.html#raphtory.AlgorithmResultStrU64) api to extract Gandalf's score and record it alongside the earliest timestamp in the window, which can then be plotted via matplotlib.

{{code_block('getting-started/algorithms','rolling',['Graph'])}}

!!! Output
    ![Gandalf Rank](./gandalf_rank.png)
