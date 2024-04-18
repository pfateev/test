import sys
import os
from github import Github
from github import Auth
from dotenv import load_dotenv

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <issue_number> <file_path>")
        sys.exit(1)
    load_dotenv()
    
    repo_owner = 'pfateev'
    repo_name = 'test'
    issue_number = int(sys.argv[1])
    file_path = sys.argv[2]

    post_issue_comment(os.getenv('GITHUB_TOKEN'), repo_owner, repo_name, issue_number, file_path)
    

def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def post_issue_comment(token, repo_owner, repo_name, issue_number, file_path):
    """Posts a comment on a GitHub issue using content from a markdown file.

    Requires a personal access token to authenticate with GitHub and uses the
    markdown file specified by file_path to create a comment on the issue identified by
    issue_number in the repository owned by repo_owner under repo_name.
    
    Args:
        token (str): The GitHub personal access token for authentication.
        repo_owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        issue_number (int): The number of the issue to which the comment will be added.
        file_path (str): The file path of the markdown file whose contents will be used for the comment.

    Raises:
        ValueError: If the file specified by file_path is not a markdown file (i.e., does not have a '.md' extension).
        FileNotFoundError: If the markdown file specified by file_path cannot be found.
        Exception: For other issues that occur while reading the file.
        GithubException: For exceptions raised by Github API

    Returns:
        None: This function does not return any value but prints the HTML URL of the created comment.
    """
    if get_file_extension(file_path) != '.md':
        raise ValueError('Usage: file_path must point to a .md file')
    
    auth = Auth.Token(token)

    g = Github(auth=auth)

    repo = g.get_repo(f"{repo_owner}/{repo_name}")

    issue = repo.get_issue(number=issue_number)

    # Read markdown content from the file
    try:
        with open(file_path, 'r') as file:
            markdown_content = file.read()
    except FileNotFoundError:
        raise
    except Exception as e:
        raise(e)

    comment = issue.create_comment(markdown_content)

    print("Comment created: ", comment.html_url)
    return

if __name__ == "__main__":
    main()
