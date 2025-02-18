"""
Title: Count Odd Numbers in an Interval Range
URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
Difficulty: Easy
Tags: Amazon, Microsoft, Apple, Adobe
Topics: Math

Approach:
- obviously we need to do some variation of (high - low) // 2
- but we must consider all edge cases -> both odd, both even, one even one odd
- run one example of each and we will find how to handle the off by 1 case


Time Complexity: O(1)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 or high % 2)



"""
Question:

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9
"""