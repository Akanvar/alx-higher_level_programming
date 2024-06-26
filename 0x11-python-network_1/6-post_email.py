#!/usr/bin/python3
"""Sends a POST request with an email variable and displays response
Usage: ./6-post_email.py email
"""
import requests
import sys

if __name__ == "__main__":
  url = sys.argv[1]
  email = sys.argv[2]

  r = requests.post(url, data={'email': email})
  print(r.text)
