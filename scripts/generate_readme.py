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
        # Title and description
        readme_file.write("# LeetCode Problems and Solutions\n\n")
        readme_file.write("This repository contains solutions to various LeetCode problems. Each problem is organized in its own directory, with the problem statement and solutions in multiple programming languages. The repository aims to provide organized solutions and problem descriptions, helping users learn and improve their problem-solving skills.\n\n")

        # Directory Structure section
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
        readme_file.write("├── scripts/\n")
        # Added this line for `generate_readme.py`
        readme_file.write("│   ├── generate_readme.py\n")
        # Added this line for `generate_problem_folders.py`
        readme_file.write("│   └── generate_problem_folders.py\n")
        readme_file.write("```\n\n")

        # Problems List section
        readme_file.write("## Problems List\n\n")
        for problem_dir in problem_directories:
            problem_path = os.path.join(
                problems_base_path, problem_dir, 'README.md')
            if os.path.exists(problem_path):
                problem_title = get_problem_title(problem_path)
                readme_file.write(
                    f"- [{problem_title}](problems/{problem_dir}/README.md)\n")

        # How to Navigate section
        readme_file.write("\n## How to Navigate\n\n")
        readme_file.write(
            "Each problem is located in the `problems/` directory. Navigate to the problem's directory to find the problem statement and solutions in different programming languages.\n\n")

        # How to Use `generate_problem_folders.py`
        readme_file.write("## How to Use `generate_problem_folders.py`\n\n")
        readme_file.write("This script helps automate the process of creating problem directories inside the `problems/` folder. It fetches the problem statement from LeetCode and creates a folder for each problem with the necessary files for you to upload your solution.\n\n")

        # How it works section
        readme_file.write("### How it Works:\n\n")
        readme_file.write(
            "1. **Problem Folder Creation**: The script fetches the problem statement from LeetCode using its slug and creates a directory for each problem inside the `problems/` folder.\n")
        readme_file.write(
            "2. **Problem Statement**: The problem statement is added to a `README.md` file inside the problem folder.\n")
        readme_file.write(
            "3. **Solution File**: An empty `solution.py` file is created where you can add your Python solution.\n\n")

        # Instructions to enter the problem name
        readme_file.write("### How to Enter the Problem Name:\n\n")
        readme_file.write("1. Run the script `generate_problem_folders.py`.\n")
        readme_file.write(
            "2. When prompted, enter the problem name or slug (e.g., `two-sum` for the Two Sum problem).\n")
        readme_file.write(
            "3. The script will create the following structure:\n")
        readme_file.write(
            "   - A folder named after the problem in the `problems/` directory.\n")
        readme_file.write(
            "   - A `README.md` file with the problem statement fetched from LeetCode.\n")
        readme_file.write(
            "   - An empty `solution.py` file where you can add your Python solution.\n\n")

        # Contributing section
        readme_file.write("## How to Contribute\n\n")
        readme_file.write("1. Fork this repository.\n")
        readme_file.write(
            "2. Create a new branch (`git checkout -b feature/problem-xyz`), replacing `problem-xyz` with the actual problem name.\n")
        readme_file.write(
            "3. Add your solutions in the respective problem directory inside the `problems/` folder.\n")
        readme_file.write(
            "4. Update the **Problems List** in this `README.md` to include your new problem.\n")
        readme_file.write(
            "5. Commit your changes (`git commit -m 'Add solution for problem xyz'`).\n")
        readme_file.write(
            "6. Push your branch to your GitHub repository (`git push origin feature/problem-xyz`).\n")
        readme_file.write(
            "7. Create a Pull Request to merge your changes into the main repository.\n")

        # License section
        readme_file.write("\n## License\n\n")
        readme_file.write(
            "This repository is open-source and available under the MIT License. Feel free to contribute and share!\n")


if __name__ == "__main__":
    # Define the base path where the problems are located
    problems_base_path = os.path.join(os.path.dirname(
        __file__), "..", "problems")  # Relative path
    output_path = os.path.join(os.path.dirname(
        __file__), "..", "README.md")  # Output path for README.md

    # Generate or update the main README.md file
    generate_main_readme(problems_base_path, output_path)
