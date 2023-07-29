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

The `main()` function in `Exercise1.py` provides an example of how to call `find_duplicates()`. It defines an example list, calls `find_duplicates()` with this list, and prints the result.

To run the code, use the following command from the root directory of this repository:

```
python -m exercise1.Exercise1
```

## Testing the code

Implemented using unittest...