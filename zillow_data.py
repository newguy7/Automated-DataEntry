from bs4 import BeautifulSoup
import requests
import re


class ZillowData:

    listing_prices = []
    listing_addresses = []
    listing_links = []

    def __init__(self):
        self.response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
        self.zillow_web_page = self.response.text

        self.soup = BeautifulSoup(self.zillow_web_page, "html.parser")
        

    def get_listing_prices(self):
        # Find all span elements within the page
        all_price_elements = self.soup.select(".PropertyCardWrapper span") 
        for price in all_price_elements:
            if "$" in price.text:
                price = price.get_text().replace("/mo", "").split("+")[0]
                self.listing_prices.append(price)
        
        return self.listing_prices

    def get_listing_addresses(self):
                
        all_listing_addresses = self.soup.find_all('address', {'data-test': 'property-card-addr'})

        for address in all_listing_addresses:
            address = address.get_text().replace(" | ", " ").strip()            
            self.listing_addresses.append(address)
        return self.listing_addresses


    def get_listing_links(self):
        all_listing_links = self.soup.find_all('a', {'class': 'StyledPropertyCardDataArea-anchor','data-test': 'property-card-link'})
        for links in all_listing_links:
            listing_link = links.get('href')
            self.listing_links.append(listing_link)
        return self.listing_links

