setup: venv requirements.txt
	pip install -r requirements.txt

venv:
	python -m venv venv
	venv/bin/pip install --upgrade pip

style:
	venv/bin/ruff check .

format:
	venv/bin/ruff format .

test:
	venv/bin/python -m pytest --spec tests

clean:
	rm -rf venv
