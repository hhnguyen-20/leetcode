import requests
import os
import sys

username = os.getenv('LEETCODE_USERNAME')
password = os.getenv('LEETCODE_PASSWORD')

if not username or not password:
    print("Missing username or password secrets.")
    sys.exit(1)

URL = 'https://leetcode.com/accounts/login/'

# Browser-like headers to avoid bot detection
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://leetcode.com/',
    'Connection': 'keep-alive',
}

session = requests.Session()

# Get initial CSRF token with headers
response = session.get(URL, headers=headers)
csrf_token = session.cookies.get('csrftoken', '')

if not csrf_token:
    print("Failed to get initial CSRF token.")
    sys.exit(1)

# Prepare login data
login_data = {
    'login': username,
    'password': password,
    'csrfmiddlewaretoken': csrf_token,
    'next': '/problems'  # Optional, but helps with redirect
}

# Add Referer and update headers for POST
post_headers = {**headers, 'Referer': URL}

# Perform login
response = session.post(URL, data=login_data, headers=post_headers)

if response.status_code != 200 or 'csrftoken' not in session.cookies or 'LEETCODE_SESSION' not in session.cookies:
    print("Login failed. Check credentials or if LeetCode changed their login process.")
    sys.exit(1)

# Fresh tokens
new_csrf = session.cookies['csrftoken']
new_session = session.cookies['LEETCODE_SESSION']

# Set them as GitHub env vars for the next steps
with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f"LEETCODE_CSRF_TOKEN={new_csrf}\n")
    env_file.write(f"LEETCODE_SESSION={new_session}\n")
