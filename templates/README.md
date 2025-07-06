# 📝 Solution Templates

This directory contains templates and utilities to help you create consistent, well-documented solutions for LeetCode problems.

## 🎯 Available Templates

### 1. `solution_template.py`
A comprehensive Python template for LeetCode problems that includes:
- Problem description section
- Multiple solution approaches
- Comprehensive test cases
- Time and space complexity analysis
- Related problems section

## 🚀 How to Use

### Creating a New Solution

1. **Copy the template:**
   ```bash
   cp templates/solution_template.py solutions/easy/your-problem-name/solution.py
   ```

2. **Fill in the details:**
   - Replace `[Problem Name]` with actual problem name
   - Add the LeetCode problem link
   - Copy the problem description
   - Implement your solution
   - Add test cases

3. **Example structure:**
   ```
   solutions/
   ├── easy/
   │   └── two-sum/
   │       ├── solution.py
   │       └── README.md
   ├── medium/
   │   └── add-two-numbers/
   │       ├── solution.py
   │       └── README.md
   └── hard/
       └── median-of-two-sorted-arrays/
           ├── solution.py
           └── README.md
   ```

### Template Sections

#### Header Section
```python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Category: Arrays & Hashing
"""
```

#### Solution Class
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Your implementation here
        pass
```

#### Test Cases
```python
def test_example_1(self):
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    result = self.solution.twoSum(nums, target)
    self.assertEqual(result, expected)
```

## 📋 Best Practices

1. **Always include:**
   - Problem description and link
   - Time and space complexity
   - Test cases for examples and edge cases
   - Clear comments explaining your approach

2. **Naming conventions:**
   - Use kebab-case for folder names: `two-sum`, `add-two-numbers`
   - Use descriptive method names
   - Include type hints

3. **Documentation:**
   - Explain your approach in detail
   - Mention alternative solutions if applicable
   - List related problems for practice

4. **Testing:**
   - Include all examples from the problem
   - Add edge cases (empty arrays, single elements, etc.)
   - Test both manual and unittest approaches

## 🔧 Quick Setup Script

You can create a quick setup script to automate the template copying:

```bash
#!/bin/bash
# create_solution.sh

if [ $# -eq 0 ]; then
    echo "Usage: ./create_solution.sh <difficulty> <problem-name>"
    echo "Example: ./create_solution.sh easy two-sum"
    exit 1
fi

difficulty=$1
problem_name=$2

# Create directory
mkdir -p "solutions/$difficulty/$problem_name"

# Copy template
cp "templates/solution_template.py" "solutions/$difficulty/$problem_name/solution.py"

# Create README
cat > "solutions/$difficulty/$problem_name/README.md" << EOF
# $problem_name

[Add problem description here]

## Solution
- [solution.py](./solution.py)

## Related Problems
- [Add related problems here]
EOF

echo "Created solution structure for $problem_name in solutions/$difficulty/"
```

## 📚 Additional Resources

- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Python unittest](https://docs.python.org/3/library/unittest.html)
- [LeetCode Problem Patterns](https://seanprashad.com/leetcode-patterns/)

---

*Happy coding! 🐍* 