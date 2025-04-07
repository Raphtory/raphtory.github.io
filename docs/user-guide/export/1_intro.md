# Exporting and visualising your graph
As with Raphtory's connectors for ingesting data, there are a host of different formats and libraries that you can export your graphs into. Below we explore two of these, namely Pandas dataframes and NetworkX graphs.

All functions mentioned in this section work on both `graphs/nodes/edges` and `graph/node/edge views`, allowing you to specify different windows, layers and subgraphs before conversion. 

By default exporting will include all properties and all update history. However, this can be modified via flags on each export function, depending on use case requirements. You can find a description of these flags in the API docs for the function. 

!!! Info
    If we are missing a format that you believe to be important, please raise an [issue](https://github.com/Pometry/Raphtory/issues) and it will be available before you know it!

For the examples in this tutorial we are going to be reusing the network traffic dataset from the [ingestion tutorial](../ingestion/3_dataframes.md) and the monkey interaction network from the [querying tutorial](../querying/1_intro.md). In the below code segment you can get a refresher of what these datasets looks like. 

{{code_block('getting-started/export','ingest_data',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:ingest_data"
    ```
