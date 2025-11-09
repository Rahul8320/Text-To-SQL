# Text To SQL

Interact with your database by naturel english text or query.

## Prerequisites

 - [Python (version 3.14 or higher)](https://www.python.org/downloads)
 - [UV](https://docs.astral.sh/uv/getting-started/installation)

## Local Development Setup

1. Clone the repo 

```bash
git clone https://github.com/Rahul8320/Text-To-SQL.git
cd Text-To-SQL
```

2. Install dependency

```bash
uv sync -U
```

3. Seed database

```bash
uv run .\Scripts\seed_db.py
```