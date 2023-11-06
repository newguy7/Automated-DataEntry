import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FormData:

    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_argument("start-maximized")
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.gmail_url = "https://mail.google.com/"
        
        self.form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfyybevxj7JghtmuDLMkYBXkfr9mmjJPXOwzhEpBAd-T4m4aQ/viewform?usp=sf_link"

    def login_to_gmail(self, email, password):
        self.driver.get(self.gmail_url)
        email_field = self.driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username"]')
        email_field.send_keys(email)
        email_field.send_keys(Keys.ENTER)
        time.sleep(2)  # Wait for the next page to load (you can adjust the wait time)

        password_field = self.driver.find_element(By.CSS_SELECTOR,'input[name="Passwd"]')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

    def get_form(self):    
        self.driver.get(self.form_url)


    # Find the question1
    def fill_addresses(self,address):
        address_input = self.driver.find_element(By.CSS_SELECTOR,'input[aria-labelledby="i1"]')
        address_input.click()
        address_input.send_keys(address)

    # Find the question2
    def fill_prices(self,price):
        price_input = self.driver.find_element(By.CSS_SELECTOR,'input[aria-labelledby="i5"]')
        price_input.click()
        price_input.send_keys(price)


    # Find the question3
    def fill_links(self,link):
        link_input = self.driver.find_element(By.CSS_SELECTOR,'input[aria-labelledby="i9"]')
        link_input.click()
        link_input.send_keys(link)
        time.sleep(2)

    # Submit the form
    def submit_response(self):
        submit_button = self.driver.find_element(By.XPATH,'//span[contains(text(), "Submit")]')
        submit_button.click()

    def submit_another_response(self):
        anchor_element = self.driver.find_element(By.LINK_TEXT, "Submit another response")

        # Interact with the anchor element (click on it)
        anchor_element.click()

    def close_form(self):
        self.driver.quit()

    def save_responses(self):
        responses_link = self.driver.find_element(By.LINK_TEXT, "Responses")
        responses_link.click()
        time.sleep(2)
        link_to_sheet = self.driver.find_element(By.XPATH,'//span[contains(text(), "Link to Sheets")]')
        link_to_sheet.click()
        time.sleep(2)