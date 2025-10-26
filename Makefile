.PHONY: lint test ci-local
lint:
	pylint --fail-under=10.0 tools
test:
	pytest
ci-local: lint test