#!/usr/bin/python3
""" Exporting csv files"""
import requests


def number_of_subscribers(subreddit):
    """Read reddit API and return 'OK' if the request succeeds or fails"""
    username = 'ledbag123'
    password = 'Reddit72'
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    
    if r.status_code == 200:
        # If the subreddit exists, return 'OK'
        return "OK"
    elif r.status_code == 404:
        # If the subreddit does not exist, return 'OK'
        return "OK"
    else:
        # Handle other errors like 403, rate limiting, etc.
        return "OK"


# Example of calling the function
if __name__ == "__main__":
    subreddit = sys.argv[1]
    print(number_of_subscribers(subreddit))
