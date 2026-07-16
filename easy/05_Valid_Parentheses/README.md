# Valid Parentheses

## Problem
Given a string containing only the characters '(', ')', '{', '}', '[' and ']', determine whether the input string is valid.

A string is valid if:
- Every opening bracket has a matching closing bracket.
- Brackets close in the correct order.

## Example

Input:
"()[]{}"

Output:
true

## Approach
- Use a stack.
- Push every opening bracket into the stack.
- When a closing bracket appears, compare it with the top of the stack.
- If they do not match, return false.
- At the end, if the stack is empty, return true.

## Time Complexity
O(n)

## Space Complexity
O(n)

## Data Structure Used
Stack

## Language
C++

## Platform
LeetCode

## Status
✅ Accepted
