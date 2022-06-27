---
layout: post
title:  "Raphtory's Filter API"
categories: [Features,Analysis]
author: Naomi Arnold
excerpt: One of the features of the new 0.5.0 release of Raphtory is the Filter API which allows you to remove vertices and edges from a graph perspective, leaving just those which satisfy a given criterion. Graph filtering can be a really beneficial step to include in your data pipeline, particularly if you are working with large or dense networks, but it's not always clear how to start. In this blog post we will cover some of the benefits of filtering, a whistle-stop tour of common graph filtering techniques and how they are implemented in Raphtory.
---

One of the features of the new 0.1.0 release of Raphtory is the Filter API which allows you to remove vertices and edges from a graph perspective, leaving just those which satisfy a given criterion. Graph filtering can be a really beneficial step to include in your data pipeline, particularly if you are working with large or dense networks, but it's not always clear how to start. In this blog post we will cover some of the benefits of filtering, a whistle-stop tour of common graph filtering techniques and how they are implemented in Raphtory.

## Why filter?

* **Clearer visualisation and querying**: once a graph is bigger than a few thousand nodes and edges, it becomes hard to meaningfully visualise it. Pruning nodes and edges down to a *backbone* can produce something that still captures the main features of the graph but is small enough to visualise.
* **Algorithms run quicker**: many graph algorithms have a complexity of $\mathcal{O}(m)$ or $\mathcal{O}(n^2)$ meaning the time it takes to run scales with the number of edges or squared number of nodes in the graph. Filtering out vertices and edges can therefore drastically reduce the time taken to run these algorithms.
* **Removal of "noise"**: tasks such as community detection are more easily achieved on sparser graphs. Filtering can help remove edges which don't add much information to the overall graph structure, potentially leading to more meaningful results.

## Basic filter API

At the lowest level, Raphtory's *algorithm API* allows removal of vertices and edges via `vertex.remove()` and `edge.remove()`. The *filter API* allows removal of vertices/edges by specifying a function taking a `Vertex` or `Edge` to a `Boolean` true/false value. Vertices, edges respectively, for which this function returns true are kept in the graph and otherwise they are removed. As an example,
```scala
graph.filter(vertex => vertex.degree>=1)
```
will remove all vertices with degree zero, and
```scala
graph.edgeFilter(edge => edge.weight[Int]()>1)
```
will remove all weight 1 edges. 

Additionally, the `VertexFilter` and `EdgeFilter` classes enable the filtering to be run within a chain of algorithms.

For example,

```scala
graph.
    .execute(PageRank -> 
             VertexFilter(vertex => vertex.getState("prlabel")>0.001) ->
             LPA)
```
will run the PageRank algorithm on the graph, filter the graph down to vertices with PageRank score above 0.001, then run the Label Propagation community detection algorithm over this new filtered graph.

## Quantile filters
Filtering by applying a global threshold such as keeping nodes above a certain centrality value or removing edges below a certain weight/strength may be useful if a sensible threshold is known already. More often, however, we want to filter the network down to a target size or density, especially if the reason for filtering is to improve the runtime or make it small enough to visualise. For example, we might want to distill the graph down to the top 50% of edges in weight, not necessarily caring about a specific weight threshold. 

This is where vertex and edge quantile filtering comes in. Rather than specifying a threshold value, we can specify quantile of interest to keep in the graph. Using the analogy fo the previous example,

```scala
graph.        ...
    .execute(PageRank -> 
             VertexQuantileFilter("prlabel",lower=0.9f) ->
             LPA)
```

would first run the PageRank algorithm, then filter out the *bottom 90%* of nodes by this PageRank score, before running the label propagation algorithm.

This has the benefit of not needing to calculate an appropriate threshold beforehand if the goal is only to reduce the graph by a given proportion.

## Pitfalls :warning:

This above of filtering: either setting a threshold or setting a quantile of interest, is fairly common in network analysis. However, it's worth being aware of a common feature of many node and edge distributions: heavily unequal distributions. What does this mean and why do we care?

Let's take a look at the following example. In the Raphtory project, we have recently been working with an English-language corpus of sentences from books, spanning from the 1800s to the 2010s. The first dataset spans the 1810-1860 period, the second spans the 1960-2010 period. This can be turned into a graph where the words are vertices and the number of sentences in which they co-occur forms a weighted edge. Naturally, this leads to a dense graph, since a sentence of 10 words would lead to those 10 nodes being completely connected in the graph. It is a perfect candidate, therefore, for doing some edge filtering.

The first filter we tried in this situation is to remove edges below the median weight as a proxy for less meaningful edges. However, we found that the a huge proportion of edges were being removed, much more than the quantile proportion specified. When we investigated the distribution of edge weights (shown below), the reason for this became clear.
![](https://i.imgur.com/cEC5z8q.png)
The above figure shows the number of edges in the two time periods that would be removed by applying a global weight threshold to the edges. In both datasets, around 80% of the edges have weight 1 so this approach would have no inbetween from the whole graph to 20% of it. A similar phenomenon often occurs with vertex degree in real networks, with most vertices having degree 1.

Another nuance that this filtering method does not capture is the *information* content of the edges. There may be high frequency edges that carry little information, purely by each of the two words being themselves high-frequency, and conversely, low frequency edges that are high compared to the total occurrences of that word.

With these things in mind, it was clear that we needed a new filtering approach.

### Introducing the Disparity Filter

In networks such as this one with weighted edges, Serrano et al [1] developed a method for filtering edges that can overcome these challenges. The method asks: how meaningful is this edge compared to the edges coming from vertices adjacent to it? 

The method uses a *null model* which assumes that the total weight of edges coming from a node is instead distributed along those edges at random. Then, provided with a desired significance level, it is possible to say that an edge has a *higher weight* than expected at random. 

First, being a more local filter, this method acts to normalise the effects of the degree of the vertex at each end of the edge. Second, it provides a more fine grained ranking of the edges for removal (see below).
![](https://i.imgur.com/1mXEhT6.png)
The above figure now shows how the number of edges would be reduced by decreasing the significance value $\alpha$. This means that the network can be tuned down to any desired size.

For undirected weighted networks, Raphtory's `filter` module includes the Disparity Filter, which can work within the chain API as with other filtering algorithms. 

[1] Serrano, M. Á., Boguná, M., & Vespignani, A. (2009). Extracting the multiscale backbone of complex weighted networks. Proceedings of the National Academy of Sciences, 106(16), 6483-6488.