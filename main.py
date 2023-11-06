
from zillow_data import ZillowData
from form_data import FormData

def main():
    # Create the object of ZillowData class
    zillow = ZillowData()
    
    # get the price, address and link lists
    price_list = zillow.get_listing_prices()
    address_list = zillow.get_listing_addresses()
    link_list = zillow.get_listing_links()

    # Create the object of the FormData class
    form = FormData()    
    # open the google form
    form.get_form()  

    # Fill the data on the form
    for n in range(len(price_list)):
        form.fill_addresses(address_list[n])
        form.fill_prices(price_list[n])
        form.fill_links(link_list[n])
        form.submit_response()
        form.submit_another_response()
    
    form.close_form()    


if __name__ == "__main__":
    main()





