install:
	uv sync

gendiff:
	uv run gendiff

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build