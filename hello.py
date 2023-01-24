#!/usr/bin/ python3
# Run it as a python executable

import os
import json

print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ))) #We are not sending html, rather JSON