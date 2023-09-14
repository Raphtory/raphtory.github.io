# Querying your graph

After reading in data to Raphtory, we can now make use of the graph representation to ask some interesting questions. For this tutorial, we will use a dataset from [SocioPatterns](http://www.sociopatterns.org/datasets/baboons-interactions/), comprising different behavioural interactions between a group of 22 baboons over a month. 

!!! info 
    If you want to read more about the dataset, you can check it out in this paper: [V. Gelardi, J. Godard, D. Paleressompoulle, N. Claidière, A. Barrat, “Measuring social networks in primates: wearable sensors vs. direct observations”, Proc. R. Soc. A 476:20190737 (2020)](https://royalsocietypublishing.org/doi/10.1098/rspa.2019.0737). 

In the below code we load this dataset into a dataframe and do a small amount of preprocessing to prepare it for loading into Raphtory. This includes dropping rows with blank fields and mapping the values of the `behaviour category` into a `weight` which can be aggregated. The mapping consists of the following conversions:

* Affiliative (positive interaction) → `+1`
* Agonistic (negative interaction) → `-1` 
* Other (neutral interaction) → `0`

{{code_block('getting-started/querying','read_data',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:read_data"
    ```

Next we load this into Raphtory using the `load_edges_from_pandas` function, modelling it as a weighted multi-layer graph, with a layer per unique `behaviour`. 

{{code_block('getting-started/querying','new_graph',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:new_graph"
    ```
 
## Graph metrics and functions

### Basic metrics
Now that we have our graph let's start probing it for some basic metrics, such as how many nodes and edges it contains and the time range over which it exists. 

Note, as the property APIs are the same for the graph, vertices and edges, these are discussed together in [property queries](#property-queries) below.

!!! info
    In the below code segment you will see the functions `num_edges` and `num_temporal_edges` being called and returning different results. This is because `num_edges` returns the number of unique edges and `num_temporal_edges` returns the total edge updates which have occurred. 
    
    The second is useful if you want to imagine each edge update as a separate connection between the two nodes. The edges can be accessed in this manner via `edge.explode()`, as is discussed in [edge metrics and functions](#edge-metrics-and-functions) below.

{{code_block('getting-started/querying','graph_metrics',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:graph_metrics"
    ```

### Accessing vertices and edges  
Three types of functions are provided for accessing the vertices and edges within the graph: 

* **Existance check:** Via `has_vertex()` and `has_edge()` you can check if an entity is present within the graph.
* **Direct access:** `vertex()` and `edge()` will return a vertex/edge object if the entity is present and `None` if it is not.
* **Iterable access:** `vertices()` and `edges()` will return iterables for all vertices/edges which can be used within a for loop or as part of a [function chain](#chaining-functions).

All of these functions are shown in the code below and will appear in several other examples throughout this tutorial.

{{code_block('getting-started/querying','graph_functions',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:graph_functions"
    ```


## Vertex metrics and functions
Vertices can be accessed by storing the object returned from a call to `add_vertex()`, by directly asking for a specific node via `vertex()`, or by iterating over all nodes via `vertices()`. Once you have a vertex, we can ask it some questions. 

### Update history 

Vertices have functions for querying their earliest/latest update time (as an epoch or datetime) as well as for accessing their full history (`history()`). In the code below we create a vertex object for `Felipe` and see when their updates occurred. 

{{code_block('getting-started/querying','vertex_metrics',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:vertex_metrics"
    ```


### Neighbours, edges and paths
To investigate who a vertex is connected with we can ask for its `degree()`, `edges()`, or `neighbours()`. As Raphtory is a directed graph all of these functions also have an `in_` and `out_` variation, allowing you get only incoming and outgoing connections respectively. These functions return the following:

* **degree:** A count of the number of unique connections a vertex has.
* **edges:** An iterable (`Edges`) of edge objects, one for each unique `(src,dst)` pair.
* **neighbours:** An iterable of vertex objects (`PathFromVertex`), one for each node the vertex shares an edge with.

In the code below we call a selection of these functions to show the sort of questions you may ask. 

!!! info

    The final section of the code makes use of `v.neighbours().name().collect()` - this is a chain of functions which are run on each vertex in the `PathFromVertex` iterable. We will discuss these sort of operations more in [Chaining functions](#chaining-functions) below. 

{{code_block('getting-started/querying','vertex_neighbours',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:vertex_neighbours"
    ```

## Edge metrics and functions 
Edges can be accessed by storing the object returned from a call to `add_edge()`, by directly asking for a specific edge via `edge()`, or by iterating over all edges via `in-edges()`/`out-edges()`/`edges()`. 

### Edge structure and update history
An edge object in Raphtory will by default contain all updates over all layers between the given source and destination vertices. As an example of this, we can look at the two edges between `FELIPE` and `MAKO` (one for each direction). 

In the code below we create the two edge objects by requesting them from the graph and then print out the layers each is involved in via the `layer_names()` function. We can see here that there are multiple behaviours in each direction represented within the edges.

Following this we access the history and earliest/latest update time, as we have previously with the graph and vertices. This update history consists all interactions across all the aforementioned layers.

!!!info 
    Note that we call `e.src().name()` because `src()` and `dst()` return a vertex object, instead of just an id/name.

{{code_block('getting-started/querying','edge_history',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:edge_history"
    ```

### Exploded edges
The very first question you may have after reading this is "What if I don't want all of the layers?". For this Raphtory offers you three different ways to split the edge, depending on your use case:

* `.layers()`: which takes a list of layer names and returns a new `Edge View` which only contains updates for the specified layers - This is discussed in more detail in the [Graph views](#graph-views) section below.
* `.explode_layers()`: which returns an iterable of `Edge Views`, each containing the updates for one layer.
* `.explode()`: which returns an `Exploded Edge` containing only the information from one call to `add_edge` i.e. an edge object for each update. 

In the code below you can see usage of all of these functions. We first call `explode_layers()`, seeing which layer each edge object represents and output its update history. Next we fully `explode()` the edge and see each update as an individual object. Thirdly we use the `layer()` function to look at only the `Touching` and `Carrying` layers and chain this with a call to `explode()` to see the updates within these individually. 

!!! info
    Within the examples and in the API documentation you will see singular and plural versions of the same functions (i.e. `.layer_names()/.layer_name()` `.history()/.time()`) these singular versions are simply helpers which return only the first value of the list for when you know an edge is exploded and will only have one value. 

{{code_block('getting-started/querying','edge_explode_layer',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:edge_explode_layer"
    ```


## Property queries
As you will have seen in the [ingestion tutorial](ingestion.md), graphs, vertices and edges may all have `constant` and `temporal` properties, consisting of a wide range of data types. Raphtory provides a unified API for accessing this data via the [Properties](https://docs.raphtory.com/en/master/#raphtory.Properties) object available on all classes by calling `.properties`. 

This `Properties` class offers several functions for you to access the values you are interested in in the most appropriate format. To demonstrate this let's create a simple graph with one vertex that has a variety of different properties, both temporal and constant. 

We can grab this vertices property object and call all of the functions to access the data:

* `keys()`: Returns all of the property keys (names).
* `values()`: Returns the latest value for each property.
* `items()`: Combines the `keys()` and `values()` into a list of tuples.
* `get()`: Returns the latest value for a given key if the property exists or `None` if it does not.
* `as_dict()`: Converts the `Properties` object into a standard python dictionary.

The `Properties` class also has two attributes `constant` and `temporal` which have all of the above functions, but are restricted to only the properties which fall within their respective catagories. The API and semantics for [ConstProperties](https://docs.raphtory.com/en/master/#raphtory.ConstProperties) are exactly the same as described above. [TemporalProperties](https://docs.raphtory.com/en/master/#raphtory.TemporalProperties) on the other hand allow you to do much more, as is discussed below.

{{code_block('getting-started/querying','properties',['Vertex'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:properties"
    ```

### Temporal specific functions
As temporal properties have a history, we may often want to do more than just look at the latest value. As such, calling `get()`, `values()` or `items()` on `TemporalProperties` will return a [TemporalProp](https://docs.raphtory.com/en/master/#raphtory.TemporalProp) object which contains all of the value history.

`TemporalProp` has a host of helper functions covering anything that you may want to do with this history. This includes:

* `value()`/`values()`: Get the latest value or all values of the property.
* `at()`: Get the latest value of the property at the specified time.
* `history()`: Get the timestamps of all updates to the property.
* `items()`: Merges `values()` and `history()` into a list of tuples.
* `mean()`/`median()`/`average()`: If the property is orderable, get the average value for the property.
* `min()`/`max()`: If the property is orderable, get the minimum or maximum value.
* `count()`: Get the number of updates which have occurred
* `sum()`: If the property is additive, sum the values and return the result.

In the code below, we call a subset of these functions on the `Weight` property of the edge between `FELIPE` and `MAKO` in our monkey graph.

{{code_block('getting-started/querying','temporal_properties',['Edge'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:temporal_properties"
    ```


## Chaining functions

When we called `v.neighbours()` [earlier](#neighbours-edges-and-paths), a `PathFromVertex` was returned rather than a straightforward list. This, along with all other iterables you have seen above (`Vertices`,`Edges`,`Properties`,etc.) are [lazy](https://en.wikipedia.org/wiki/Lazy_evaluation) data structures which allow you to chain multiple functions together before a final execution. 

For example, for a vertex `v`, `v.neighbours().neighbours()` will return the two-hop neighbours. The first call of `neighbours()` returns the immediate neighbours of `v`, the second applies the`neighbours()` function to each of the vertices returned by the first call. These are then flattened under the hood such that a single `PathFromVertex` is returned. 

We can continue this chain for as long as we like, with any functions in the Vertex, Edge or Property API until we either: 

* Call `.collect()`, which will execute the chain and return the result.
* Execute the chain by handing it to a python function such as `list()`, `set()`, `sum()`, etc.
* Iterate through the chain via a loop/list comprehension.

We can see a basic example of these function chains below in which we get the names of all the monkeys, the names of their two-hop neighbours, zip these together and print the result.

{{code_block('getting-started/querying','function_chains',['Edges'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:function_chains"
    ```

### Chains with properties
To demonstrate some more complex questions that you could ask our monkey graph, we can include some property aggregation into our chains. 

In the code below we sum the `Weight` value of each of `Felipe's` out-neighbours to rank them by the number of positive interactions he has initiated with them. Following this find the most annoying monkey by ranking globally who on average has had the most negative interactions initiated against them.


{{code_block('getting-started/querying','friendship',['Edges'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:friendship"
    ```

## Graph views
All of the operations we have discussed up to this point have been executed on the whole graph, including the full history. In this section we will look at applying `Graph Views` which provide a way to look at the subset of this data without having to reingest it. 

Raphtory can maintain hundreds of thousands of `Graph Views` in parallel, allows chaining view functions together to create as specific a filter as is required for your use case, and provides a unified API such that all functions mentioned can be called on a graph, vertex or edge.

### Querying the graph over time
The first set of views we will look at are for traveling through time, viewing the graph as it was at a specific point, or between two points (applying a time window). For this Raphtory provides four functions: `at()`, `window()`, `expand()` and `rolling()`.

#### At

The `at()` function takes a `time` argument in epoch (integer) or datetime (string/datetime object) format and can be called on a graph, vertex, or edge. This will return an equivalent `Graph View`, `Vertex View` or `Edge View` which includes all updates between the beginning of the graphs history and the provided time (**inclusive of the time provided**). 

This returned object has all of the same functions as its unfiltered counterpart and will pass the view criteria onto any entities it returns. For example if you call `at()` on a graph and then call `vertex()`, this will return a `Vertex View` filtered to the time passed to the graph.

An example of this can be seen in the code below where we print the degree of `Lome` on the full dataset, at 9:07 on the 14th of June and at 12:17 on the 13th of June.

!!! info 

    You will see in these function calls that we can both do `graph.at().vertex()` and `graph.vertex().at()` and the same results can be achieved.

We also introduce two new time functions here, `start()` and `end()`, which specify the time range a view is filtered to, if one has been applied. You can see in the last line of the example we print the `start`, `earliest_time`, `latest_time` and `end` of the vertex to show you how these differ.

{{code_block('getting-started/querying','at',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:at"
    ```


#### Window
The `window()` function works the same as the `at()` function, but allows you to set a `start` time as well as an `end` time (**inclusive of start, exclusive of end**). 

This is useful for digging into specific ranges of the history that you are interested in, for example a given day within your data, filtering everything else outside this range. An example of this can be seen below where we look at the number of times `Lome` interacts wth `Nekke` within the full dataset and for one day between the 13th of June and the 14th of June.

!!! info
    We use datetime objects in this example, but it would work exactly the same with string dates and epoch integers.

{{code_block('getting-started/querying','window',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:window"
    ```


#### Expanding
If you have data covering a large period of time, or have many time points of interest, it is quite likely you will find yourself calling `at()` over and over. If there is a pattern to these calls, say you are interested in how your graph looks every morning for the last week, you can instead utilise `expanding()`. 

`expanding()` will return an iterable of views as if you called `at()` from the earliest time to the latest time at increments of a given `step`. 

The step can be given as a simple epoch integer, or a natural language string describing the interval. For the latter, this is converted it into a iterator of datetimes, handling all corner cases like varying month length and leap years.

Within the string you can reference `years`, `months` `weeks`, `days`, `hours`, `minutes`, `seconds` and `milliseconds`. These can be singular or plural and the string can include 'and', spaces, and commas to improve readability. 

In the code below, we can see some examples of this where we first increment through the full history of the graph (one month) a week at a time. This creates four views, each of which we ask how many monkey interactions it has seen. You will notice the start time doesn't not change, but the end time increments by 7 days each view.

The second example shows the complexity of increments Raphtory can handle, stepping by `2 days, 3 hours, 12 minutes and 6 seconds` each time. We have additionally bounded this expand via a window between the 13th and 23rd of June to demonstrate how these views may be chained.

{{code_block('getting-started/querying','expanding',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:expanding"
    ```

#### Rolling 
Where `at()` has `expanding()`, `window()` has `rolling()`. This function will return an iterable of views, incrementing by a `window` size and only including the history from inside the window period (**Inclusive of start, exclusive of end**). This allows you to easily extract metrics like daily or monthly activity.

 For example, below we take the code from [expanding](#expanding) and swap out the function for `rolling()`. In the first loop we can see both the start date and end date increase by seven days each time, and the number of weekly interactions sometimes decreases as older data is dropped from the window.

{{code_block('getting-started/querying','rolling_intro',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:rolling_intro"
    ```

Alongside the window size, `rolling()` takes an option `step` argument which specifies how far along the timeline it should increment before applying the next window. By default this is the same as `window`, allowing all updates to be analysed exactly once in non-overlapping windows. 

If, however, you would like to have overlapping or fully disconnected windows, you can set a `step` smaller or greater than the given `window` size. For example, in the code below we add a `step` of two days. You can see in the output the start and end dates incrementing two days each view, but are always seven days apart.  


{{code_block('getting-started/querying','rolling_intro_2',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:rolling_intro_2"
    ```

As a small example of how useful this can be, in the following segment we plot the daily unique interactions of `Lome` via `matplotlib` in only 10 lines! 

!!! info
    We have to recreate the graph in the first section of this code block so that the output can be rendered as part of the documentation. Please ignore this. 


{{code_block('getting-started/querying','rolling',[])}}

### Layered graphs
!!!info 
    Edge layers have been discussed several times, notably in [Ingestion](ingestion.md#edge-layers) and [Exploded Edges](#exploded-edges). Please check these before reading this section.

 As previously discussed, an edge object by default will contain information on all layers between its source and destination vertices. However, it is often the case that there are a subset of these relationships that we are interested in. To handle this the `Graph`, `Vertex` and `Edge` provide the `layers()` function. 

 This takes a list of layer names and returns an view with only edge updates that occurred on these layers. Layer views will pass their restrictions on to any object they return (as with the time views) and can be used in combination with any other view function.

 As an example of this in the code below we look at the total edge weight over the full graph, then restrict this to the `Grooming` and `Resting` layers and then reduce this further by applying a window between the 13th and 20th of June.

{{code_block('getting-started/querying','layered',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:layered"
    ```

### Subgraph
Similar to only being interested in a subset of edge layers, for some use cases we may only be interested in a subset of vertices within the graph. One solution to this could be to call `g.vertices()` and filter this before continuing your workflow. However, this does not remove anything for later calls to `neighbours()`, `edges()`, etc. Meaning you will have to constantly recheck these lists. 

To handle all of these corner cases Raphtory provides the `subgraph()` function which takes a list of nodes of interest. This applies a view such that all vertices not in the list are hidden from all future function calls. This also hides any edges linked to hidden vertices to keep the subgraph consistent. 

In the below example we demonstrate this by looking at the neighbours of `FELIPE` in the full graph, vs a subgraph of `FELIPE`, `LIPS`, `NEKKE`, `LOME` and `BOBO`. We also show how that `subgraph` can be combined with other view functions, in this case a window between the 17th and 18th of June.


{{code_block('getting-started/querying','subgraph',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:subgraph"
    ```

### Materialize
All of the view functions mentioned hold zero updates of their own, simply providing a lens through which to look at the original graph you ingested into. This is by design so that we can have many of them without our machines exploding from data duplication. 

This does mean, however, if the original graph is updated, all of the views over it will also update. If you do not want this to happen you may `materialize()` a view, creating a new graph and duplicating all the updates the view contains into it. 

Below we can see an example of this where we create a windowed view between the 17th and 18th of June and then materialize this. After adding a new monkey interaction in the graph, we can see the original view now contains this new update, but our materialized one does not.

{{code_block('getting-started/querying','materialize',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:materialize"
    ```