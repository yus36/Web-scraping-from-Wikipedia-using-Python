🕸️ Wikipedia Scraper with Python
A lightweight, efficient script to extract and clean article text from Wikipedia using Python.

🚀 The Core Stack
Requests: Fetches the raw HTML content from the web.

BeautifulSoup4: Parses the HTML into a searchable tree.

lxml: The high-speed engine used to read the data.

Re (Regex): Cleans the text by removing citation brackets (e.g., [1]).

🛠️ Requirements & Installation
Ensure you have Python installed, then run:

Bash
pip install requests beautifulsoup4 lxml
📝 The Workflow
1. The "Fetch" (Requests)
We send a request to the URL. Note: Using a User-Agent header prevents Wikipedia from identifying the script as a basic bot and potentially blocking it.

2. The "Target" (HTML IDs)
Instead of scraping the entire page, we target the main content container.

Main Title: Located in <h1> with id="firstHeading".

Main Body: Located inside <div> with id="bodyContent".

3. The "Filter" (Finding Tags)
We loop through all <p> (paragraph) tags inside the body container. This ignores sidebars, navigation links, and footers.

4. The "Scrub" (Cleaning)
Wikipedia is full of citation tags. We use a Regular Expression (\[.*?\]) to find anything inside square brackets and delete it, leaving only clean text.

💻 Sample Code Snippet
Python
import requests, re
from bs4 import BeautifulSoup

# Setup
res = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(res.text, 'lxml')

# Action: Get title and paragraphs
title = soup.find('h1').text
body = soup.find(id="bodyContent")

for p in body.find_all('p'):
    # Scrub [1], [2], etc.
    clean_text = re.sub(r'\[.*?\]', '', p.text)
    print(clean_text)
