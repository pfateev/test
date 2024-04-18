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
    auth = Auth.Token(os.getenv('GITHUB_TOKEN'))
    g = Github(auth=auth)
    repo = g.get_repo("pfateev/test")
    issue_number = 1

    def test_add_comment(self):
        # get number of current comments
        issue = self.repo.get_issue(number=self.issue_number)
        # perform add
        # check to make sure comment was added
        pass
    
    def test_bad_filename():
        pass

    def test_false_issue():
        pass
    
    def test_non_md_file():
        pass