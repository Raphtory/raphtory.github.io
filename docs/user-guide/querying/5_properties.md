
# Property queries
As you will have seen in the [ingestion tutorial](../ingestion/2_direct-updates.md), graphs, nodes and edges may all have `constant` and `temporal` properties, consisting of a wide range of data types. Raphtory provides a unified API for accessing this data via the `Properties` object available on all classes by calling `.properties`. 

This `Properties` class offers several functions for you to access the values you are interested in in the most appropriate format. To demonstrate this let's create a simple graph with one node that has a variety of different properties, both temporal and constant. 

We can grab this nodes property object and call all of the functions to access the data:

* `keys()`: Returns all of the property keys (names).
* `values()`: Returns the latest value for each property.
* `items()`: Combines the `keys()` and `values()` into a list of tuples.
* `get()`: Returns the latest value for a given key if the property exists or `None` if it does not.
* `as_dict()`: Converts the `Properties` object into a standard python dictionary.

{{code_block('getting-started/querying','properties',['Node'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:properties"
    ```


The `Properties` class also has two attributes `constant` and `temporal` which have all of the above functions, but are restricted to only the properties which fall within their respective catagories. 

!!! info
    The semantics for `ConstantProperties` are exactly the same as described above. `TemporalProperties` on the other hand allow you to do much more, as is discussed below.

## Temporal specific functions
As temporal properties have a history, we may often want to do more than just look at the latest value. As such, calling `get()`, `values()` or `items()` on `TemporalProperties` will return a `TemporalProp` object which contains all of the value history.

`TemporalProp` has a host of helper functions covering anything that you may want to do with this history. This includes:

* `value()`/`values()`: Get the latest value or all values of the property.
* `at()`: Get the latest value of the property at the specified time.
* `history()`/`history_date_time()`: Get the timestamps of all updates to the property.
* `items()`/`items_date_time()`: Merges `values()` and `history()`/`history_date_time()` into a list of tuples.
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

