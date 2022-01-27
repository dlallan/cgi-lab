#!/usr/bin/env python3
import os
import json

# print('Content-Type: text/plain')
# print()
# print(os.environ)

# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ.items())))

# print('Content-Type: text/plain')
# print()
# print(os.getenv('QUERY_STRING'))

print('Content-Type: text/plain')
print()
print(os.getenv('HTTP_USER_AGENT'))