# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:21:52 2023

@author: Sanika More
"""

import requests
import json

def get_repo_commits(username):
    # Get user's repositories
    repo_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repo_url)
    repos = json.loads(response.text)

    # Get number of commits for each repository
    repo_commits = {}
    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        response = requests.get(commits_url)
        commits = json.loads(response.text)
        repo_commits[repo_name] = len(commits)

    return repo_commits
username = "SANIKA1809"
repo_commits = get_repo_commits(username)
print(repo_commits)
