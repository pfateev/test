# GitHub Issue Commenter

This Python script allows users to automatically post comments to GitHub issues using the contents of a Markdown file. It leverages the GitHub API to access a specific repository and issue, and then posts the content of the provided Markdown file as a comment to the designated issue.

## Requirements

Before running the script, ensure you have the following requirements installed:

- Python 3.x
- `PyGithub`: This package is used to interact with the GitHub API.
- `python-dotenv`: This package is used to manage environment variables.

You can install these requirements using pip:

```bash
pip install PyGithub python-dotenv
```

## Setup

1. **Environment Variables**:
   - Create a `.env` file in the same directory as the script and add your GitHub token:
     ```
     GITHUB_TOKEN=your_github_personal_access_token
     ```
   - You can generate a new token by going to GitHub Settings > Developer settings > Personal access tokens.

2. **Repository Information**:
   - The script currently posts to the repository specified by `repo_owner` and `repo_name` in the script. Modify these variables in the script if you want to target a different repository.

## Usage

Run the script with the following command format:

```bash
python script.py <issue_number> <file_path>
```

### Parameters:

- `issue_number`: The number of the issue where the comment should be posted.
- `file_path`: The path to the Markdown file whose contents will be used as the comment. Ensure this is a `.md` file, as the script checks the file extension.

### Example:

```bash
python script.py 123 ./comments/update.md
```

This example will post the contents of `update.md` to issue number 123 in the repository defined in the script.

## Error Handling

- The script checks if the file extension is `.md` and will raise an error if a different file type is provided.
- Proper error messages are provided for common issues like missing command line arguments or file not found errors.

## Note

Ensure that your GitHub token has the appropriate permissions to interact with repositories and issues.