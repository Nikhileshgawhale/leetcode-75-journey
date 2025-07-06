# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**LeetCode Link:** [Two Sum](https://leetcode.com/problems/two-sum/)

## Examples

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Solutions

### 1. Hash Map Approach (Optimal)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

This is the most efficient approach that uses a hash map to store numbers and their indices.

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []
```

**How it works:**
1. Use a hash map to store each number and its index
2. For each number, calculate the complement (target - number)
3. If the complement exists in the hash map, we found our pair
4. Otherwise, store the current number and continue

### 2. Brute Force Approach

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

A straightforward approach using nested loops (less efficient but easier to understand).

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []
```

## Key Insights

1. **Hash Map for O(1) Lookups:** Using a hash map allows us to check if a complement exists in constant time.

2. **Single Pass:** We can solve this in a single pass through the array, making it O(n) time complexity.

3. **Order Doesn't Matter:** The problem allows returning the answer in any order, so we don't need to worry about the order of indices.

## Edge Cases to Consider

- **Duplicate Numbers:** The solution handles cases where the same number appears multiple times
- **Negative Numbers:** Works correctly with negative numbers
- **Large Numbers:** Handles large integers within the constraints
- **Minimum Array Size:** Works with arrays of size 2 (minimum constraint)

## Related Problems

- [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Medium)
- [3Sum](https://leetcode.com/problems/3sum/) (Medium)
- [4Sum](https://leetcode.com/problems/4sum/) (Medium)
- [Two Sum BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) (Easy)

## Practice Problems

To strengthen your understanding of this pattern, try these related problems:

1. **Easy:**
   - [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
   - [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

2. **Medium:**
   - [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
   - [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

---

**Solution File:** [solution.py](./solution.py) 