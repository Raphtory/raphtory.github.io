
# Chaining functions

When we called `v.neighbours()` in [Vertex metrics](../querying/vertex-metrics.md#neighbours-edges-and-paths), a `PathFromVertex` was returned rather than a `List`. This, along with all other iterables previously mentioned (`Vertices`,`Edges`,`Properties`), are [lazy](https://en.wikipedia.org/wiki/Lazy_evaluation) data structures which allow you to chain multiple functions together before a final execution. 

For example, for a vertex `v`, `v.neighbours().neighbours()` will return the two-hop neighbours. The first call of `neighbours()` returns the immediate neighbours of `v`, the second applies the`neighbours()` function to each of the vertices returned by the first call. 

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

## Chains with properties
To demonstrate some more complex questions that you could ask our monkey graph, we can include some property aggregation into our chains. 

In the code below we sum the `Weight` value of each of `Felipe's` out-neighbours to rank them by the number of positive interactions he has initiated with them. Following this find the most annoying monkey by ranking globally who on average has had the most negative interactions initiated against them.


{{code_block('getting-started/querying','friendship',['Edges'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:friendship"
    ```