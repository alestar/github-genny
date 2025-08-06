# github_api_utils.py

import requests

GITHUB_API = "https://api.github.com"

def get_repo_file_tree(owner, repo, branch="main"):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to get file tree: {response.text}")
    tree = response.json()['tree']
    return [item['path'] for item in tree if item['type'] == 'blob']


def fetch_file_content(owner, repo, path, branch="main"):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {path}")
        return None
    return response.text


def get_code_files(owner, repo, branch="main", file_types=None):
    if file_types is None:
        file_types = ['.py', '.js', '.ts', '.java']

    all_files = get_repo_file_tree(owner, repo, branch)
    code_files = []

    for path in all_files:
        if any(path.endswith(ext) for ext in file_types):
            content = fetch_file_content(owner, repo, path, branch)
            if content:
                code_files.append({
                    'path': path,
                    'content': content
                })

    print(f"Fetched {len(code_files)} code files from GitHub API.")
    return code_files
