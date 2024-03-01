format:
	poetry run black .
	poetry run isort .
	poetry run autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive .
	poetry run flake8 .
format-check:
	poetry run black --check .
	poetry run isort --check .
	poetry run autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive --check .
	poetry run flake8 .
test:
	poetry run pytest --cov=src tests
create-cli:
	poetry run pyinstaller src/noclockscli/__main__.py --onefile --name noclockscli
build-package:
	poetry run python setup.py sdist
release-to-pypi:
	poetry run twine upload dist/*
