import pytest
import json
import os
from .exercise2 import build_dep_tree


# Function to create the JSON test files
def create_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


# Function to delete the test files after completion of the test
def delete_json_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


 
def test_basic_example():
    test_file = '/tmp/deps.json'
    result = build_dep_tree(test_file)
    assert result == {"pkg1": {"pkg2": {"pkg3": {}},
                               "pkg3": {}},
                      "pkg2": {"pkg3": {}},
                      "pkg3": {}
                      }



def test_circular_deps():

    # Define test file name in tmp folder
    test_file = '/tmp/test_circular_deps.json'

    # Define test file content
    test_data = {"pkg1": ["pkg2"], "pkg2": ["pkg1"]}

    # Create JSON file 
    create_json_file(test_data, test_file)

    # Store object returned by build_dep_tree()
    result = build_dep_tree(test_file)

    # Assert that produced and expected result are the same
    assert result == {"pkg1": {"pkg2": {}}, "pkg2": {"pkg1": {}}}

    # Delete test file created in tmp dir
    delete_json_file(test_file)



def test_deps_empty():
    test_file = '/tmp/test_deps_empty.json'
    test_data = {}
    create_json_file(test_data, test_file)
    result = build_dep_tree(test_file)
    assert result == {}
    delete_json_file(test_file)


def test_self_depend():
    test_file = '/tmp/test_self_depend.json'
    test_data = {"pkg1": ["pkg2"], "pkg2": ["pkg2"]}
    create_json_file(test_data, test_file)
    result = build_dep_tree(test_file)
    assert result == {"pkg1": {"pkg2": {}}, "pkg2": {}}
    delete_json_file(test_file)


def test_unknown_package():
    test_file = '/tmp/test_duplicate_packages.json'
    test_data = {"pkg1": ["pkg2"], "pkg2": ["pkg3"]}
    create_json_file(test_data, test_file)
    result = build_dep_tree(test_file)
    assert result == {"pkg1": {"pkg2": {"pkg3": {}}}, "pkg2": {"pkg3": {}}}
    delete_json_file(test_file)


def test_one_package_no_deps():
    test_file = '/tmp/test_one_package_no_deps.json'
    test_data = {"pkg1": []}
    create_json_file(test_data, test_file)
    result = build_dep_tree(test_file)
    assert result == {"pkg1": {}}
    delete_json_file(test_file)


def test_bigger_file():
    test_file = '/tmp/test_bigger_file.json'
    test_data = {
                "pkg1": ["pkg2", "pkg3"],
                "pkg2": ["pkg3", "pkg4"],
                "pkg3": [],
                "pkg4": ["pkg1", "pkg5"],
                "pkg5": ["pkg3", "pkg2", "pkg1"]
            }
    create_json_file(test_data, test_file)
    result = build_dep_tree(test_file)
    assert result == {
                    "pkg1": {
                        "pkg2": {
                            "pkg3": {},
                            "pkg4": {
                                "pkg5": {
                                    "pkg3": {}
                                }
                            }
                        },
                        "pkg3": {}
                    },
                    "pkg2": {
                        "pkg3": {},
                        "pkg4": {
                            "pkg1": {
                                "pkg3": {}
                            },
                            "pkg5": {
                                "pkg3": {},
                                "pkg1": {
                                    "pkg3": {}
                                }
                            }
                        }
                    },
                    "pkg3": {},
                    "pkg4": {
                        "pkg1": {
                            "pkg2": {
                                "pkg3": {}
                            },
                            "pkg3": {}
                        },
                        "pkg5": {
                            "pkg3": {},
                            "pkg2": {
                                "pkg3": {}
                            },
                            "pkg1": {
                                "pkg2": {
                                    "pkg3": {}
                                },
                                "pkg3": {}
                            }
                        }
                    },
                    "pkg5": {
                        "pkg3": {},
                        "pkg2": {
                            "pkg3": {},
                            "pkg4": {
                                "pkg1": {
                                    "pkg3": {}
                                }
                            }
                        },
                        "pkg1": {
                            "pkg2": {
                                "pkg3": {},
                                "pkg4": {}
                            },
                            "pkg3": {}
                        }
                    }
                }
    delete_json_file(test_file)


