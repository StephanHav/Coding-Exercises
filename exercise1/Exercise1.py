def find_duplicates(input_list):

    # Instantiate set to track unique values
    uniques = set()

    # Instantiate list to keep track of the order of unique elements
    uniques_ordered = []

    # Iterate over every element in the input list
    for element in input_list:

        # Check if the element is already in the set
        if element not in uniques:
            
            # Add to list containing ordered unique values
            uniques_ordered.append(element)

            # Add to set of uniques 
            uniques.add(element)

    # List comprehension to generate ordered list of duplicates by 
    # checking occurrences of unique values in input list
    duplicates = [element for element in uniques_ordered if input_list.count(element) > 1]

    return duplicates


def main():

    #input_list = ['w', 'b'] + ["a", "c", "c", "a", "c", "d", "c", "d", 1] * 10000000 + ['z', 'e', 2]
    input_list = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
    print(find_duplicates(input_list))

    

if __name__ == '__main__':
    main()
    

