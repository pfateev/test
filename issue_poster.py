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

    if get_file_extension(file_path) != '.md':
        print("Usage: file_path must point to a .md file")
        sys.exit(1)

    post_issue_comment(os.getenv('GITHUB_TOKEN'), repo_owner, repo_name, issue_number, file_path)
    

def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def post_issue_comment(token, repo_owner, repo_name, issue_number, file_path):
    auth = Auth.Token(token)

    g = Github(auth=auth)

    repo = g.get_repo(f"{repo_owner}/{repo_name}")

    issue = repo.get_issue(number=issue_number)

    # Read markdown content from the file
    try:
        with open(file_path, 'r') as file:
            markdown_content = file.read()
    except FileNotFoundError:
        print("The specified file was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    comment = issue.create_comment(markdown_content)

    print("Comment created: ", comment.html_url)
    return

if __name__ == "__main__":
    main()
