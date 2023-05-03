import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://www.amazon.in/s?k=earbuds&i=electronics&sprefix=ear%2Celectronics%2C333&ref=nb_sb_ss_ts-doa-p_1_3'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the top 5 bestselling books in the category
books = soup.find_all('div', {'class': 'a-size-base-plus a-color-base a-text-normal'})

# Create an HTML table to display the book data
html = '<table>\n<tr><th>Title</th><th>Price</th><th>Rating</th></tr>\n'

# Loop through each book and extract the title, price, and rating
for book in books[:5]:
    title = book.find('div', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text.strip()
    price = book.find('span', {'class': 'a-offscreen'}).text.strip()
    rating = book.find('span', {'class': 'a-icon a-icon-star-small a-star-small-4 aok-align-bottom'}).text.strip()
    
    # Add a row to the HTML table for the book data
    html += f'<tr><td>{title}</td><td>{price}</td><td>{rating}</td></tr>\n'
    
# Close the HTML table
html += '</table>'

# Display the HTML table in the console
print(html)
