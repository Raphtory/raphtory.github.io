# Running algorithms 

Within Raphtory we have implemented many of the standard algorithms you may expect within a graph library, but have also added several temporal algorithms such as `Temporal Reachability` and `Temporal Motifs`. You can check out the full list of available algorithms [here](https://docs.raphtory.com/en/master/reference/algorithms/index.html) and edit the code snippets below in your own notebook to test them out.

Before we look at the different types of algorithms, let's first load in some data. For these examples we are going to use the [One graph to rule them all](https://arxiv.org/abs/2210.07871) dataset, which maps the co-occurrence of characters within the Lord of The Rings books. This dataset is a simple edge list, consisting of the source character, destination character and the sentence they occurred together in (which we shall use as a timestamp). The dataframe for this can be seen in the output below.

{{code_block('getting-started/algorithms','data_loading',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="algorithms"
    --8<-- "python/getting-started/algorithms.py:data_loading"
    ```
