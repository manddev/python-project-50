install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

unpack: install build package-install

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint

remove-package:
	uv tool uninstall hexlet-code