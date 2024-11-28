ifeq ($(OS),Windows_NT)
	VENV_PREFIX=$(strip venv\bin\)
else
	VENV_PREFIX=venv/bin/
endif

setup: venv requirements.txt
	pip install -r requirements.txt

venv:
	python -m venv venv
	$(VENV_PREFIX)pip install --upgrade pip

style:
	$(VENV_PREFIX)ruff check .

format:
	$(VENV_PREFIX)ruff format .

test:
	$(VENV_PREFIX)python -m pytest --spec tests

clean:
	rm -rf venv
