---
layout: page
title: Raphtory Overview
permalink: /about/
---

This page will give you a full run through of what we are up to with the Raphtory project. There is quite a lot of info here, but its broken up with a couple of pit stops along the way. Check out the summary section at the top ([Raphtory from 10,000ft](#raphtory-from-10-000ft)) and from there you can pivot into our tutorial or dive into the details!

![]({{ site.baseurl }}/images/about/diving.gif)

# Table Of Contents

- [Raphtory from 10,000ft](#raphtory-from-10-000ft)
  * [What questions can I ask?](#what-questions-can-i-ask-)
  * [How do I get my data in and insights out?](#how-do-i-get-my-data-in-and-insights-out-)
  * [How do I actually run it?](#how-do-i-actually-run-it-)
- [Lets take a quick breather](#-warning--lets-take-a-quick-breather--warning-)
- [Lets dive back in!](#---lets-dive-back-in----)
  * [The Graph Model](#the-graph-model)
  * [Ingestion Components](#ingestion-components)
  * [Analysis Components](#analysis-components)
- [Analysis in Raphtory](#analysis-in-raphtory)
- [What’s going on under the hood](#what-s-going-on-under-the-hood)
- [Deployment](#deployment)
- [Finished!](#-fireworks--finished---fireworks-)

# Raphtory from 10,000ft
Data is at the heart of decision making today, and graphs are firmly embedded in the modern data stack. From fraud detection and drug discovery to market and supply modelling, graphs enable previously unachievable insights. However, while graph analytics platforms are increasingly used across the industry, most applications and solutions overlook a crucial element: time. 
 
Current solutions focus solely on the latest version of the data - missing out on how it has arrived at the state it is in today. 

Temporal graphs embed the full history of data, keeping track of every change that has ever occurred. This enables organisations to understand the order of interactions, investigate the evolution of the network over time, and control for risk or prepare for future trends.

In social networks, this can help us understand the outreach of marketing campaigns or, contrarily, control the spread of fake news. In finance, it helps identify emerging markets and allows for a timely response to financial crime. In supply chains, it brings to light highly coupled dependencies and how service outages may impact delivery. 
 
From its inception, Raphtory was developed to fill this clear gap in analytical capabilities. Time is a cornerstone of our graph storage model and integrates seamlessly into the analysis you wish to run. 

## What questions can I ask?

Raphtory is an analytics platform which combines the capabilities of a graph structure with time-series analysis, providing a powerful model for extracting new insights from your data. 

Within this new paradigm you may run traditional analysis from either domain, extracting shortest paths and community groupings from the graph world, or detect trends and anomalies via time-series. However, where things get interesting is that these can be freely combined. This allows you to look for time-respecting paths through your data, model the evolution of communities over time or extract temporal patterns in the interactions between entities in the network. 

Not only will this expose entirely new contextual insights within your data, but by working with time-respecting patterns you actually shrink the search space of classic graph algorithms, drastically reducing run-times.

Once an algorithm is defined (and plenty are available out of the box) it may be run on any point in the history of your data, with Raphtory creating an exact view of what the graph would have looked like to execute on. This can then be expanded to ranges of time, with sets of windows, exploring the evolution of your metrics in the short, medium and long term. 

## How do I get my data in and insights out?
Whilst this way of viewing data is very exciting, it would be no use if getting anything in or out of the platform was a total pain. As such, Raphtory's secondary objective is to make transitioning into the graph world as easy as possible.

With this in mind we have created an ingestion pipeline which allows you to leave your data stored wherever you currently have it, be that on disk or in the cloud. This can then be quickly loaded it into Raphtory whenever you want to get some graphy insights. $Raw data \rightarrow Graph$ is specified by one simple function with Raphtory handling everything else, no matter the size of the data.

On the other side, getting your results out is handled much the same way, requiring you only to choose the destination system (file, database, stream, etc.) and format (csv,Json,domain specific, etc.). All results are then neatly tagged with the timepoint they run at and any window that was applied. 

## How do I actually run it?

Raphtory is a [Scala](https://www.scala-lang.org) based tool which is fully distributed and decentralised, scaling to billions of records in minutes. All this requires is a `Raphtory Service` definition (one class) which can then be deployed automatically on bare metal or containerised via Kubernetes. We have a fantastic set of tutorials to walk you through this, and a wonderful community always ready to help!

P.S. For those of you who can't imagine working outside Python, the next Raphtory release will have a full working Python interface :snake:.

# :warning: Lets take a quick breather :warning:

![]({{ site.baseurl }}/images/about/phew.gif)

That was a pretty intense wirlwind tour of Raphtory and I just wanna check in. If that's quite enough reading for you, can I recommend you check out our most recent talk on Raphtory at <a href="https://www.youtube.com/watch?v=7S9Ymnih-YM&list=PLuD_SqLtxSdVEUsCYlb5XjWm9D6WuNKEz&index=9">AIUK</a>. This gives a good overview of Raphtory and some use cases where we have applied it.  

If you are more than convinced this is the tool for you and you can't wait to get your teeth into it, head on over to the [docs](https://docs.raphtory.com) where the tutorials will walk you through everything required. If you run into any issues, you can reach the team and community on our [Slack](https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA)!

If you cannot be swayed and want to learn more...

# 🤿 Lets dive back in! 🤿

## The Graph Model
Raphtory’s model is very similar to the property graph model that you may have seen in other graph systems. There are vertices (entities) and edges (relationships), both of which can have a `type` and a set of key/value properties dictating their characteristics. 

Raphtory improves on this model by further tracking every update that occurs and when they occur. These updates are recorded in a chronological log maintaining the full property and relationship history of all entities (as opposed to overwriting the information when new data arrives). This in turn allows for a complete historic exploration of the graph.

![]({{ site.baseurl }}/images/about/model.png)

The figure above shows an example of a Raphtory graph being built from social network data. In this instance there are two clear pieces of information which would be lost in a traditional graph system. 

First, both of the vertices (people) update their occupations to new jobs, which would overwrite the prior value. Second, although they were historically and are currently friends, there was a period of time (between t5 and t6) where this relationship soured. Interrogation of the evolution of this relationship and of similar relations across the entire network would not normally be possible.

## Ingestion Components

![]({{ site.baseurl }}/images/about/components.png)

To facilitate the building of temporal graphs, Raphtory is composed of several decoupled components which may be independently scaled out (horizontally and vertically) depending on the use case at hand. These components can be seen in the above figure, and are split between ingestion and modelling (left) and analysis (right). 

For ingestion, Raphtory supports a full ETL/ELT (extract, transform, load) pipeline. This consists of:
*	`Spouts` which provide the entry point for data. These can pull from any data source, be that data on disk, remote storage or streams. Once ingested the `Spout` will push the loaded data downstream to the `Graph Builders`.
*	`Graph Builders` convert this raw data into the graph updates we saw in the model (adding/removing/updating vertices/edges) via a user defined function. 

![]({{ site.baseurl }}/images/about/partitions.png)

Once the updates are transformed, they are forwarded into the `Partition Managers` which are in charge of storing and maintaining a portion of the overall graph - allowing it to scale beyond the memory of a single machine. All routing of updates and synchronisation of the graph state between partitions is handled fully within Raphtory. 

Additionally, due to the temporal model of Raphtory, out-of-order updates are of no concern (unlike in a database where ACID compliance is critical to producing the right state). No matter what order the updates arrive in the same graph will be created as everything is sorted chronologically. 

### Running Ingestion (Batch and Stream)
Raphtory supports two ingestion paradigms, batch and stream ingestion. In the Streaming pipeline Raphtory continuously ingests updates from a stream of data, enabling real-time analysis on the latest version of the graph. In this mode `Spouts` and `Builders` may be shut down when no new data is available, leaving the partitions to be analysed. When more data is identified, the user may reinstate the `Spout` and `Builders` to stream in the new data. Alternatively new `Spouts` for different data sources may be connected to the running Raphtory deployment, merging their data into the same graph.

In Batch mode, Raphtory quickly ingests large amounts of pre-collected data into the system. This is useful for an initial historical bulk ingestion, or when your data is unordered and you want this to be handled by Raphtory. Once the data is fully ingested the partitions will enable analysis, allowing all users to run queries as and when required. The user man then additionally attach a new streaming `Spout` and `Builder` pair to begin adding fresh data on top.

## Analysis Components
The analytical engine for Raphtory is similarly developed to work in a highly scalable decentralised fashion. The primary component here is the Query Manager which is responsible for accepting, scheduling and executing user queries and algorithms. 

Each time a user submits an algorithm, a new Query Handler is spawned within the cluster. This handler is in charge of orchestrating the analysis across the partitions, generating the perspectives of the graph (views of the graph through time), performing any global aggregations and returning the results to the user. Once the chosen algorithm has completed on all perspectives the handler will clean up all temporary state it has generated, return all compute resources allocated and shutdown. 


# Analysis in Raphtory
As a key feature of Raphtory’s design goals was to ensure it could scale to the largest of datasets, algorithms had to be fully distributable. To enable this, we adopted the `think like a vertex` model, where computation is completed in synchronised supersteps. Within these steps all vertices execute independently, communicating via messages, and can therefore be spread across any number of machines.

![]({{ site.baseurl }}/images/about/thinklikeavertex.png)

Algorithms in this form consist of each vertex receiving some information from its neighbours, calculating some new state for itself based on this received information, and optionally forwarding this state out to neighbours to be used in the next step. This process may continue for a pre-defined number of steps or until a convergence criterion is met, at which point the results will be returned. This workflow can be seen in the figure above. 

![]({{ site.baseurl }}/images/about/api.png)

Raphtory’s Analysis API can be envisioned as three distinct layers which combine to provide a simple manner of interacting with both the graph structure and historic state. This consists of: The Vertex State layer, The Algorithm Structure layer, and The Time Selection layer. See figure above.

## Vertex State
Beginning at the lowest of these, the Vertex State layer provides: 
*	Access to the property and update history of each vertex and its edges.
*	Functions for messaging incoming/outgoing neighbours in the present, past and future.
*	Storage of algorithmic state local to the vertex or as part of a global aggregate.
*	Several helper functions to examine the history as a time-series, automatically aggregate edge weightings, etc.  

## Algorithm Structure
To add some structure to these individual vertex operations the Algorithm Structure layer defines the stages to be completed via `Step` and `Iterate` functions. This specifies the flow of an algorithm from setup to final convergence, upon which the user may `Select` the elements of interest from each vertex to be written out. 

```scala
class ConnectedComponents extends NodeList(Seq("cclabel")) {

  override def apply(graph: GraphPerspective): graph.Graph =
    graph
      .step { vertex =>
        vertex.setState("cclabel", vertex.ID)
        vertex.messageAllNeighbours(vertex.ID)
      }
      .iterate(
              { vertex =>
                import vertex.IDOrdering
                val label = vertex.messageQueue[vertex.IDType].min
                if (label < vertex.getState[vertex.IDType]("cclabel")) {
                  vertex.setState("cclabel", label)
                  vertex.messageAllNeighbours(label)
                }
                else
                  vertex.voteToHalt()
              },
              iterations = 100,
              executeMessagedOnly = true
      )

}
```

As a concrete example, above is Raphtory’s implementation of `Connected Components` in Scala. The goal of this algorithm is to work out which `component` each vertex belongs to, where a component is a set of nodes which all have a path to each other. This is useful for identifying communities, entity resolution, inter-dependencies and more.

#### Code explanation

The algorithm begins via a setup `Step` where each vertex sets its component label as its own ID and then sends this to all its neighbours. Following this is a multi-step `Iterate` where each vertex calculates the minimum label it has received and, if this is less than its own label, will now adopt this value and propagate on to its neighbours. If no lower label is received the vertex will instead vote to halt (believes it has converged). Via these two simple stages the lowest ID propagates throughout each component, with all reachable vertices adopting it. A similar process can be seen in our algorithms for Community Detection, Taint Tracking and more.

## Time Selection
Once an algorithm has been defined it can be applied at any point in the history of the graph via the Time Selection layer. Here we can specify a slice of the history we are interested in, set an increment with which to traverse this range, and optionally set windows of varying sizes to investigate both short- and long-term patterns.

```scala
graph
    .range("2020-01-01","2021-01-01","1 day")
    .window(["1 day","1 week","1 month"])
    .execute(ConnectedComponents())
    .writeTo(FileSink("outputdir"))
```

Each unique combination of time points and windows generates a specific Perspective of the graph upon which the algorithm is applied and results returned. For example in the above query, Connected Components is run over a year of data, once per day, looking back one day, one week and one month. Unlike its static counterpart, temporal connected component goes further to also shed light on emerging communities, recurring patterns (money laundering) and identity evolution. 

## Sinks and Formats

Finally, once you are happy with your algorithm and query you can easily set the location and format for your output. This is done by using a `Sink` which is given to the query when it is executed. Several inbuilt output formats are available within Raphtory, but it is also simple to implement your own if you have a specific destination in mind.

As an example, in our prior code snippet the `FileSink` saves the results of each partition as separate files in a directory `outputdir`. This directory is the only manditory argument required when creating the `FileSink` object and passing it to the query. We can, however, add an optionl argument of a `Format` for the data. This can be seen in the first line below where a `JSONFormat` is provided which will override the default `CSVFormat`. 

A `Format` specifies how to serialise on a per query, per pespective and per vertex basis. This allows for simple formats, such as the `CSVFormat` outputting one line per vertex, or much more complicated formats such as the `JSONFormat(JsonFormat.GLOBAL)` where the entire query is serialised as one valid JSON object. 

```scala 
FileSink("/tmp/raphtory", JsonFormat())
PulsarSink("connected component results",CSVFormat())
S3Sink("s3/bucket",JSONFormat(JsonFormat.GLOBAL))
```

## Prepackaged algorithms
![]({{ site.baseurl }}/images/about/algorithms.png)

Finally, whilst it is very much encouraged to jump into these API’s and start creating your own algorithms, Raphtory’s open-source community has been hard at work expanding the algorithmic library to cover a wide variety of traditional and temporal graph algorithms. 

Today we stand at 40+ open-source algorithms, and more with close-source highly optimised algorithms. These are all full [documented](https://docs.raphtory.com/en/master/_autodoc/com/raphtory/algorithms/generic/index.html) and can be used as is or as a starting point for creating your own. 

# What’s going on under the hood

Communication between Raphtory's components is managed by [Apache Pulsar](https://pulsar.apache.org), a high performance, scalable pub/sub broker for ETL workflows. We have tuned Pulsar specifically for graph workloads, reaching up to 100,000 operations per second, per machine (5 times quicker than Kafka). Unlike other systems Pulsar supports built-in ACID compliance through its underlying BookKeepers; a highly scalable, sharded, transaction log for data persistence. This means that no data will ever be lost during real-time streaming!

However, to make proof of concepts and testing more lightweight, Raphtory also has a local mode where components communicate via [Akka](https://akka.io), requiring no external services. These are both managed via a communication layer abstraction we call the `Topic Repository` where the components publish messages to topics unaware of the actual medium of communication. In later versions of Raphtory this layer will be exposed to the end user allowing them to run Raphtory ontop of any messaging service (Kafka, RabbitMQ, etc.) further simplifying integration with their current stack.

## Trinio
Alongside allowing Raphtory to provide seamless real-time data refreshes, integration with Apache Pulsar’s persistent Bookies also allows for real-time alerting/querying via the distributed sql engine [Trino](https://trino.io). An example of this running live on Ethereum blocks can be seen below. Simply put, Trino doesn’t just enable SQL analysis, it also enables real-time monitoring of watchlists, and enables the user to trigger analytics in Raphtory to provide valuable first to market insights.

![]({{ site.baseurl }}/images/about/trinio.png)


# Deployment
Whilst it is important for Ingestion and Analysis to run fast, from our own experience with other graphy/big data tools, that doesn’t matter if you can’t get a platform to deploy properly. We have put a lot of work into making Raphtory’s deployment process as smooth as possible.

```scala 
 val source  = FileSpout(path)
 val builder = new LOTRGraphBuilder()
 val graph   = Raphtory.load(spout = source, graphBuilder = builder)
 val output  = FileSink("/tmp/raphtory")

 val queryHandler = graph
    .at(32674)
    .past()
    .execute(DegreesSeparation())
    .writeTo(output)

 queryHandler.waitForJob()
```

As it is written in Scala, in its simplest form Raphtory may be imported into your project as a maven dependency and run locally without any other requirements. All you need to do is define your Spout and Builder and start submitting queries, as can be seen in the code snippets above (taken from our tutorial). And of course, the code may be compiled into a Jar and run on bare metal anywhere the user desires.  

```scala 
object LOTRService extends RaphtoryService[String] {

  override def defineSpout(): Spout[String] = FileSpout("/tmp/lotr.csv")

  override def defineBuilder: LOTRGraphBuilder = new LOTRGraphBuilder()

}
```

To run Raphtory in a distributed mode we instead define a `RaphtoryService` which contains the same information as the Local graph but can instead be used to deploy singular components (`Spouts`, `Builders`, `Partitions`, etc.) across a large, distributed cluster.

Alongside the open-source deployment options, [Pometry](https://www.pometry.com) provides the ability to containerise (through Kubernetes) and automate deployments through custom Ansible, Terraform and Helm scripts. This allows organisations to deploy, ingest, execute analysis, and write out results in the click of a button. 

Below is a screenshot of Raphtory running in a Kubernetes against the Ethereum data queried by Trinio. The code for this Ethereum graph and Kubenetes Deployment can be found in the [examples repo.](https://github.com/Raphtory/Raphtory/tree/master/examples/raphtory-example-ethereum)

![]({{ site.baseurl }}/images/about/Kube.png)


## Monitoring and Logging
Raphtory offers monitoring and logging directly integrated with popular solutions such as Grafana, Kibana and Prometheus. This includes information on memory and cpu utilisation, latency, graph level metadata (e.g. node and edge count), number of spouts, builders and partition managers, number of analysis jobs running, their query times, progress tracking and more. 

If deployed as a streaming solution, Raphtory will also report broker and consumer level metrics such as number of updates being published a second, backlog count, network latency, read and write latency to disk (if persistent). An example of these dashboards can be seen below containing the topics for the Ethereum deployment. 

![]({{ site.baseurl }}/images/about/graphana.png)

Finally, as Raphtory is deployable through Kubernetes, cluster, and pod level kube metrics are directly available at Grafana and REST level. Reporting heartbeat, health status, uptime, memory, and CPU usage, and other Kubernetes related data.

## Logging
Similar to monitoring, `Spout` (batch and stream), `Builder` and `Analysis` logs are available at all levels, making it easy to understand what is happening in the system and to debug potential bugs, performance issues or track running jobs. 

While this information is available directly at a deployment level, we also offer the ability to scrape this information and load into services such as Kibana for alerting and querying purposes. 


# :fireworks: Finished! :fireworks:
![]({{ site.baseurl }}/images/about/finish.gif)

Thanks for sticking with us to the end! I hope think has helped you understand what we are trying to build and are excited to get your data into Raphtory. If so, get into the [docs](https://docs.raphtory.com) and come say [hello](https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA)!