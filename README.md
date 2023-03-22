[![](docs/assets/media/banner.png)](https://lucmos.github.io/powermanim)

<p align="center">
    <a href="https://pypi.org/project/powermanim/"><img alt="PyPi" src=https://img.shields.io/pypi/v/powermanim></a>
    <a href="https://pypi.org/project/powermanim/"><img alt="PyPi" src=https://img.shields.io/pypi/dm/powermanim></a>
    <a href="https://github.com/lucmos/powermanim/actions/workflows/publish.yml"><img alt="CI" src=https://github.com/lucmos/powermanim/actions/workflows/publish.yml/badge.svg?branch=main></a>
    <a href="https://lucmos.github.io/powermanim"><img alt="Docs" src=https://img.shields.io/github/deployments/lucmos/powermanim/github-pages?label=docs></a>
    <a href="https://black.readthedocs.io/en/stable/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

Manim extension with custom components, layouts and slide templates aimed to ease the development of live presentations.


## Installation

```bash
pip install git+ssh://git@github.com/lucmos/powermanim.git
```


## Quickstart

[comment]: <> (> Fill me!)


## Development installation

Setup the development environment:

```bash
git clone git@github.com:lucmos/powermanim.git
cd powermanim
conda env create -f env.yaml
conda activate powermanim
pre-commit install
```

Run the tests:

```bash
pre-commit run --all-files
pytest -v
```


### Update the dependencies

Re-install the project in edit mode:

```bash
pip install -e .[dev]
```
