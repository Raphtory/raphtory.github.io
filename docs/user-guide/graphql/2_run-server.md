# Running the GraphQL Server

Before you run the GraphQL server, you will need to follow our tutorials on how to get your data into Raphtory. These tutorials can be found following this [link](../../ingestion/1_creating-a-graph).

## Saving your Raphtory graph into a directory

Once your graph is loaded into Raphtory, the graph needs to be saved into your working directory. This can be done with the following code snippet (change `g` to the constant that your Raphtory graph is saved under):

=== ":fontawesome-brands-python: Python"

    ```python
    import os
    working_dir = "graphs/"

    if not os.path.exists(working_dir):
        os.makedirs(working_dir)
    g.save_to_file(working_dir + "your_graph")
    ```

## Starting a server with .run()

To run the GraphQL server with `.run()`, create a python file `run_server.py` with the following code:

=== ":fontawesome-brands-python: Python"

```python
from raphtory import graphql

import argparse
parser = argparse.ArgumentParser(description="For passing the working_dir")
parser.add_argument(
    "--working_dir",
    type=str,
    help="path for the working directory of the raphtory server",
)
args = parser.parse_args()

server = graphql.GraphServer(args.working_dir)

server.run()
```

To run the server, type this command into the terminal:

```bash
python run_server.py --working_dir ../your_working_dir
```

## Starting a server with .start()

It is also possible to start the server in Python with `.start()`. This is an example of how to start the server and send a Raphtory graph to the server (rename `new_graph` to your Raphtory graph object).

=== ":fontawesome-brands-python: Python"

```python
tmp_work_dir = tempfile.mkdtemp()
with GraphServer(tmp_work_dir, tracing=True).start():
    client = RaphtoryClient("http://localhost:1736")
    client.send_graph(path="g", graph=new_graph)

    query = """{graph(path: "g") {nodes {list {name}}}}"""
    client.query(query)
```

You can set the port in `RaphtoryClient()` to the port that you desire the GraphQL server to be run on.

The path parameter is always the graph in your server that you would like to change/read. So in this example, we want to send new_graph to graph "g" on the server.

The graph parameter is set to the Raphtory graph that we would like to send. An additional `overwrite` parameter can be stated if we want this new graph to overwrite the old graph.
