PYTHON  = $$([ $$(command -v python3 || true) ] && echo python3 || echo python)
all: help

clean   :
	rm -rf */*.pyc */__pycache__

.PHONY: test
test    :
	@echo "Running unittests"
	@python3 -B -m unittest discover -v


help    :
	@echo "Make <targets> = { clean, test }"
	@echo "Examples:"
	@echo "   make clean"
	@echo "   make test"
	@echo