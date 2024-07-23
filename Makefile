install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	source .venv/bin/activate && python3 -m pip install dist/*.whl

.PHONY: install brain-games
