# main.py
import argparse

from service.docgen_service import docgen_run_single


def main():
    """
    Main entry point for the documentation generator.
    This will:
      1. Ask for a GitHub repo URL
      2. Clone the repo locally
      3. Crawl for .py, .java, and .txt files
      4. Generate documentation for each file using the LLM
      5. Save all documentation into a single combined Markdown file
    """
    parser = argparse.ArgumentParser(
        description="Generate documentation from a GitHub repository using an LLM."
    )

    parser.add_argument(
        "url",
        type=str,
        help="GitHub repository URL to document"
    )
    parser.add_argument(
        "-o", "--output",
        default="DOCUMENTATION.md",
        help="Output markdown file (default: DOCUMENTATION.md)"
    )

    parser.add_argument(
        "-t", "--types",
        nargs="+",
        default=[".py", ".java", ".txt"],
        help="File extensions to include (default: .py .java .txt)"
    )

    parser.add_argument(
        "-k", "--key",
        default="",
        help="LLM API Key"
    )
    args = parser.parse_args()

    docgen_run_single(args.url,args.output)

if __name__ == "__main__":
    main()