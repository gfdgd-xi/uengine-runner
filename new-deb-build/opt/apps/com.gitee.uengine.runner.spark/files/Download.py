#!/usr/bin/env python3
import sys
import base64
import requests
print(requests.get(base64.b64decode("aHR0cDovLzEyMC4yNS4xNTMuMTQ0L3VlbmdpbmUtcnVubmVyL0luc3RhbGwucGhwP1ZlcnNpb249").decode("utf-8") + sys.argv[1]).text)