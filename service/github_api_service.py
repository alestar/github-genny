
# main.py

from utils.github_api_utils import get_code_files

def repo_crawl_in_mem():
    url = input("Enter GitHub repo URL (e.g. https://github.com/psf/requests): ").strip()

    try:
        owner, repo = url.split("github.com/")[1].split("/")[:2]
    except Exception as e:
        print("Invalid GitHub URL format.")
        return

    branch = "main"  # or "master", depending on the repo

    code_files = get_code_files(owner, repo, branch)

    for file in code_files:
        print(f"\nFile: {file['path']}")
        print("----- CODE SNIPPET -----")
        print(file['content'][:300], '...')

    print(f"\nTotal files fetched: {len(code_files)}")
