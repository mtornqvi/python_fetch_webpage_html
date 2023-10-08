try:
    import requests
except ImportError:
    print('Please install the requests library using pip install requests')
    exit()
try:
    from bs4 import BeautifulSoup
except ImportError:
    print('Please install the BeautifulSoup library using pip install beautifulsoup4')
    exit()


# Send a GET request to the URL
url = 'https://www.s-kaupat.fi'
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Debugging : Open a file named 'debugging.html' in write mode
with open('debugging.html', 'w', encoding='utf-8') as file:
    # Use the prettify() method to format the HTML nicely
    pretty_html = soup.prettify()
    
    # Write the formatted HTML to the file
    file.write(pretty_html)

