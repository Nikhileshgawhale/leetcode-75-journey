#!/usr/bin/env python3
"""
Solution Creator Script
=======================

This script helps you quickly create new LeetCode solution files using the template.
Usage: python create_solution.py <difficulty> <problem-name> [problem-number]
"""

import os
import sys
import shutil
from datetime import datetime


def create_solution_structure(difficulty, problem_name, problem_number=None):
    """
    Create a new solution structure for a LeetCode problem.
    
    Args:
        difficulty (str): 'easy', 'medium', or 'hard'
        problem_name (str): Name of the problem (e.g., 'two-sum')
        problem_number (str, optional): Problem number (e.g., '1')
    """
    
    # Validate difficulty
    valid_difficulties = ['easy', 'medium', 'hard']
    if difficulty.lower() not in valid_difficulties:
        print(f"❌ Error: Difficulty must be one of {valid_difficulties}")
        return False
    
    # Create directory path
    solution_dir = f"solutions/{difficulty.lower()}/{problem_name.lower()}"
    
    # Create directory
    try:
        os.makedirs(solution_dir, exist_ok=True)
        print(f"✅ Created directory: {solution_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return False
    
    # Copy template
    template_path = "templates/solution_template.py"
    solution_path = f"{solution_dir}/solution.py"
    
    try:
        shutil.copy2(template_path, solution_path)
        print(f"✅ Copied template to: {solution_path}")
    except Exception as e:
        print(f"❌ Error copying template: {e}")
        return False
    
    # Create README
    readme_path = f"{solution_dir}/README.md"
    create_readme(readme_path, problem_name, problem_number)
    
    # Update progress tracker
    update_progress_tracker(problem_name, difficulty, problem_number)
    
    print(f"\n🎉 Successfully created solution structure for {problem_name}!")
    print(f"📁 Location: {solution_dir}")
    print(f"📝 Next steps:")
    print(f"   1. Edit {solution_path} to implement your solution")
    print(f"   2. Update {readme_path} with problem details")
    print(f"   3. Run your solution: python {solution_path}")
    
    return True


def create_readme(readme_path, problem_name, problem_number=None):
    """Create a basic README file for the problem."""
    
    # Convert kebab-case to title case
    title = problem_name.replace('-', ' ').title()
    
    readme_content = f"""# {title}

## Problem Description

[Add problem description here]

**LeetCode Link:** [{title}](https://leetcode.com/problems/{problem_name}/)

## Examples

### Example 1:
```
Input: [add input here]
Output: [add output here]
Explanation: [add explanation here]
```

## Constraints

- [Add constraints here]

## Solutions

### Approach 1

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

[Add solution description here]

```python
def solution(self, input_param):
    # Your implementation here
    pass
```

## Key Insights

1. [Add key insight 1]
2. [Add key insight 2]

## Edge Cases to Consider

- [Add edge case 1]
- [Add edge case 2]

## Related Problems

- [Related problem 1]
- [Related problem 2]

---

**Solution File:** [solution.py](./solution.py)
"""
    
    try:
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        print(f"✅ Created README: {readme_path}")
    except Exception as e:
        print(f"❌ Error creating README: {e}")


def update_progress_tracker(problem_name, difficulty, problem_number=None):
    """Update the progress tracker with the new problem."""
    
    tracker_path = "progress_tracker.md"
    
    try:
        with open(tracker_path, 'r') as f:
            content = f.read()
        
        # Find the daily log section and add new entry
        if "## 📈 Daily Log" in content:
            # Get current date
            current_date = datetime.now().strftime("%Y-%m-%d")
            
            # Create new entry
            new_entry = f"| {current_date} | [{problem_name}](link) | {difficulty.title()} | [Topic] | ⏳ Pending | [Add notes] |"
            
            # Insert after the header
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if "## 📈 Daily Log" in line:
                    # Find the table header
                    for j in range(i, len(lines)):
                        if "|-----|------|---------|------------|-------|--------|-------|" in lines[j]:
                            # Insert new entry after the separator
                            lines.insert(j + 1, new_entry)
                            break
                    break
            
            # Write back to file
            with open(tracker_path, 'w') as f:
                f.write('\n'.join(lines))
            
            print(f"✅ Updated progress tracker")
    
    except Exception as e:
        print(f"⚠️  Warning: Could not update progress tracker: {e}")


def main():
    """Main function to handle command line arguments."""
    
    if len(sys.argv) < 3:
        print("Usage: python create_solution.py <difficulty> <problem-name> [problem-number]")
        print("Example: python create_solution.py easy two-sum 1")
        print("Example: python create_solution.py medium add-two-numbers")
        return
    
    difficulty = sys.argv[1]
    problem_name = sys.argv[2]
    problem_number = sys.argv[3] if len(sys.argv) > 3 else None
    
    print(f"🚀 Creating solution for: {problem_name}")
    print(f"📊 Difficulty: {difficulty}")
    if problem_number:
        print(f"🔢 Problem Number: {problem_number}")
    print()
    
    success = create_solution_structure(difficulty, problem_name, problem_number)
    
    if success:
        print(f"\n✨ You're all set! Happy coding! 🐍")
    else:
        print(f"\n❌ Failed to create solution structure.")


if __name__ == "__main__":
    main() 