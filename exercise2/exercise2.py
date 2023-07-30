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

    path = path + [package]  # Add the current package to the path
    graph = {}
    for dependency in data[package]:
        if dependency not in path:  # Only recurse if we haven't visited this package in the current path
            graph[dependency] = find_dependencies(data, dependency, path)
    return graph


def main():

    dep_tree = build_dep_tree('/tmp/deps.json')
    print(json.dumps(dep_tree, indent=4))


if __name__ == '__main__':
    main()