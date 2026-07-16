# Palindrome Number

## Problem

Given an integer `x`, return `true` if it is a palindrome, otherwise return `false`.

## Language

C++

## Approach

- Negative numbers cannot be palindromes.
- Reverse the given number digit by digit.
- Compare the reversed number with the original number.
- If both are equal, return `true`; otherwise return `false`.

## Algorithm

1. Check if the number is negative.
2. Store the original number.
3. Reverse the digits using a loop.
4. Compare the reversed number with the original.
5. Return the result.

## Time Complexity

O(log n)

## Space Complexity

O(1)
