#!/usr/bin/env python3
import sys
import os
import re


def to_snake_case(name):
    return re.sub(r'\s+', '_', name.strip().lower())


def create_code_file(day, snake_name, problem_name, topic, difficulty):
    os.makedirs("code", exist_ok=True)
    path = f"code/day{day}_{snake_name}.py"
    content = f"""# Problem: {problem_name}
# Topic: {topic}
# Difficulty: {difficulty}


class Solution:
    def solve(self):
        # TODO: implement solution
        pass
"""
    with open(path, "w") as f:
        f.write(content)
    return path


def create_solution_file(day, snake_name, problem_name, topic, difficulty):
    os.makedirs("solutions", exist_ok=True)
    path = f"solutions/day{day}_{snake_name}.md"
    content = f"""# Day {day}: {problem_name}

- **Difficulty:** {difficulty}
- **Topic:** {topic}

## Approach



## Complexity

- **Time:**
- **Space:**

## Code

[View solution](../code/day{day}_{snake_name}.py)
"""
    with open(path, "w") as f:
        f.write(content)
    return path


def append_readme_row(day, problem_name, difficulty, topic, code_path, solution_path):
    row = f"| {day} | {problem_name} | {difficulty} | {topic} | [Solution]({code_path}) | [Writeup]({solution_path}) |\n"
    with open("README.md", "a") as f:
        f.write(row)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python add_problem.py <day_number> \"<problem_name>\" \"<topic>\" \"<difficulty>\"")
        sys.exit(1)

    day = sys.argv[1]
    problem_name = sys.argv[2]
    topic = sys.argv[3]
    difficulty = sys.argv[4]
    snake_name = to_snake_case(problem_name)

    code_path = create_code_file(day, snake_name, problem_name, topic, difficulty)
    solution_path = create_solution_file(day, snake_name, problem_name, topic, difficulty)
    append_readme_row(day, problem_name, difficulty, topic, code_path, solution_path)

    print(f"Created {code_path}")
    print(f"Created {solution_path}")
    print(f"Updated README.md")