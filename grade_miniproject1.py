# Auto grading miniproject 1 on flake8 which determines any failing format and syntax errors
import os
import subprocess

# Get the current directory
current_directory = os.getcwd()

ignore_folders = [".git", ".github", "HieuNguyen", "Homework-HuuTuan", "HuyTran"]

for folder_name in os.listdir(current_directory):
    folder_path = os.path.join(current_directory, folder_name)

    # Check if it's a directory
    if os.path.isdir(folder_path) and folder_name not in ignore_folders:
        # Construct the flake8 command
        output_file = f"{folder_name}/{folder_name}.txt"
        command = [
            "flake8",
            "-v",
            "--ignore=E501",
            "--show-source",
            "--statistics",
            "--format=pylint",
            f"--output-file={output_file}",
            folder_path,
        ]

        # Execute the command
        try:
            subprocess.run(command, check=True)
            print(f"Executed flake8 for {folder_name}, output saved to {output_file}.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing flake8 for {folder_name}: {e}")
