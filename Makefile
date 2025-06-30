install:
	uv sync

gendiff:
	uv run gendiff

lint:
	uv run ruff check

test:
	uv run pytest

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build