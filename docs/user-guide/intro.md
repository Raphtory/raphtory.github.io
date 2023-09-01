# Introduction

This getting started guide is written for new users of Raphtory. The goal is to provide a overview of the most common functionality. For more in-depth examples you can checkout our [example repository](https://github.com/Pometry/Raphtory/tree/master/examples) or go directly to the [library APIs](docs.raphtory.com).

The guide is split into the follow sections, which are written under the assumption of being read in order, but feel free to jump to anywhere that takes your interest first.

| Section                              | Summary                                                                                           |
|--------------------------------------|---------------------------------------------------------------------------------------------------|
| [Installation](installation.md)      | How to install Raphtory as either a Rust or Python library.                                       |
| [Ingestion](ingestion.md)            | Loading data into Raphtory via direct function calls and automatic dataframe parsers.             |
| [Querying](querying.md)              | How to start querying and exploring your graphs and apply different *graph views*.                |
| [Algorithms](algorithms.md)          | How to run the in-build graph algorithm suite on your data and handle the returned results.       |
| [Visualisation](visualisation.md)    | How to visualise/display your data in graph form.                                                 |
| [GraphQL](graphql.md)                | Hosting and querying your graphs via the in-build graphql service.                                |
| [Deletions](graph-deletions.md)      | How to build graphs where the edges have duration or explicit deletions.                          |


!!! rust
    The rust examples within this guide are currently under development - whilst the general principles discussed are the same between python and rust, you can find code snippets in our [docs.rs](https://docs.rs/raphtory/latest/raphtory/) page.