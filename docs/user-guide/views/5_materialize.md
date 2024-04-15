# Materialize
All of the view functions mentioned hold zero updates of their own, simply providing a lens through which to look at the original graph you ingested into. This is by design so that we can have many of them without our machines exploding from data duplication. 

This does mean, however, if the original graph is updated, all of the views over it will also update. If you do not want this to happen you may `materialize()` a view, creating a new graph and copying all the updates the view contains into it. 

Below we can see an example of this where we create a windowed view between the 17th and 18th of June and then materialize this. After adding a new monkey interaction in the materialized graph, we can see the original graph doesn't contains this update, but our materialized graph does.

{{code_block('getting-started/querying','materialize',[])}}
!!! Output

    ```python exec="on" result="text" session="getting-started/querying"
    --8<-- "python/getting-started/querying.py:materialize"
    ```