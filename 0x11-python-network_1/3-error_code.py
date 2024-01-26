#!/usr/bin/python3
"""
Manage urllib.error.HTTPError exceptions and print: Error code:
"""
if __name__ == "__main__":
    import sys
    import urllib.error
    import urllib.request


    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
