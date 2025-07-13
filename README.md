# LeetCode Problems and Solutions

This repository contains solutions to various LeetCode problems. Each problem is organized in its own directory, with the problem statement and solutions in multiple programming languages. The repository aims to provide organized solutions and problem descriptions, helping users learn and improve their problem-solving skills.

## Directory Structure

```
LeetCode-Problems-Solutions/
│
├── README.md
├── problems/
│   ├── Contains Duplicate/
│   │   ├── README.md
│   │   ├── solution.py
│   ├── Valid Anagram/
│   │   ├── README.md
│   │   ├── solution.py
├── scripts/
│   ├── generate_readme.py
│   └── generate_problem_folders.py
```

## Problems List

- [Contains Duplicate](problems/Contains%20Duplicate/README.md)
- [Valid Anagram](problems/Valid%20Anagram/README.md)

## How to Navigate

Each problem is located in the `problems/` directory. Navigate to the problem's directory to find the problem statement and solutions in different programming languages.

## How to Use `generate_problem_folders.py`

This script helps automate the process of creating problem directories inside the `problems/` folder. It fetches the problem statement from LeetCode and creates a folder for each problem with the necessary files for you to upload your solution.

### How it Works:

1. **Problem Folder Creation**: The script fetches the problem statement from LeetCode using its slug and creates a directory for each problem inside the `problems/` folder.
2. **Problem Statement**: The problem statement is added to a `README.md` file inside the problem folder.
3. **Solution File**: An empty `solution.py` file is created where you can add your Python solution.

### How to Enter the Problem Name:

1. Run the script `generate_problem_folders.py`.
2. When prompted, enter the problem name or slug (e.g., `two-sum` for the Two Sum problem).
3. The script will create the following structure:
   - A folder named after the problem in the `problems/` directory.
   - A `README.md` file with the problem statement fetched from LeetCode.
   - An empty `solution.py` file where you can add your Python solution.

## How to Contribute

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/problem-xyz`), replacing `problem-xyz` with the actual problem name.
3. Add your solutions in the respective problem directory inside the `problems/` folder.
4. Update the **Problems List** in this `README.md` to include your new problem.
5. Commit your changes (`git commit -m 'Add solution for problem xyz'`).
6. Push your branch to your GitHub repository (`git push origin feature/problem-xyz`).
7. Create a Pull Request to merge your changes into the main repository.

## License

This repository is open-source and available under the MIT License. Feel free to contribute and share!
