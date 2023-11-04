import os
import re

import toml
import time

import argparse
import subprocess
import contextlib

from typing import Iterator
from loguru import logger

logger.add("tools.log", format="{time} {level} {message}")


def spinning_cursor() -> Iterator[str]:
    """Generate a spinning cursor for the CLI."""
    while True:
        for cursor in "|/-\\":
            yield cursor


@contextlib.contextmanager
def log_with_spinner(message: str):
    """Context manager to display a spinning cursor with a log message."""
    spinner = spinning_cursor()

    for _ in range(10):
        logger.opt(raw=True).info(f"\r{next(spinner)} {message} ")
        time.sleep(0.1)
    yield


def update_import_statements(file_path: str, old_name: str, new_name: str) -> None:
    """Update the import statements from old_name to new_name in the given file."""
    with open(file_path, "r") as file:
        filedata = file.read()

    old_import_pattern = rf"\b{re.escape(old_name)}\."
    new_import_pattern = f"{new_name}."

    filedata, count = re.subn(old_import_pattern, new_import_pattern, filedata)

    if count > 0:
        with open(file_path, "w") as file:
            file.write(filedata)

        with log_with_spinner(f"Updated {count} import(s) in file"):
            logger.info(f"Updated imports in {file_path}")


def update_pyproject_name(file_path: str, new_name: str) -> None:
    """Update the project name in pyproject.toml."""
    with open(file_path, "r") as file:
        data = toml.load(file)

    if "tool" in data and "poetry" in data["tool"]:
        data["tool"]["poetry"]["name"] = new_name

        with open(file_path, "w") as file:
            toml.dump(data, file)

        logger.info(f"Updated project name in pyproject.toml to {new_name}")


def update_makefile_directory_references(
    file_path: str, old_name: str, new_name: str
) -> None:
    """Update the directory references in the Makefile."""
    with open(file_path, "r") as file:
        filedata = file.read()

    directory_pattern = rf"{re.escape(old_name)}/"
    filedata, count = re.subn(directory_pattern, f"{new_name}/", filedata)

    if count > 0:
        with open(file_path, "w") as file:
            file.write(filedata)

        logger.info(f"Updated {count} directory reference(s) in Makefile")


def find_and_update_files(directory: str, old_name: str, new_name: str) -> None:
    """Find and update import statements in all Python files in the directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                update_import_statements(os.path.join(root, file), old_name, new_name)


def rename_directory(old_name: str, new_name: str) -> None:
    """Rename the directory from old_name to new_name."""
    with log_with_spinner("Renaming directory to the new name"):
        os.rename(old_name, new_name)
        logger.info(f"Renamed directory from {old_name} to {new_name}")


def reset_git_history(commit_message: str = "feat: initial commit") -> None:
    """Reset Git history with a single commit."""
    try:
        # Remove the .git directory and re-initialize it.
        subprocess.check_call(["rm", "-rf", ".git"])
        subprocess.check_call(["git", "init", "--initial-branch=main"])

        # Add all files to the Git index and commit them.
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-m", commit_message])

        logger.info("Git history reset to a single initial commit.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to reset Git history: {e}")


def is_python_project(directory: str) -> bool:
    """Check if the directory is a Python project by looking for pyproject.toml."""
    return os.path.isfile(os.path.join(directory, "pyproject.toml"))


def self_destruct(script_file: str) -> None:
    """Self destruct the script file."""
    try:
        os.remove(script_file)
        logger.info("The script has self-destructed.")
    except OSError as e:
        logger.error(f"Failed to self-destruct the script file: {e}")


def main():
    """Run the main script functionality with CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Rename a Python package, reset Git history if required, and self-destruct the script."
    )

    parser.add_argument(
        "old_name",
        help="Specify the current directory name to rename.",
    )

    parser.add_argument(
        "new_name",
        help="Specify the new directory name to apply.",
    )

    parser.add_argument(
        "--reset-git",
        action="store_true",
        help="Optionally reset Git history with an initial commit.",
    )

    parser.add_argument(
        "--self-destruct",
        action="store_true",
        help="Self destruct the script after execution.",
    )

    args, unknown = parser.parse_known_args()

    if unknown:
        logger.error("Unknown arguments: {}".format(" ".join(unknown)))
        parser.print_help()
        return

    if not is_python_project("."):
        logger.error("This directory does not appear to be a Python project.")
        return

    try:
        rename_directory(
            args.old_name,
            args.new_name,
        )

        find_and_update_files(
            ".",
            args.old_name,
            args.new_name,
        )

        pyproject_path = os.path.join(".", "pyproject.toml")
        makefile_path = os.path.join(".", "Makefile")

        if os.path.isfile(pyproject_path):
            update_pyproject_name(
                pyproject_path,
                args.new_name,
            )

        if os.path.isfile(makefile_path):
            update_makefile_directory_references(
                makefile_path,
                args.old_name,
                args.new_name,
            )

        if args.reset_git:
            reset_git_history()

        if args.self_destruct:
            self_destruct(__file__)

    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
