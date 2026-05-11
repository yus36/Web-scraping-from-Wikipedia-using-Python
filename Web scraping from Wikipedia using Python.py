import requests
from bs4 import BeautifulSoup

# 1. Provide the URL of the Wikipedia page you want to scrape
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# 2. Send an HTTP request to the URL
# We add a 'User-Agent' to tell Wikipedia we are a browser, not a 'suspicious bot'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# 3. Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'lxml')

# 4. Extract the main Title (the <h1> tag)
title = soup.find('h1', id="firstHeading").text
print(f"TITLE: {title}")
print("-" * 30)

# 5. Extract all paragraphs inside the main content area
# On Wikipedia, the main body is usually inside a div with id="bodyContent"
content = soup.find(id="bodyContent")
paragraphs = content.find_all('p')

# 6. Loop through paragraphs, clean them, and print
for p in paragraphs:
    text = p.text.strip()
    
    # Simple logic to ignore empty paragraphs
    if len(text) > 0:
        # Wikipedia cleaning: Remove citation brackets like [1], [22], etc.
        # This is a key requirement of the GeeksforGeeks exercise
        import re
        clean_text = re.sub(r'\[.*?\]', '', text)
        
        print(clean_text)
        print() # Add a space between paragraphs
