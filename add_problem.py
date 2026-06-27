#!/usr/bin/env python3
import sys
import os
import re
import subprocess


def to_snake_case(name):
    return re.sub(r'\s+', '_', name.strip().lower())


def create_code_file(problem_num, snake_name, problem_name, topic, difficulty):
    os.makedirs("code", exist_ok=True)
    path = f"code/{problem_num}_{snake_name}.py"
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


def to_lc_slug(name):
    return re.sub(r'\s+', '-', name.strip().lower())


def create_solution_file(problem_num, snake_name, problem_name, topic, difficulty):
    os.makedirs("solutions", exist_ok=True)
    path = f"solutions/{problem_num}_{snake_name}.md"
    slug = to_lc_slug(problem_name)
    lc_url = f"https://leetcode.com/problems/{slug}/"
    content = f"""# {problem_num}. {problem_name}

- **Difficulty:** {difficulty}
- **Topic:** {topic}

[LeetCode]({lc_url})

## Approach



## Complexity

- **Time:**
- **Space:**

## Code

[View solution](../code/{problem_num}_{snake_name}.py)
"""
    with open(path, "w") as f:
        f.write(content)
    return path, lc_url


def append_readme_row(problem_num, problem_name, difficulty, topic, code_path, solution_path, lc_url):
    row = f"| {problem_num} | {problem_name} | {difficulty} | {topic} | [Code]({code_path}) | [Solution]({solution_path}) | [Link]({lc_url}) |\n"
    with open("README.md", "a") as f:
        f.write(row)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python add_problem.py <problem_number> \"<problem_name>\" \"<topic>\" \"<difficulty>\"")
        sys.exit(1)

    problem_num = sys.argv[1]
    problem_name = sys.argv[2]
    topic = sys.argv[3]
    difficulty = sys.argv[4]
    snake_name = to_snake_case(problem_name)

    code_path = create_code_file(problem_num, snake_name, problem_name, topic, difficulty)
    solution_path, lc_url = create_solution_file(problem_num, snake_name, problem_name, topic, difficulty)
    append_readme_row(problem_num, problem_name, difficulty, topic, code_path, solution_path, lc_url)

    print(f"Created {code_path}")
    print(f"Created {solution_path}")
    print(f"Updated README.md")

    subprocess.run(["git", "add", code_path, solution_path, "README.md"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add {problem_num}. {problem_name}"], check=True)
    print("Committed to git")