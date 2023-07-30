# Exercise 2: Dependency Tree

This directory contains the solution for the second exercise, which is about reading a JSON file containing a list of packages and their dependencies, and constructing a full dependency graph.

## Overview

The main function, `build_dep_tree(input_file)`, takes a filename as input and returns a dictionary representing the fully resolved dependency graph. 

The function works by loading the JSON file containing dependencies and iterating over each package in the file. It uses a recursive function, `find_dependencies(data, package, path=[])`, to gather all package dependencies as well as dependencies of dependencies, and stores them in a dictionary.

For example, given a JSON file with the following content:
```json
{
  "pkg1": ["pkg2", "pkg3"],
  "pkg2": ["pkg3"],
  "pkg3": []
}
```
The function returns the following dictionary:
```json
{
    "pkg1": {
        "pkg2": {
            "pkg3": {}
        },
        "pkg3": {}
    },
    "pkg2": {
        "pkg3": {}
    },
    "pkg3": {}
}
```

## Running the code

The `main()` function in `exercise2.py` provides an example of how to call `build_dep_tree()`. It defines a filename `(/tmp/deps.json)`, calls `build_dep_tree()` with this filename, and prints the result.

To run the code, use the following command from the root directory of this repository:
```bash
python -m exercise2.exercise2
```

## Testing the code

The file `test_exercise2.py` contains a series of tests for the `build_dep_tree()` function, implemented using the PyTest testing framework. The tests cover a variety of scenarios, including circular dependencies, self-dependencies, unknown packages, and more.

To run the tests, use the following command from the root directory of this repository:
```bash
pytest exercise2/test_exercise2.py
```

This will automatically run all the test cases defined in `test_exercise2.py` and output a report on the results.