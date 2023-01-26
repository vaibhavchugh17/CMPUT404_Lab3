#!/usr/bin/env python3
import os
import json

env_vars = dict(os.environ)

print("Content-Type: application/json")
print()
print(json.dumps(env_vars)) #We are not sending html, rather JSON. To send HTML we would need to change the content type in the first print statement