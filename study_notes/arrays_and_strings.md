# 📚 Arrays & Strings Study Notes

## 🎯 Overview
Arrays and strings are fundamental data structures that appear in almost every programming problem. Mastering these concepts is crucial for solving LeetCode problems efficiently.

## 🔧 Common Techniques

### 1. Two Pointers
**When to use:** When you need to compare elements from different positions or find pairs.

**Common Patterns:**
- **Opposite ends:** Start from both ends and move inward
- **Same direction:** Both pointers move in the same direction
- **Fast and slow:** One pointer moves faster than the other

**Example Problems:**
- Two Sum II (sorted array)
- Valid Palindrome
- Container With Most Water
- 3Sum

**Template:**
```python
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process elements at left and right
        if condition:
            left += 1
        else:
            right -= 1
    
    return result
```

### 2. Sliding Window
**When to use:** When you need to find a subarray/substring that meets certain criteria.

**Types:**
- **Fixed size:** Window size is constant
- **Variable size:** Window size changes based on conditions

**Example Problems:**
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Maximum Sum Subarray of Size K

**Template:**
```python
def sliding_window_template(arr, k):
    window_start = 0
    window_sum = 0
    result = []
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        # Shrink window if needed
        while window_end - window_start + 1 >= k:
            result.append(window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    return result
```

### 3. Prefix Sum
**When to use:** When you need to calculate sum of subarrays efficiently.

**Key Insight:** Precompute cumulative sums to get range sums in O(1).

**Example Problems:**
- Range Sum Query
- Subarray Sum Equals K
- Maximum Subarray

**Template:**
```python
def prefix_sum_template(arr):
    prefix = [0] * (len(arr) + 1)
    
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    
    # Get sum from index i to j: prefix[j + 1] - prefix[i]
    return prefix
```

### 4. Kadane's Algorithm
**When to use:** Finding maximum sum subarray.

**Key Insight:** If current sum becomes negative, start fresh from current element.

**Example Problems:**
- Maximum Subarray
- Maximum Sum Circular Subarray

**Template:**
```python
def kadane_algorithm(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
```

## 🧩 Common Patterns

### 1. Frequency Counting
```python
from collections import Counter

def frequency_count(arr):
    freq = Counter(arr)
    # Process frequency map
    return result
```

### 2. Sorting for Optimization
```python
def sort_and_solve(arr):
    arr.sort()  # Often helps with two pointers or greedy approaches
    # Solve the problem
    return result
```

### 3. Hash Map for Lookups
```python
def hash_map_solution(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## ⚡ Time Complexity Cheat Sheet

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access by index | O(1) | O(1) |
| Search by value | O(n) | O(1) |
| Insert at end | O(1) | O(1) |
| Insert at beginning | O(n) | O(1) |
| Delete from end | O(1) | O(1) |
| Delete from beginning | O(n) | O(1) |
| Two pointers | O(n) | O(1) |
| Sliding window | O(n) | O(1) |
| Prefix sum | O(n) | O(n) |

## 🎯 Problem Categories

### Easy Problems (1-2)
- Two Sum
- Valid Palindrome
- Maximum Subarray
- Remove Duplicates from Sorted Array

### Medium Problems (3-4)
- 3Sum
- Container With Most Water
- Longest Substring Without Repeating Characters
- Group Anagrams

### Hard Problems (5)
- Median of Two Sorted Arrays
- Minimum Window Substring
- Trapping Rain Water

## 💡 Tips & Tricks

1. **Always consider edge cases:**
   - Empty arrays
   - Single element
   - All same elements
   - Negative numbers

2. **Space-time tradeoffs:**
   - Use hash maps for O(1) lookups
   - Use sorting when order doesn't matter
   - Use two pointers to avoid extra space

3. **Common optimizations:**
   - Early termination
   - Skip duplicates in sorted arrays
   - Use mathematical properties

4. **Debugging techniques:**
   - Print intermediate values
   - Use small test cases
   - Check boundary conditions

## 🔗 Related Topics

- [Two Pointers](./two_pointers.md)
- [Sliding Window](./sliding_window.md)
- [Dynamic Programming](./dynamic_programming.md)
- [Hash Tables](./hash_tables.md)

---

*Practice makes perfect! Keep solving problems in this category to build intuition.* 🚀 