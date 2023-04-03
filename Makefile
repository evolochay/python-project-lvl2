install:
	poetry install


gendiff:
	poetry run gendiff


build:
	poetry build


package-install:
	python3 -m pip install --user dist/*.whl


package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl


make lint:
	poetry run flake8 gendiff


make test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/