default:
	poetry install
	poetry run argb_generator
	
.PHONY: install_poetry
install_poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
