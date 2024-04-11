#!/bin/bash
# Sends a request to URl and only displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
