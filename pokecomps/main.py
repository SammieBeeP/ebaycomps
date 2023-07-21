import requests #with pointers and forwarders 
from bs4 import BeautifulSoup

def scrape_reselling_sites():
    # Define the URLs of major reselling sites
    site_urls = ['https://www.ebay.com', 'https://example2.com', 'https://example3.com']
    
    card_data = []
    
    for url in site_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant card information from the webpage
        card_name = soup.select('.card-name')[0].text
        card_condition = soup.select('.card-condition')[0].text
        card_price = soup.select('.card-price')[0].text
        
        card_data.append({
            'name': card_name,
            'condition': card_condition,
            'price': card_price
        })
    
    return card_data

