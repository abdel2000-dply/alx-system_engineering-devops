import requests

# Define API key (replace with your own)
API_KEY = "AIzaSyCvF51voi8E3lwf44fOIkQ75VwWJXkzuVk"

# Category and author to filter by
category = "Fantasy"
author = "Isaac Asimov"
title_keyword = "Art"

# Build search query
query = f"q={category}&inauthor:{author}+intitle:{title_keyword}&key={API_KEY}"

# Send API request
url = f"https://www.googleapis.com/books/v1/volumes?" + query
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Extract book information
    books = data["items"]

    # Print titles of matching books
    for book in books:
        title = book["volumeInfo"]["title"]
        print(title)
else:
    print(f"Error: {response.status_code}")
