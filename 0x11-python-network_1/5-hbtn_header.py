#!/usr/bin/python3
"""Uses packages requests and sys"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
