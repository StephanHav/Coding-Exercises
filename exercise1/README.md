# Exercise 1: Duplicate Detection

This directory contains the solution for the first exercise, which is about detecting duplicate elements in a list.

## Overview

The main function, `find_duplicates(input_list)`, takes a list of objects as input and returns a list of duplicated elements in the order they appeared for the first time in the original list. 

For example, for the input `["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]`, the function returns `["a", "c", "d"]`.

The function works by keeping track of the unique elements it encounters in two data structures: 

- A set (`uniques`) for quick look-up of whether an element has been seen before.
- A list (`uniques_ordered`) to remember the order in which the unique elements were seen.

There is a reason why both a set and a list are used to tackle this problem. Sets are great for quick membership checks, but they don't keep track of order. So, the list is used to remember the order in which the item was first seen. This combination gives us both speed and the right order of duplicates

At the end, it uses a list comprehension to generate the list of duplicates by checking the occurrences of each unique element in the input list.

## Running the Code

The `main()` function in `Exercise1.py` provides an example of how to call `find_duplicates()`. It defines an input list (the one given in the instructions), calls `find_duplicates()` with this list, and prints the result.

To run the code, use the following command from the root directory of this repository:

```bash
python -m exercise1.exercise1
```

## Testing the Code

The file `test.py` contains a series of tests for the `find_duplicates()` function, implemented using the `unittest` module from Python's standard library. The tests cover a variety of scenarios.

To run the tests, use the following command from the root directory of this repository:

```bash
python -m unittest exercise1.test
```

This will automatically run all the test cases defined in test.py and output a report on the results. Some additional explanation on each of the test cases is given below:

1. `test_given_example(self)`: This test checks the functionality of the function with the example given in the instructions. It's important to verify that your function behaves as expected with the given example.

2. `test_no_duplicates(self)`: This test checks if the function handles a list without duplicates correctly. It should return an empty list, because there are no duplicates. This test case checks whether the function gives false positives.

3. `test_all_duplicates(self)`: This test checks the function's behavior when all elements in the list are duplicates. It's important to check this scenario to ensure the function correctly identifies all elements as duplicates and doesn't miss any.

4. `test_mixed_elements(self)`: This test checks how the function behaves with a list containing elements of various data types. Python's flexibility allows for lists to contain elements of different types, so this case ensures the function can handle such lists.

5. `test_single_element(self)`: This test checks how the function behaves with a list containing a single element. This is a kind of edge case, where the function should return an empty list because there are no duplicates.

6. `test_empty_list(self)`: This test checks how the function behaves with an empty list. This is another edge case where the function should return an empty list, as there are no elements in the list to begin with.

7. `test_big_list(self)`: This test checks the function's performance and accuracy with a large list. It's crucial to test this to ensure your function can handle large lists and still produce correct results.

Each of these test cases addresses a different aspect of the function's behavior, ensuring it works correctly under a variety of scenarios.
