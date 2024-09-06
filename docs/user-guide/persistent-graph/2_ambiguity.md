# Handling of ambiguous updates

Whereas there is a natural way to construct a _link-stream_ graph regardless of the order the updates come in, throwing deletions into the mix can lead to questions about what graph to create. Let's look at the below example. 

## Order of processing additions and deletions

{{code_block('getting-started/persistent-graph','behaviour_1',['Graph'])}}

Reading this line by line, we may see this as two edges between Alice and Bob which overlap in time: one starting at time 1 and ending at time 5, another starting at time 3 and ending at time 7. After all, the link-stream graphs in Raphtory are allowed to have edges between the same pair of nodes happening at the same instant. However, when we look at the exploded edges of this graph, the following is returned:

!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:behaviour_1"
    ```

Here, we see two edges which are contingent to each other in time: one from time 1 to time 3 and one from time 3 to time 5. The second deletion at time 7 is ignored. The reason for this is so that Raphtory's graph updates are inserted in chronological order up to events which happen at the same time, such that the same graph should be constructed regardless of the line order in which the updates are made. Here, the order is: edge addition at time 1, edge addition at time 3, edge deletion at time 5 and edge deletion at time 7. This second edge deletion is now redundant.

## Additions and deletions in the same instant

{{code_block('getting-started/persistent-graph','behaviour_2',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:behaviour_2"
    ```