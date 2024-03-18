VENV = .venv

venv: $(VENV)/bin/activate

$(VENV)/bin/activate:
	python -m venv $(VENV) && \
	source $(VENV)/bin/activate && \
	python -m pip install -e '.[test]'
