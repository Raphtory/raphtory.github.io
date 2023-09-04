# Running algorithms 

Within Raphtory we have implemented many of the standard algorithms you may expect within a graph library, but have also added several temporal algorithms such as `Temporal Reachability` and `Temporal Motifs`. You can check out the full available list [here](https://docs.raphtory.com/en/master/api/raphtory.html#module-raphtory.algorithms) and edit the code snippets below in your own notebook to test them out.

For this tutorial we shall focus on just `Connected Components` and `PageRank` to demonstrate how to run an algorithm and how to utilise the returned result. All algorithms in Raphtory return a [AlgorithmResult](https://docs.raphtory.com/en/master/api/raphtory.html#raphtory.AlgorithmResultStrU64) which has functions for sorting, grouping, top_k and conversion to dataframes. 




## Running algorithms on graph views 


and look at how Gandaf's importance changes over the history of our graph by splitting the network into 1000 sentence snapshots and running the algorithm on each one.

To do this we first define a `rolling window` over the graph which will create an iterator of `windowed graphs` which only include nodes and edges updated within their window period (1000 sentences).  Before looping through these we can grab the first two snapshots to look at how the `start` and `end` of their windows line up.  

In the code below we use this API to extract Gandalfs score for each 1000 sentances and record it alongside the earliest timestamp in the window, which can the be plotted via matplotlib.