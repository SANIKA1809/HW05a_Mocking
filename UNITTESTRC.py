from unittest.mock import MagicMock
import Repocommit
import json

def test_get_repo_commits():
    response_mock = MagicMock()
    response_mock.json.return_value = [{'commit': {'committer': {'email': 'test@test.com', 'name': 'Test User'}, 'message': 'test commit message', 'url': 'https://github.com/SANIKA1809/test-repo/commit/12345'}}, {'commit': {'committer': {'email': 'test@test.com', 'name': 'Test User'}, 'message': 'another test commit message', 'url': 'https://github.com/SANIKA1809/test-repo/commit/67890'}}]
    Repocommit.requests.get = MagicMock(return_value=response_mock)

    username = "SANIKA1809"
    repo_commits = {}

    try:
        response = Repocommit.get_repo_commits(username)
        for commit in response:
            repo_commits[commit['commit']['url']] = len(commit['commit']['message'])
    except (json.JSONDecodeError, TypeError) as e:
        assert False, f"Failed to parse JSON response: {e}"
    
    assert isinstance(repo_commits, dict)
    assert len(repo_commits) == 2
    assert all(isinstance(key, str) for key in repo_commits.keys())
    assert all(isinstance(value, int) for value in repo_commits.values())
