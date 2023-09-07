# Exporting and visualising your graph
As with Raphtory's connectors for ingesting data, we also have a host of different formats and libraries that you can export your graphs into. Below we shall go over three of these, namely Pandas Dataframes, NetworkX graphs and PyVis graphs.

!!! Info
    This page doesn't contain an exhaustive list of all the different conversion methods - please feel free to check the [API documentation](https://docs.raphtory.com/) if that is what you are interested in. If we are missing a format that you believe to be important, please raise an [issue](https://github.com/Pometry/Raphtory/issues) and it will be available before you know it!

For the examples we are going to be using the network communication dataset from the [ingestion tutorial](ingestion.md), however, feel free to change this to any graph of your choosing in your own examples. In the below code segment you can get a refresher of what this data looks like.

{{code_block('getting-started/export','ingest_data',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:ingest_data"
    ```

## Exporting to Pandas Dataframes
{{code_block('getting-started/export','vertex_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:vertex_df"
    ```

{{code_block('getting-started/export','edge_df',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:edge_df"
    ```

## Exporting to NetworkX
{{code_block('getting-started/export','networkX',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:networkX"
    ```

### Visualisation

## Exporting to PyVis
{{code_block('getting-started/export','pyvis',['Graph'])}}

!!! Output

    ```python exec="on" result="text" session="export"
    --8<-- "python/getting-started/export.py:pyvis"
    ```

### Visualisation