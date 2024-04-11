#!/bin/bash
#  Takes in a URL, sends a request, displays the size of response body
curl -s "$1" | wc -c
