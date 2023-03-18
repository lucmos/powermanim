# PowerManim

<p align="center">
    <a href="https://github.com/lucmos/powermanim/actions/workflows/test_suite.yml"><img alt="CI" src=https://img.shields.io/github/workflow/status/lucmos/powermanim/Test%20Suite/main?label=main%20checks></a>
    <a href="https://lucmos.github.io/powermanim"><img alt="Docs" src=https://img.shields.io/github/deployments/lucmos/powermanim/github-pages?label=docs></a>
    <a href="https://github.com/grok-ai/nn-template"><img alt="NN Template" src="https://shields.io/badge/nn--template-0.2.3-emerald?style=flat&labelColor=gray"></a>
    <a href="https://www.python.org/downloads/"><img alt="Python" src="https://img.shields.io/badge/python-3.9-blue.svg"></a>
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
