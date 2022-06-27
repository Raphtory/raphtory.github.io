---
layout: page
title: Raphtory Algorithms Bounty Board
permalink: /algorithm-bounty/
---

On this page are the algorithms supported (:heavy_check_mark: = done) and planned to be supported within Raphtory. We will keep this updated as new algorithms are implemented and new ideas are suggested by the community.

For anyone interested in getting involved in Raphtory the low hanging fruit (:grapes:) algorithms will be a great entry point for your first contribution. Once you have merged your algorithm feel free to come back here and tick it off with your github account linked next to it.

## Network models
* Configuration model (also for the randomisation of an empirical graph)
* Erdos-Renyi $G(N,p)$
* Erdos-Renyi $G(N,M)$ :grapes: 
* Preferential attachment model
* Random geometric graphs
* Small-World Model

# Filtering
* Generic node and edge filtering (user provides a function) :heavy_check_mark: 
* Global edge weight threshold :heavy_check_mark: 
* Global vertex property threshold: :heavy_check_mark: 
* Quantile based :heavy_check_mark: ("remove bottom $x$ proportion in terms of degree/pagerank etc") 
* Disparity filter :heavy_check_mark: (aka backbone extraction) https://www.pnas.org/doi/full/10.1073/pnas.0808904106
* Uniform node/edge sampling :heavy_check_mark: (nb it works for sampling with probability $p$ but not for saying "sample N nodes")
* Largest connected component (doable but needs a "counter"/map type of graph state counting number of nodes with a given component id.)
* Ego-network :grapes: 
* $k$-cores :grapes: 

## Stochastic block models
* Tie decay networks  
* Attributes
* Homophily
* Perhaps also monophily, see https://www.nature.com/articles/s41562-018-0321-8 

## Node queries/centralities
* Degree/Weighted degree :heavy_check_mark: 
* Value of label :heavy_check_mark: 

## Edge based algorithms/metrics
* Average neighbour degree :heavy_check_mark: 
* Degree assortativity :grapes: 
* Neighbourhood overlap (jaccard similarity of two nodes in terms of neighbours) :grapes: 
* Reciprocity :grapes:

## Bipartite networks
* Different types of projections 
* Specific randomisations 
* Specific motifs (only even length cycles) 

## Centrality
* Betweenness 
* Closeness 
* Degree/weighted degree/in-out degree  :heavy_check_mark: 
* Distinctiveness :heavy_check_mark: 
* Eigenvector :grapes: 
* Harmonic 
* Influence maximization
* Katz :grapes: 
* PageRank :heavy_check_mark: 
* Weighted PageRank :heavy_check_mark: 
* K-core :grapes: (filter recursively based on degree)
* Rich-club coefficient (filter by degree then count edges remaining) :grapes: 

## Classification
* Graph Convolutional Network (GCN) 
* Greedy Colouring 

## Clustering
* Generalised Degree :question: 
* Square Clustering :grapes: 
* Local/average local clustering coefficient :heavy_check_mark: 
* Transitivity :heavy_check_mark: (sometimes known as global clustering coefficient)

## Cliques
* Maximal Cliques (NP Complete)
* Maximum Quasi-Cliques 

## Communities
* Belief propogation for SBM inference (ref from Tiago about possible distributed  method https://arxiv.org/pdf/1109.3041.pdf) 
* Community based outlier detection :heavy_check_mark: 
* Extension of LPA to temporal multilayer setting :heavy_check_mark: 
* Label propagation algorithm :heavy_check_mark: 
* Leiden 
* Louvain Distributed version: https://ieeexplore.ieee.org/document/8425242
* Mining Bursting communities: https://arxiv.org/pdf/1911.02780.pdf

## Graph signal analysis
* Graph Fourier Transform 

## Graph comparison
* For temporal networks at different times 

## Kernels + Embeddings
* Deepwalk 
* Effective resistance 
* Eigenmap 
* Node2vec 
* Random walk with restart 

## Motifs
* 1 node 2-edge motifs :heavy_check_mark: 
* Clustering coefficient :heavy_check_mark: 
* I/O motifs (e.g. for transaction nets) :heavy_check_mark: (for motifs, one usually compares their number with that of aa properly randomised system, using e.g. a z score) 
* Reciprocity of edges :heavy_check_mark: 
* 3-node motifs :heavy_check_mark: 

## Pathing
* Binary diffusion :heavy_check_mark: 
* Cycle Detection :heavy_check_mark: 
* Maxflow :heavy_check_mark:
* Minimum Spanning Tree 
* Minimum Spanning Forest 
* Preferential Flows 
* Single source (DFS) Cycle 

## Reachability
* Average shortest path length 
* Connected components :heavy_check_mark: 
* Descendants/Ancestors of a node – time respecting :heavy_check_mark: 
* Graph diameter 
* Is there a path from A to B :heavy_check_mark: 
* Is there a time-respecting path from A to B :grapes: 
* Single source shortest path :heavy_check_mark: 
* Shortest path from A to B 
* Temporal connected components (based on temporal reachability) 

## Similarity
* Cosine 
* Jacard :grapes: 
* K Nearest Neighbour

## Spreading
* Linear consensus model, e.g. de Groot model 
* Random Walks :heavy_check_mark: 
* SI/SIR/SIS algorithms 
* Watts linear cascade :heavy_check_mark: 

## Temporal queries 
* Inter-event-time distribution for the nodes, and for the edges 
* List of inter-event times. For a given entity (or maybe globally) return a list of times between subsequent activities 
* Time since last activity :heavy_check_mark: 