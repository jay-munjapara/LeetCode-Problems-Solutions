import os
import requests


def get_problem_statement_from_leetcode(problem_slug):
    # GraphQL endpoint for LeetCode
    url = "https://leetcode.com/graphql/"

    # GraphQL query to fetch problem details by slug
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        content
        title
        difficulty
      }
    }
    """

    # Variables to pass to the query
    variables = {
        "titleSlug": problem_slug
    }

    # Send POST request with the query and variables
    response = requests.post(
        url, json={"query": query, "variables": variables})

    if response.status_code == 200:
        data = response.json()
        question = data.get("data", {}).get("question", {})
        if question:
            return question.get("content", "Problem statement not found.")
        else:
            print(f"Problem {problem_slug} not found.")
            return None
    else:
        print(
            f"Error fetching problem statement for {problem_slug}: {response.status_code}")
        return None


def create_problem_folder(base_path, problem_name, problem_slug):
    # Create the folder for the problem
    problem_dir = os.path.join(base_path, problem_name)

    # Check if the problem folder already exists, if not, create it
    if not os.path.exists(problem_dir):
        os.makedirs(problem_dir)
        print(f"Created folder for problem: {problem_name}")

    # Create the README.md file for the problem (fetch problem statement from LeetCode)
    readme_path = os.path.join(problem_dir, "README.md")
    if not os.path.exists(readme_path):
        problem_statement = get_problem_statement_from_leetcode(problem_slug)

        with open(readme_path, 'w') as readme_file:
            readme_file.write(f"# {problem_name}\n\n")
            readme_file.write("## Problem Statement\n")
            if problem_statement:
                # Write the problem statement
                readme_file.write(problem_statement)
            else:
                readme_file.write("Problem statement could not be fetched.\n")
        print(f"Created README.md for problem: {problem_name}")

    # Create a Python solution file (solution.py) for the problem
    solution_path = os.path.join(problem_dir, "solution.py")
    if not os.path.exists(solution_path):
        with open(solution_path, 'w') as solution_file:
            solution_file.write("# Write your Python solution here\n")
        print(f"Created solution.py for problem: {problem_name}")


if __name__ == "__main__":
    # Define the base path where the problems will be created (relative to the script's location)
    problems_base_path = os.path.join(
        os.path.dirname(__file__), "..", "problems")

    # Get problem name or number from user input
    problem_input = input(
        "Enter the problem name or the problem slug (e.g., 'two-sum'): ").strip().lower()

    # If the input is a name, convert it to slug (You can expand this as per your needs)
    name_to_slug = {
        "two sum": "two-sum",
        "climbing stairs": "climbing-stairs",
        "longest substring without repeating characters": "longest-substring-without-repeating-characters",
        "valid parentheses": "valid-parentheses",
        "merge intervals": "merge-intervals"
    }

    # Check if the problem input is in the dictionary of problem names
    # Default to problem_input if not found
    problem_slug = name_to_slug.get(problem_input, problem_input)
    problem_name = problem_input.replace(
        "-", " ").title()  # Format the name for folder

    # Create folder for the problem
    create_problem_folder(problems_base_path, problem_name, problem_slug)
