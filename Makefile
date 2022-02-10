install:
	poetry install


gendiff:
	poetry run gendiff


build:
	poetry build


package-install:
	python3 -m pip install --user dist/*.whl