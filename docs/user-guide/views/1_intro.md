# Introduction and dataset

All of the operations we have discussed up until this point have been executed on the whole graph, including the full history. In this section we will look at applying `Graph Views` which provide a way to look at a subset of this data without having to reingest it. 

Raphtory can maintain hundreds of thousands of `Graph Views` in parallel, allows chaining view functions together to create as specific a filter as is required for your use case, and provides a unified API such that all functions mentioned can be called on a graph, node or edge.

!!! info 
    For this chapter we shall continue using the Monkey graph described in the [Querying Introduction](../querying/1_intro.md).
