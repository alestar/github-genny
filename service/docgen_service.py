# create method to generate documentation for a code file
from utils.github_utils import clone_repo, crawl_repo
from utils.docgen_utils import generate_doc

def docgen_run():
    url = input("Enter GitHub repo URL: ").strip()
    local_path = clone_repo(url)
    code_files = crawl_repo(local_path, file_types=['.py', 'java', 'txt'])

    print(f"\n📄 Generating documentation for {len(code_files)} Python files...")

    for file in code_files:
        relative_path = file['path'].replace(local_path + "/", "")
        print(f"\n🔍 Documenting: {relative_path}")
        doc = generate_doc(file['content'])
        print(f"\n📝 Generated Documentation for {relative_path}:\n")
        print(doc)
        print("\n" + "="*60)