# Two Sum

## Problem

Given an array of integers and a target, return the indices of the two numbers whose sum equals the target.

## Language

C++

## Approach

- Used two nested loops.
- Compared every pair of elements.
- Returned the indices when the target sum was found.

## Algorithm

1. Traverse the array using the first loop.
2. Compare each element with the remaining elements.
3. If the sum equals the target, return their indices.
4. If no pair is found, return an empty vector.

## Time Complexity

O(n²)

## Space Complexity

O(1)
