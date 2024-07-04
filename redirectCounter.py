import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input URL, count, and position
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve the sequence of names
for i in range(count):
    print(f"Retrieving: {url}")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position - 1].get('href', None)

# Print the last URL
print(f"Retrieving: {url}")