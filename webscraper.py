import requests
from bs4 import BeautifulSoup

try:
    # Make an HTTP request to the website
    response = requests.get('https://www.example.com') # Enter the website you want to get all links from
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print non-image links with their URLs
    links = soup.find_all('a', href=True)
    for link in links:
        link_text = link.get_text().strip()
        link_url = link['href'].strip()

        # Check if the link is associated with an image (adjust as needed)
        if not link.find('img'):
            print(f"Link: {link_text} ({link_url})")

except requests.exceptions.RequestException as e:
    print("Error during HTTP request:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
