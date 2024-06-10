import os

def get_problem_directories(base_path):
    return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

def get_problem_title(readme_path):
    with open(readme_path, 'r') as file:
        for line in file:
            if line.startswith("#"):
                return line.strip("#").strip()
    return "Unknown Title"

def generate_main_readme(problems_base_path, output_path):
    problem_directories = sorted(get_problem_directories(problems_base_path))
    with open(output_path, 'w') as readme_file:
        readme_file.write("# LeetCode Problems and Solutions\n\n")
        readme_file.write("This repository contains solutions to various LeetCode problems. Each problem is organized in its own directory, with the problem statement and solutions in multiple programming languages.\n\n")
        
        # Add directory structure
        readme_file.write("## Directory Structure\n\n")
        readme_file.write("```\n")
        readme_file.write("LeetCode-Problems-Solutions/\n")
        readme_file.write("│\n")
        readme_file.write("├── README.md\n")
        readme_file.write("├── problems/\n")
        for problem_dir in problem_directories:
            readme_file.write(f"│   ├── {problem_dir}/\n")
            readme_file.write(f"│   │   ├── README.md\n")
            # Assuming you have solutions in multiple languages
            for lang in ['solution.py', 'solution.cpp', 'solution.java']:
                if os.path.exists(os.path.join(problems_base_path, problem_dir, lang)):
                    readme_file.write(f"│   │   ├── {lang}\n")
        readme_file.write("└── scripts/\n")
        readme_file.write("    └── generate_readme.py\n")
        readme_file.write("```\n\n")
        
        readme_file.write("## Problems List\n\n")
        for problem_dir in problem_directories:
            problem_path = os.path.join(problems_base_path, problem_dir, 'README.md')
            if os.path.exists(problem_path):
                problem_title = get_problem_title(problem_path)
                readme_file.write(f"- [{problem_title}](problems/{problem_dir}/README.md)\n")

if __name__ == "__main__":
    problems_base_path = "problems"
    output_path = "README.md"
    generate_main_readme(problems_base_path, output_path)
