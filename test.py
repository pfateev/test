import sys
import os
from github import Github, GithubException
from github import Auth
import issue_poster
from dotenv import load_dotenv
import unittest

class TestIssuePoster(unittest.TestCase):
    # Setup
    load_dotenv()
    token = os.getenv('GITHUB_TOKEN')
    auth = Auth.Token(token)
    g = Github(auth=auth)
    repo = g.get_repo("pfateev/test")
    issue_number = 1

    def test_add_valid_comment(self):
        # get number of current comments
        issue = self.repo.get_issue(number=self.issue_number)
        currCount = issue.comments
        # perform add
        issue_poster.post_issue_comment(self.token, 'pfateev', 'test', self.issue_number, 'cli/test.md')
        updatedIssue = self.repo.get_issue(number=self.issue_number)
        newCount = updatedIssue.comments
        self.assertTrue(newCount - currCount == 1)
    
    def test_bad_filename(self):
        with self.assertRaises(FileNotFoundError):
            issue_poster.post_issue_comment(self.token, 'pfateev', 'test', self.issue_number, 'test.md')

    def test_invalid_issue(self):
        with self.assertRaises(GithubException):
            issue_poster.post_issue_comment(self.token, 'pfateev', 'test', 2, 'test.md')
    
    # def test_non_md_file():
    #     pass

if __name__ == '__main__':
    unittest.main()