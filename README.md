# Raphtory Docs

This repo contains the Documentation for [Raphtory](https://github.com/Pometry/Raphtory) - the temporal graph engine and is based on the documentation for [Polars](https://github.com/pola-rs/polars).

## Getting Started

The User guide is made with [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/). In order to get started with building this book perform the following steps:

```shell
make requirements

```

In order to serve the books run `make serve`. This will run all the python examples and display the output inline using the `markdown-exec` plugin.

## Deployment

Deployment of the book is done using Github Pages and Github Workflows. The book is automatically deployed on each push to master / main branch. There are a number of checks in the CI pipeline to avoid non-working examples:

- Run all python examples, fail on any errors
- Check all links in markdown
- Run black formatter

## Current Todo's

### Small changes
- [ ] Add documentation on node types within the direct updates page
- [ ] Add documentation on node types within dataframes
- [ ] Add documentation on node types to Node metrics and functions
- [ ] Need to add documentation on `exclude_layers` `valid_layers` and `exclude_nodes` in Exploded edges and Layer Views
- [ ] Need to add documentation on `nbr`
- [ ] Once implemented add about date_time

### Full pages 
- [ ] Add documentation on GraphQL
- [ ] Add documentation on the PersistentGraph
- [ ] Add documentation on the Vector storage
- [ ] Add documentation on the Index Graph

### Minor tweaks 
- [ ] Add a note about updating whilst iterating causing deadlocks
- [ ] Add a note on how numbers as strings will be converted to int IDs (in Accepted ID types)




### Comments that need to be added in later

!!! info 
    Note: All functions here which return a timestamp as part of the result have a `*_date_time()` variation allowing you to get datetime objects instead of epoch integers. For instance, `items_date_time()`.