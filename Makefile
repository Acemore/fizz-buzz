build:
	poetry build

fizz-buzz:
	poetry run fizz-buzz

install:
	poetry install

lint:
	poetry run flake8 fizz_buzz

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=fizz_buzz --cov-report xml

.PHONY: build install lint package-install publish test
