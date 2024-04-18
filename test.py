import sys
import os
from github import Github
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
        issue_poster.post_issue_comment(self.token, 'pfateev', 'test', 1, 'cli/test.md')
        # perform add
        updatedIssue = self.repo.get_issue(number=self.issue_number)
        newCount = updatedIssue.comments
        assert newCount - currCount == 1
        # check to make sure comment was added
    
    # def test_bad_filename():
    #     pass

    # def test_false_issue():
    #     pass
    
    # def test_non_md_file():
    #     pass

if __name__ == '__main__':
    unittest.main()