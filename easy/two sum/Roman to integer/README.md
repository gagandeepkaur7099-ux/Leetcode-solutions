# Roman to Integer

## Problem

Given a Roman numeral, convert it into an integer.

## Approach

- Create a helper function to return the value of each Roman numeral character.
- Traverse the string from left to right.
- If the current Roman numeral has a smaller value than the next one, subtract its value.
- Otherwise, add its value to the answer.
- Return the final integer.

## Algorithm

1. Initialize the answer as 0.
2. Traverse the Roman numeral string.
3. Compare the current character with the next character.
4. If the current value is smaller, subtract it.
5. Otherwise, add it.
6. Return the final result.

## Time Complexity

O(n)

## Space Complexity

O(1)

## Concepts Used

- String Traversal
- Conditional Statements
- Helper Function
- Greedy Approach
