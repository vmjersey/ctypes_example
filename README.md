# ctypes_example

## Project Structure

   * examples:  Directory with simple python scripts to show how the python package is used.
   * python:  Directory with the c_utils package.  
   * write_file: Example shared library for writing a simple text file.

## Install Python Package


```
	% cd python
	% pip install . 
```

## Install Shared Library

```
	% mkdir build
 	% cd build
	% cmake ..
	% make
	% make install
```



