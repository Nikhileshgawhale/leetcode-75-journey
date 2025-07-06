"""
LeetCode Problem: Two Sum
=========================

Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Category: Arrays & Hashing

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Approach:
1. Hash Map Approach (Optimal):
   - Use a hash map to store numbers and their indices
   - For each number, check if (target - number) exists in the map
   - If found, return the current index and the stored index
   - Time: O(n), Space: O(n)

2. Brute Force Approach:
   - Use nested loops to check all pairs
   - Time: O(n²), Space: O(1)

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(n) - Hash map to store numbers and indices

Related Problems:
- Two Sum II (sorted array)
- 3Sum
- 4Sum
- Two Sum BST
"""

from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target using hash map approach.
        
        Args:
            nums: List of integers
            target: Target sum to find
            
        Returns:
            List containing indices of two numbers that sum to target
        """
        # Hash map to store number -> index mapping
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement needed
            complement = target - num
            
            # If complement exists in hash map, we found our pair
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # No solution found (though problem guarantees one exists)
        return []


class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach using nested loops.
        Less efficient but easier to understand.
        """
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []


# Test cases
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test the first example from the problem"""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        # Sort both lists since order doesn't matter
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_2(self):
        """Test the second example from the problem"""
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_3(self):
        """Test the third example from the problem"""
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]  # -3 + (-5) = -8
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        nums = [1, 5, 5, 10]
        target = 10
        expected = [1, 2]  # 5 + 5 = 10
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_large_numbers(self):
        """Test with large numbers"""
        nums = [1000000000, -1000000000, 1, 2]
        target = 0
        expected = [0, 1]  # 1000000000 + (-1000000000) = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))


# Manual testing (for quick verification)
def run_tests():
    """Run manual tests without unittest framework"""
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            "input": ([2, 7, 11, 15], 9),
            "expected": [0, 1],
            "description": "Example 1"
        },
        {
            "input": ([3, 2, 4], 6),
            "expected": [1, 2],
            "description": "Example 2"
        },
        {
            "input": ([3, 3], 6),
            "expected": [0, 1],
            "description": "Example 3"
        },
        {
            "input": ([-1, -2, -3, -4, -5], -8),
            "expected": [2, 4],
            "description": "Negative numbers"
        },
        {
            "input": ([1, 5, 5, 10], 10),
            "expected": [1, 2],
            "description": "Duplicate numbers"
        }
    ]
    
    print("Running manual tests for Two Sum...")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        nums, target = test_case["input"]
        result = solution.twoSum(nums, target)
        expected = test_case["expected"]
        
        # Sort both lists since order doesn't matter
        status = "✅ PASS" if sorted(result) == sorted(expected) else "❌ FAIL"
        print(f"Test {i} ({test_case['description']}): {status}")
        print(f"  Input: nums = {nums}, target = {target}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print()


if __name__ == "__main__":
    # Run manual tests
    run_tests()
    
    # Uncomment to run unittest tests
    # unittest.main() 