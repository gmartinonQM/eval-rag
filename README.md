# Eval RAG

This repository allows to reproduce figures from the AMIAD submission "Vers une évaluation rigoureuse des systèmes RAG : le défi de la
due diligence".

In particular, the dataset is in the `data/` folder, and the code to reproduce figures from the paper is in the `notebooks` folder.

# Setup environment

## Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Create your virtual environment

```bash
uv sync --all-groups
```

## Install pre-commit

```bash
uv run pre-commit install
```

## Run notebooks

```bash
uv run jupyter notebook
```