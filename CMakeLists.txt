cmake_minimum_required(VERSION 3.9)

project(cmake_example)

add_subdirectory(write_file)


# This doesn't seem to be the best way to install a Python package within CMake, but couldn't find good doc

find_package(Python ${PYTHON_VERSION} REQUIRED COMPONENTS Development)

install(DIRECTORY python/c_utils DESTINATION $CMAKE_INSTALL_PREFIX}/lib/python${Python_VERSION_MAJOR}.${Python_VERSION_MINOR}/site-packages)

