#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
"""
import sys
import requests

if __name__ == "__main__":
  username = sys.argv[1]
  token = sys.argv[2]

  headers = {
          'X-GitHub-Api-Version': '2022-11-28',
          'Authorization': f'Bearer {token}',
          'Accept': 'application/vnd.github+json'
          }

  r = requests.get('https://api.github.com/user', headers=headers)
  print(r.json().get("id"))

