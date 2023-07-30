import json


def build_dep_tree(input_file):
    
    # Assert that input file given is of filetype JSON
    assert input_file.split('.')[-1] == "json", "Please give a JSON file as input file"
    
    # Load JSON file containing dependencies
    with open(input_file, 'r') as content:
        data = json.load(content)

    # Instantiate dict to store dependency tree
    dep_tree = {}

    # iterate over each key in the dictionary
    for package in data:

        # Use recursive function to gather all package dependencies
        # as well as dependencies of dependencies
        dep_tree[package] = find_dependencies(data, package)

    return dep_tree


def find_dependencies(data, package, path=[]):

    # Add current package to path variable
    path = path + [package]

    # Instantiate dict to store dependency tree
    dep_tree = {}

    # iterate over every value corresponding to the keys
    for dependency in data[package]:

        # Check if recursion has already been done in current path
        if dependency not in path:

            # Check if dependency matches one of the keys in the file
            if dependency in data:
                dep_tree[dependency] = find_dependencies(data, dependency, path)

            else:
                print(f"Warning: Package {dependency} is not a key in JSON file")
                dep_tree[dependency] = {}

    return dep_tree


def main():

    dep_tree = build_dep_tree('/tmp/deps.json')
    print(json.dumps(dep_tree, indent=4))


if __name__ == '__main__':
    main()