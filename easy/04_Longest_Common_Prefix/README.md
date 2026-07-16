# Longest Common Prefix

## Problem
Given an array of strings, return the longest common prefix among all the strings.

If there is no common prefix, return an empty string `""`.

## Example

Input:
["flower","flow","flight"]

Output:
"fl"

## Approach
- Take the first string as the initial prefix.
- Compare it with every other string.
- If the current string does not start with the prefix, remove the last character from the prefix.
- Repeat until all strings share the same prefix.

## Time Complexity
O(n × m)

- n = Number of strings
- m = Length of the shortest string

## Space Complexity
O(1)

## Language
C++

## Platform
LeetCode

## Status
✅ Accepted
