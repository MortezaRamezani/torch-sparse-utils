all:
	python setup.py build_ext --inplace

clean:
	rm -rf build/ *.so *.cpp *.egg-info dist/
	rm -rf */*/*.cpp */*/*.c */*/*.so */*/*.html