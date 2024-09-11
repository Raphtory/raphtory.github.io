# Views on a persistent graph

<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>

When dealing with the `Graph` object previously where edges are formed from instantaneous event streams, views were used to create a temporal bound on the graph to ultimately see how the graph changes over time. Single views were created using `at`, `before`, `after` and `window`, and iterators of windows were created using `expanding` and `rolling`. Functionality with the same name is available for the persistent graph. It shares similarities with the functionality for `Graph` but has some important differences. Through the use of example, this page aims to cover the behaviour of this time-bounding behaviour on the `PersistentGraph`.

## Querying an instant of the graph with `at()`

{{code_block('getting-started/persistent-graph','at_1',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:at_1"
    ```

As we can see, the edge's presence in the graph is _inclusive_ of the timestamp at which it was added, but _exclusive_ of the timestamp at which it was deleted. You might think of it being present on a interval \\(1 \leq t < 5 \subseteq \mathbb{Z}\\). Note that the earliest and latest times for each edge is adjusted to the time bound in the query.

Another thing to note is that while nodes are not present until they are added (see example at time 1), but once they are added they are in the graph forever (see example at time 6). This differs from the `Graph` equivalent where nodes are present only when they contain an update within the time bounds. Crucially, this means that while performing a node count on a `Graph` will count the nodes who have activity (a property update, an adjacent edge added) within the time bounds specified, the same is not true for `PersistentGraph`s. As this may not be desirable, we are currently working on an alternative in which nodes without any edge within the time window will be treated as not present.

## Getting the graph before a certain point with `before()`

{{code_block('getting-started/persistent-graph','before_1',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:before_1"
    ```

Here we see that the `before(T)` bound is exclusive of the end point \\(T\\), creating an intersection between the time interval \\(-\infty < t < T\\) and \\(2 \leq t < 5\\) where \\(T\\) is the argument of `before`.

## Getting the graph after a certain point with `after()`

{{code_block('getting-started/persistent-graph','after_1',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:after_1"
    ```

`after(T)` is also exclusive of the starting point \\(T\\).

## Windowing the graph with `window()`

{{code_block('getting-started/persistent-graph','window_1',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:window_1"
    ```

A `window(T1, T2)` creates a half-open interval \\(T_1 \leq t < T_2\\) intersecting the edge's active time ( \\(2 \leq t < 5 \\) in this case). Some examples to note are when the window is completely inside the edge active time and when the edge's active time is strictly inside the window. In both cases, the edge is treated as present in the graph. For some applications, it may be useful to consider edges whose last update inside the window is a deletion as being absent. This option is going to be explored in coming versions of Raphtory.