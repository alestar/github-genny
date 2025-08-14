
from utils.github_utils import clone_repo, crawl_repo

def repo_crawl_local():
    # Step 1: Input GitHub repo
    github_url = input("Enter the GitHub repo URL to clone: ")

    # Step 2: Clone it
    local_path = clone_repo(github_url)

    # Step 3: Crawl the repo and collect code
    file_types = ['.py', '.js', '.ts', '.java']  # Customize as needed
    code_files = crawl_repo(local_path, file_types=file_types)

    # Step 4: Print summary
    for file in code_files:
        print(f"\nFile: {file['path']}")
        print("----- CODE SNIPPET -----")
        print(file['content'][:300], '...')  # Print first 300 characters

    print(f"\nTotal files crawled: {len(code_files)}")
