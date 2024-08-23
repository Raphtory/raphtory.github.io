# Saving and loading graphs
The fastest way to ingest a graph is to load one from Raphtory's on-disk format using the `load_from_file()` function on the graph. This does require first ingesting via one of the prior methods and saving the produced graph via `save_to_file()`, but means for large datasets you do not need to parse the data every time you run a Raphtory script.
!!! info
    You can also [pickle](https://docs.python.org/3/library/pickle.html) Raphtory graphs, which uses these functions under the hood.

In the example below we ingest the edge dataframe from the last section, save this graph and reload it into a second graph. These are both printed to show they contain the same data.

{{code_block('getting-started/ingestion','save_load',[])}}

!!! Output

    ```python exec="on" result="text" session="getting-started/save_load"
    --8<-- "python/getting-started/ingestion.py:save_load"
    ```
