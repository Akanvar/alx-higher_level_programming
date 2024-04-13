#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status.
Usage: ./4-hbtn_status.py
"""
import requests

if __name__ == "__main__":
  req = requests.get('https://alx-intranet.hbtn.io/status')
  print("Body response:")
  print(f'\t- type: {type(req.text)}')
  print(f'\t- content: {req.text}')
