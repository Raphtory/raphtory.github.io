# Handling of ambiguous updates

Whereas there is a natural way to construct a _link-stream_ graph regardless of the order the updates come in, throwing deletions into the mix can lead to questions about what graph to create. Let's look at the below example. 

## Order of resolving additions and deletions

{{code_block('getting-started/persistent-graph','behaviour_1',['Graph'])}}

Reading this line by line, we may see this as two edges between Alice and Bob which overlap in time: one starting at time 1 and ending at time 5, another starting at time 3 and ending at time 7. After all, the link-stream graphs in Raphtory are allowed to have edges between the same pair of nodes happening at the same instant. However, when we look at the exploded edges of this graph, the following is returned:

!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:behaviour_1"
    ```

Here, we see two edges which are contingent to each other in time: one from time 1 to time 3 and one from time 3 to time 5. The second deletion at time 7 is ignored. The reason for this is that Raphtory's graph updates are inserted in chronological order, such that the same graph should be constructed regardless of the line order in which the updates are made (apart from events which have the same timestamp, which will be covered shortly). Here, the order is: edge addition at time 1, edge addition at time 3, edge deletion at time 5 and edge deletion at time 7. This second edge deletion is now redundant.

## Hanging deletions

We saw on the previous page that adding edges without a deletion afterwards results in an edge which lasts forever. What about a deletion without a prior addition?

{{code_block('getting-started/persistent-graph','hanging_deletions',['Graph'])}}

This results in the following:
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:hanging_deletions"
    ```
which assumes that an edge was once present for it to be deleted. This can be useful if we have a dataset of changes to a graph but we're missing some starting period of the system which would have once included some original edge additions.

## Additions and deletions in the same instant

We have seen that if the update times to an edge are all distinct from each other, the graph that is constructed is fully unambiguous. What about when events have the same timestamp? 

{{code_block('getting-started/persistent-graph','behaviour_2',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:behaviour_2"
    ```

In this example, it is impossible to infer what the intended update order is (particularly since we allow hanging deletions/additions). In this case, we tie-break the updates by the order in which they are executed. This means that the first graph has an edge which instantaneously appears and disappears at time 1, and in the second an edge which instantaneously disappears at time 1 but is present for all time before and all after. It is important to bear this in mind in your analysis if you are aware of some cases like this.

## Interaction with layers

Remember the example earlier with how deletions and additions are resolved?

{{code_block('getting-started/persistent-graph','behaviour_1',['Graph'])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:behaviour_1"
    ```

Now take a look at this slightly modified example.

{{code_block('getting-started/persistent-graph','behaviour_3',['Graph'])}}

The only difference is that we've added layer names to the different edge instances. Now let's look at how the output differs.

!!! Output

    ```python exec="on" result="text" session="getting-started/persistent-graph"
    --8<-- "python/getting-started/persistent-graph.py:behaviour_3"
    ```

Here we have two edges, one starting and ending at 1 and 5 respectively with the 'colleague' layer, the other starting and ending at 3 and 7 on the 'friends' layer. Layering allows different types of interaction to exist, and edges on different layers can have overlapping times in a way that doesn't make sense for edges in the same layer or for edges with no layer. 