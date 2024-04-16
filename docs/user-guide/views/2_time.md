# Querying the graph over time
The first set of view functions we will look at are for traveling through time, viewing the graph as it was at a specific point, or between two points (applying a time window). For this Raphtory provides six functions: `before()`, `at()`, `after()`, `window()`, `expand()` and `rolling()`.

All of these functions can be called on a graph, node, or edge, returning an equivalent `Graph View`, `Node View` or `Edge View` which have all the same functions as its unfiltered counterpart. This means if you write a function which takes a Raphtory entity, it will work irrelevant of which filters have been applied.

## Before, At and After 

Beginning with the simplest of these filters, `before()`, `at()` and `after()` take a singular `time` argument in epoch (integer) or datetime (string/datetime object) format and return a `View` of the object which includes:

* `before()` - All updates between the beginning of the graph's history and the provided time (**exclusive of the time provided**).
* `after()` - All updates between the provided time and the end of the graph's history (**exclusive of the time provided**)
* `at()`- Only updates which happened at exactly the time provided.

!!! note
    While the first two are more useful on continuous time datasets, `at()` can be very handy when you have snapshots or logical timestamps and want to look at them individually or compare/contrast.

As an example of these, in the code below where we print the degree of `Lome` on the full dataset, before 12:17 on the 13th of June and after 9:07 on the 30th of June.

We also introduce two new time functions here, `start()` and `end()`, which specify the time range a view is filtered to, if one has been applied. 

{{code_block('getting-started/querying','at',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:at"
    ```

!!! note
    You may have noticed in the code we have called the `before()` on the graph and `after()` on the node. This is important, as there are some subtle differences in where these functions are called, which we shall discuss [below](2_time.md#traversing-the-graph-with-views).


## Window
The `window()` function is a more general version of the functions above, allowing you to set both a `start` time as well as an `end` time (**inclusive of start, exclusive of end**). 

This is useful for digging into specific ranges of the history that you are interested in, for example a given day within your data, filtering everything else outside this range. An example of this can be seen below where we look at the number of times `Lome` interacts wth `Nekke` within the full dataset and for one day between the 13th of June and the 14th of June.

!!! info
    We use datetime objects in this example, but it would work exactly the same with string dates and epoch integers.

{{code_block('getting-started/querying','window',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:window"
    ```

## Traversing the graph with views
As mentioned above, there are some slight differences when applying views, depending on which object you call them on. This has to do with how the filters propagate as you traverse the graph.
 
As a general rule, when you call any function on a `Graph View`, `Node View` or `Edge View` which returns another entity, the view's filters will be passed onto the entities it returns. For example, if you call `before()` on a graph and then call `node()`, this will return a `Node View` filtered to the time passed to the graph.

However, if this was always the case, it would make it very annoying if we later wanted to explore outside of these bounds, especially as we traverse across the graph. 

To allow for both global bounds and moving bounds, if a filter is applied onto the graph, all entities extracted always have this filter applied. However, if it is applied to either a node or an edge, once you have traversed to a new node (neighbour) this filter is removed. 

As an example of this, below we look at LOME's one hop neighbours before the 20th of June and their neighbours (LOME's two hop neighbours) after the 25th of June. First we try calling `before()` on the graph, which works for the one hop neighbours, but once the `after()` has been applied, the graph is empty as their is no overlap in dates between the two filters. 

Next, we instead call `before()` on the node, which once the neighbours have been reached allows the `after()` to work as desired as the original filter has been removed.

{{code_block('getting-started/querying','hopping',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:hopping"
    ```

## Expanding
If you have data covering a large period of time, or have many time points of interest, it is quite likely you will find yourself calling the above functions over and over. If there is a pattern to these calls, say you are interested in how your graph looks every morning for the last week, you can instead utilise `expanding()`. 

`expanding()` will return an iterable of views as if you called `before()` from the earliest time to the latest time at increments of a given `step`. 

The step can be given as a simple epoch integer, or a natural language string describing the interval. For the latter, this is converted into a iterator of datetimes, handling all corner cases like varying month length and leap years.

Within the string you can reference `years`, `months` `weeks`, `days`, `hours`, `minutes`, `seconds` and `milliseconds`. These can be singular or plural and the string can include 'and', spaces, and commas to improve readability. 

In the code below, we can see some examples of this where we first increment through the full history of the graph a week at a time. This creates four views, each of which we ask how many monkey interactions it has seen. You will notice the start time doesn't not change, but the end time increments by 7 days each view.

The second example shows the complexity of increments Raphtory can handle, stepping by `2 days, 3 hours, 12 minutes and 6 seconds` each time. We have additionally bounded this expand via a window between the 13th and 23rd of June to demonstrate how these views may be chained.

{{code_block('getting-started/querying','expanding',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:expanding"
    ```

## Rolling 
If instead of including all prior history, you want a rolling window, you may use `rolling()`. This function will return an iterable of views, incrementing by a `window` size and only including the history from inside the window period (**Inclusive of start, exclusive of end**). This allows you to easily extract daily or monthly metrics.

 For example, below we take the code from [expanding](#expanding) and swap out the function for `rolling()`. In the first loop we can see both the start date and end date increase by seven days each time, and the number of monkey interactions sometimes decreases as older data is dropped from the window.

{{code_block('getting-started/querying','rolling_intro',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:rolling_intro"
    ```

Alongside the window size, `rolling()` takes an option `step` argument which specifies how far along the timeline it should increment before applying the next window. By default this is the same as `window`, allowing all updates to be analysed exactly once in non-overlapping windows. 

If, however, you would like to have overlapping or fully disconnected windows, you can set a `step` smaller or greater than the given `window` size. 

As a small example of how useful this can be, in the following segment we plot the daily unique interactions of `Lome` via `matplotlib` in only 10 lines! 

!!! info
    We have to recreate the graph in the first section of this code block so that the output can be rendered as part of the documentation. Please ignore this. 


{{code_block('getting-started/querying','rolling',[])}}