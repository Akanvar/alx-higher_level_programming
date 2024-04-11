#!/bin/bash
# Sends a delete request to URL passed and displays body of response
curl -X DELETE -s "$1"
