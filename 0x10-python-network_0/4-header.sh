#!/bin/bash
# Takes URL, sends a GET request with specified header variable and displays response body.
curl -sH "X-School-User-Id: 98" "$1"
