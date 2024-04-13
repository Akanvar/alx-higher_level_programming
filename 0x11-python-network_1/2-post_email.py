#!/usr/bin/python3
"""Sends a POST request with email parameter and displays response.
Usage: ./2-post_email.py email
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
  url = sys.argv[1]
  email = sys.argv[2]

  value = {"email": email}
  data = urllib.parse.urlencode(value)
  data = data.encode('ascii')
  req = urllib.request.Request(url, data)
  with urllib.request.urlopen(req) as response:
      print(response.read().decode("utf-8"))
