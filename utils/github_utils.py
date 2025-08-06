# github_utils.py

import os
from git import Repo


def clone_repo(github_url: str, local_dir: str = "cloned_repo") -> str:
    """
    Clone a GitHub repo into the local_dir.
    Returns the local path to the cloned repo.
    """
    if os.path.exists(local_dir):
        print(f"Removing existing directory: {local_dir}")
        import shutil
        shutil.rmtree(local_dir)

    print(f"Cloning repo from {github_url}...")
    Repo.clone_from(github_url, local_dir)
    print("Repository cloned successfully.")
    return local_dir


def crawl_repo(directory: str, file_types=None):
    """
    Recursively collects code files from the directory.
    Returns a list of dicts with 'path' and 'content'.
    """
    if file_types is None:
        file_types = ['.py']  # Default to Python files

    code_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(file_types)):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        code_files.append({
                            'path': full_path,
                            'content': f.read()
                        })
                except Exception as e:
                    print(f"Failed to read {full_path}: {e}")

    print(f"Found {len(code_files)} code files.")
    return code_files
