---
hide:
  - navigation
---

# Raphtory

<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/6665739/130641943-fa7fcdb8-a0e7-4aa4-863f-3df61b5de775.png" alt="Raphtory" width="50%"/>
</p>
<p align="center">
</p>

<p align="center">
<a href="https://github.com/Raphtory/Raphtory/actions/workflows/test.yml/badge.svg">
<img alt="Test and Build" src="https://github.com/Raphtory/Raphtory/actions/workflows/test.yml/badge.svg" />
</a>
<a href="https://github.com/Raphtory/Raphtory/releases">
<img alt="Latest Release" src="https://img.shields.io/github/v/release/Raphtory/Raphtory?color=brightgreen&include_prereleases" />
</a>
<a href="https://github.com/Raphtory/Raphtory/issues">
<img alt="Issues" src="https://img.shields.io/github/issues/Raphtory/Raphtory?color=brightgreen" />
</a>
<a href="https://crates.io/crates/raphtory">
<img alt="Crates.io" src="https://img.shields.io/crates/v/raphtory">
</a>
<a href="https://pypi.org/project/raphtory/">
<img alt="PyPI" src="https://img.shields.io/pypi/v/raphtory">
</a>
</p>
<p align="center">
<a href="https://www.raphtory.com">🌍 Website </a>
&nbsp
<a href="https://docs.raphtory.com/">📒 Documentation</a>
&nbsp 
<a href="https://www.pometry.com"><img src="https://user-images.githubusercontent.com/6665739/202438989-2859f8b8-30fb-4402-820a-563049e1fdb3.png" width="20pt" align="center"/> Pometry</a> 
&nbsp
<a href="https://docs.raphtory.com/en/master/Introduction/ingestion.html">🧙🏻‍ Tutorial</a> 
&nbsp
<a href="https://github.com/Raphtory/Raphtory/issues">🐛 Report a Bug</a> 
&nbsp
<a href="https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA"><img src="https://user-images.githubusercontent.com/6665739/154071628-a55fb5f9-6994-4dcf-be03-401afc7d9ee0.png" width="20" align="center"/> Join Slack</a> 
</p>

<br>

Raphtory is an in-memory graph tool written in Rust with friendly Python APIs on top. It is blazingly fast, scales to hundreds of millions of edges 
on your laptop, and can be dropped into your existing pipelines with a simple `pip install raphtory`.  

It supports time traveling, multilayer modelling, and advanced analytics beyond simple querying like community evolution, dynamic scoring, and mining temporal motifs.

If you wish to contribute, check out the open [list of issues](https://github.com/Pometry/Raphtory/issues), [bounty board](https://github.com/Raphtory/Raphtory/discussions/categories/bounty-board) or hit us up directly on [slack](https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA). Successful contributions will be reward with swizzling swag!


## About this guide

The `Raphtory` user guide is intended to live alongside the API documentation. Its purpose is to help new users get going with `Raphtory` and to provide meaningful examples. If you are looking for details on a specific object or functions, it is probably best to go the API documentation: [Python](https://docs.raphtory.com/en/v0.5.2/) | [Rust](https://docs.rs/raphtory/0.5.2/raphtory/).


## Example

{{code_block('home/example','example',['Graph'])}}

### Output
```python exec="on" result="python" session="home/example"
--8<-- "python/home/example.py:example"
```

## Sponsors

[<img src="https://github.com/Pometry/Raphtory/assets/6665739/3953c945-e8b4-4b4b-a01a-dd595ffb06e9" style="height:75px"/>](https://www.pometry.com/)


## Community  

Join the growing community of open-source enthusiasts using Raphtory to power their graph analysis projects!

- Follow [![Slack](https://img.shields.io/twitter/follow/raphtory?label=@raphtory)](https://twitter.com/raphtory) for the latest Raphtory news and development

- Join our [![Slack](https://img.shields.io/badge/community-Slack-red)](https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA) to chat with us and get answers to your questions!

--8<-- "docs/people.md"

## Contribute 

Want to get involved? Please checkout our [Contributing Guide](https://github.com/Pometry/Raphtory/blob/master/CONTRIBUTING.md) and raise a PR or join the Raphtory [Slack](https://join.slack.com/t/raphtory/shared_invite/zt-xbebws9j-VgPIFRleJFJBwmpf81tvxA) and speak with us on how you could pitch in!

## License

Raphtory is licensed under the terms of the GNU General Public License v3.0.
