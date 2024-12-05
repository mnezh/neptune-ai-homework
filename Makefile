ifeq ($(OS),Windows_NT)
	VENV_PREFIX=$(strip venv\bin\)
else
	VENV_PREFIX=venv/bin/
endif

TESTS?=tests

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
	$(VENV_PREFIX)python -m pytest --spec -s $(TESTS)

package: build/package.zip

build/package.zip:
	mkdir -p build
	zip -r build/package.zip * -x "*/.*" -x "build/*" -x "reports/*" -x "*__pycache__*" "venv/*"
	
clean:
	rm -rf venv reports
