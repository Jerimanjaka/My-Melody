# Makefile pour le projet voici-ai

.PHONY: all clean install

# Variables
PYTHON=python3
VENV=.venv

all: install

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)

install: $(VENV)/bin/activate requirements.txt
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV)