#!/usr/bin/python3
"""Displays the body of response
Usage: ./7-error_code.py email
Prints Error code if > 400
"""
import sys
import requests

if __name__ == "__main__":
  r = requests.get(sys.argv[1])
  if r.status_code >= 400:
      print(f'Error code: {r.status_code}')
