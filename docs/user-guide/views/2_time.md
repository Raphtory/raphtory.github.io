# Querying the graph over time
The first set of view functions we will look at are for traveling through time, viewing the graph as it was at a specific point, or between two points (applying a time window). For this Raphtory provides four functions: `at()`, `window()`, `expand()` and `rolling()`.

## At

The `at()` function takes a `time` argument in epoch (integer) or datetime (string/datetime object) format and can be called on a graph, vertex, or edge. This will return an equivalent `Graph View`, `Vertex View` or `Edge View` which includes all updates between the beginning of the graphs history and the provided time (**inclusive of the time provided**). 

This returned object has all of the same functions as its unfiltered counterpart and will pass the view criteria onto any entities it returns. For example if you call `at()` on a graph and then call `vertex()`, this will return a `Vertex View` filtered to the time passed to the graph.

An example of this can be seen in the code below where we print the degree of `Lome` on the full dataset, at 9:07 on the 14th of June and at 12:17 on the 13th of June.

!!! info 

    You will below that `graph.at().vertex()` and `graph.vertex().at()` are synonymous.

We also introduce two new time functions here, `start()` and `end()`, which specify the time range a view is filtered to, if one has been applied. You can see in the last line of the example we print the `start`, `earliest_time`, `latest_time` and `end` of the vertex to show you how these differ.

{{code_block('getting-started/querying','at',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:at"
    ```


## Window
The `window()` function works the same as the `at()` function, but allows you to set a `start` time as well as an `end` time (**inclusive of start, exclusive of end**). 

This is useful for digging into specific ranges of the history that you are interested in, for example a given day within your data, filtering everything else outside this range. An example of this can be seen below where we look at the number of times `Lome` interacts wth `Nekke` within the full dataset and for one day between the 13th of June and the 14th of June.

!!! info
    We use datetime objects in this example, but it would work exactly the same with string dates and epoch integers.

{{code_block('getting-started/querying','window',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:window"
    ```


## Expanding
If you have data covering a large period of time, or have many time points of interest, it is quite likely you will find yourself calling `at()` over and over. If there is a pattern to these calls, say you are interested in how your graph looks every morning for the last week, you can instead utilise `expanding()`. 

`expanding()` will return an iterable of views as if you called `at()` from the earliest time to the latest time at increments of a given `step`. 

The step can be given as a simple epoch integer, or a natural language string describing the interval. For the latter, this is converted it into a iterator of datetimes, handling all corner cases like varying month length and leap years.

Within the string you can reference `years`, `months` `weeks`, `days`, `hours`, `minutes`, `seconds` and `milliseconds`. These can be singular or plural and the string can include 'and', spaces, and commas to improve readability. 

In the code below, we can see some examples of this where we first increment through the full history of the graph a week at a time. This creates four views, each of which we ask how many monkey interactions it has seen. You will notice the start time doesn't not change, but the end time increments by 7 days each view.

The second example shows the complexity of increments Raphtory can handle, stepping by `2 days, 3 hours, 12 minutes and 6 seconds` each time. We have additionally bounded this expand via a window between the 13th and 23rd of June to demonstrate how these views may be chained.

{{code_block('getting-started/querying','expanding',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:expanding"
    ```

## Rolling 
Where `at()` has `expanding()`, `window()` has `rolling()`. This function will return an iterable of views, incrementing by a `window` size and only including the history from inside the window period (**Inclusive of start, exclusive of end**). This allows you to easily extract daily or monthly metrics.

 For example, below we take the code from [expanding](#expanding) and swap out the function for `rolling()`. In the first loop we can see both the start date and end date increase by seven days each time, and the number of monkey interactions sometimes decreases as older data is dropped from the window.

{{code_block('getting-started/querying','rolling_intro',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:rolling_intro"
    ```

Alongside the window size, `rolling()` takes an option `step` argument which specifies how far along the timeline it should increment before applying the next window. By default this is the same as `window`, allowing all updates to be analysed exactly once in non-overlapping windows. 

If, however, you would like to have overlapping or fully disconnected windows, you can set a `step` smaller or greater than the given `window` size. For example, in the code below we add a `step` of two days. You can see in the output the start and end dates incrementing by two days each view, but are always seven days apart.  


{{code_block('getting-started/querying','rolling_intro_2',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:rolling_intro_2"
    ```

As a small example of how useful this can be, in the following segment we plot the daily unique interactions of `Lome` via `matplotlib` in only 10 lines! 

!!! info
    We have to recreate the graph in the first section of this code block so that the output can be rendered as part of the documentation. Please ignore this. 


{{code_block('getting-started/querying','rolling',[])}}