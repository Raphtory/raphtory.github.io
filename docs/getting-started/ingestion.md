# Getting data into Raphtory

There are plenty of ways to get data into Raphtory and start running analysis. In this tutorial we are going to cover two of the most versatile, direct updating and loading from a Pandas Dataframe. 

## Creating a graph
To get started we first need to create a graph to store our data:

{{code_block('getting-started/ingestion','new_graph',['Graph'])}}
**Output:**
```python exec="on" result="text" session="getting-started/ingestion"
--8<-- "python/getting-started/ingestion.py:new_graph"
```

Printing this graph will show it as empty with no vertices, edges or update times.

## Direct Updates

Now that we have a graph we can directly update it with the `add_vertex` and `add_edge` functions.

### Adding vertices
To add a vertex we need a unique `id` to represent it and an update `timestamp` to specify when in the history of your data this vertex addition took place. In the below example we are going to add vertex `10` at timestamp `1`. 

!!! info

    If your data doesn't have any timestamps, don't fret! You can just set a constant value like `1` for all additions into the graph.  

{{code_block('getting-started/ingestion','vertex_add_1',[])}}
**Output:**
```python exec="on" result="text" session="getting-started/vertex_add_1"
--8<-- "python/getting-started/ingestion.py:vertex_add_1"
```
Printing out the graph and the returned vertex we can see it has been added to the graph.
As you might imagine, you can call this function when looping through any data source

#### What time formats you can ingest
{{code_block('getting-started/ingestion','vertex_add_2',[])}}

```python exec="on" result="text" session="getting-started/vertex_add_2"
--8<-- "python/getting-started/ingestion.py:vertex_add_2"
```

#### What types of ID you can have 

{{code_block('getting-started/ingestion','vertex_add_3',[])}}

```python exec="on" result="text" session="getting-started/vertex_add_3"
--8<-- "python/getting-started/ingestion.py:vertex_add_3"
```

#### Vertex properties

{{code_block('getting-started/ingestion','vertex_add_4',[])}}

```python exec="on" result="text" session="getting-started/vertex_add_4"
--8<-- "python/getting-started/ingestion.py:vertex_add_4"
```

#### What if my properties don't have a timestamp?

{{code_block('getting-started/ingestion','vertex_add_5',[])}}

```python exec="on" result="text" session="getting-started/vertex_add_5"
--8<-- "python/getting-started/ingestion.py:vertex_add_5"
```