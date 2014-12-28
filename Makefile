# I don't know how "py.test" can run on different python versions
# So this just has the python script call pytest within the python file
test:
	python tests/test_simple.py
