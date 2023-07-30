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

The file `test_exercise2.py` contains a series of tests for the `build_dep_tree()` function, implemented using the PyTest testing framework. The tests cover a variety of scenarios, including circular dependencies, self-dependencies, unknown packages, and more. In order to run these tests it creates test files in the `/tmp` folder, which are deleted upon completion of the test case. tmp is a good directory to do this as files will not persist after a restart in case files are failed to be deleted by the script through an error.  

To run the tests, use the following command from the root directory of this repository:
```bash
pytest exercise2/test_exercise2.py
```

This will automatically run all the test cases defined in `test_exercise2.py` and output a report on the results. Some additional explanation on each of the test cases is given below:

1. `test_basic_example()`: This test validates the functionality of the build_dep_tree() function with the example given in the problem statement. It's important to verify that the function behaves as expected with this basic example.

2. `test_circular_dependency`: This test checks if the function handles circular dependencies correctly. This is an edge case where pkg1 depends on pkg2 and pkg2 depends on pkg1, risking that the function gets stuck in an infinite recursion loop. The function should still be able to construct the correct dependency tree.

3. `test_deps_empty()`: This test checks how the function behaves when given an empty dictionary. This is an edge case where there are no packages or dependencies. The function should return an empty dictionary.

4. `test_self_depend()`: This test checks how the function handles a package that depends on itself. This is an edge case where pkg2 depends on pkg2. The function should not get stuck in a loop and should be able to construct the correct dependency tree.

5. `test_unknown_package()`: This test checks how the function handles a package that depends on an unknown package (a dependency of a package that is not a key itself in the JSON file). The function should still be able to construct the correct dependency tree and issue a warning about the unknown package.

6. `test_one_package_no_deps()`: This test checks how the function handles a package with no dependencies. This case ensures that the function can handle such scenarios and correctly identifies that the package has no dependencies.

7. `test_bigger_file()`: This test checks the function's performance and accuracy with a larger and more complex set of packages and dependencies. It's crucial to test this to ensure your function can handle larger and more complex data and still produce correct results.

Each of these test cases addresses a different aspect of the function's behavior, ensuring it works correctly under a variety of scenarios.