#!/usr/bin/python3
"""Displays the body of a response."""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
  req = urllib.request.Request(sys.argv[1])

  try:
      with urllib.request.urlopen(req) as response:
          print(response.read().decode("utf-8"))
  except urllib.error.HTTPError as e:
      print(f'Error code: {e.code}')
