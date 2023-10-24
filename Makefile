TEST = pytest 
TEST_ARGS = --verbose --color=yes
TYPE_CHECK = mypy --strict
STYLE_CHECK = flake8
STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive

.PHONY: all
all: style-check type-check run-test clean


.PHONY: run-test
run-test:
	python hvert.py
	

.PHONY: type-check
type-check:
	@mypy --strict hvert.py
	@mypy --strict test_hvert.py
	@mypy --strict test_unit_hvert.py


.PHONY: style-check
style-check:
	flake8 hvert.py
	flake8 test_hvert.py
	flake8 test_unit_hvert.py


.PHONY: local-kattis-test
local-kattis-test:
	@cat sample_input.in | python hvert.py | diff - sample_output.ans
	@echo "Test passed"


.PHONY: local-unit-test
local-unit-test:
	@pytest test_hvert.py
	@pytest test_unit_hvert.py


.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis


.PHONY: push
push: run-test clean
	

.PHONY: fix-style
fix-style:
	@autopep8 --in-place --aggressive --aggressive hvert.py
	@autopep8 --in-place --aggressive --aggressive test_hvert.py
	@autopep8 --in-place --aggressive --aggressive test_unit_hvert.py


.PHONY: submit-kattis
submit-kattis:
	@python ../kattis-cli/submit.py -f -p hvertskalmaeta hvert.py