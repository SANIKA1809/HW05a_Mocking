import unittest
from unittest.mock import patch
import Repocommit

class RepoCommitUsers(unittest.TestCase):
    @patch('Repocommit.get_repo_commits')
    def test_get_repo_commits(self, mock_get_repo_commits):
        username = "SANIKA1809"
        mock_get_repo_commits.return_value = {'repo1': 10, 'repo2': 5}
        repo_commits = Repocommit.get_repo_commits(username)
        assert isinstance(repo_commits, dict)
        assert len(repo_commits) > 0
        assert all(isinstance(key, str) for key in repo_commits.keys())
        assert all(isinstance(value, int) for value in repo_commits.values())
        mock_get_repo_commits.assert_called_once_with(username)

if __name__ == '__main__':
    unittest.main(exit=False)
