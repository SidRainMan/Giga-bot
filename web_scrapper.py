from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up the Service with the path to ChromeDriver executable
ser_obj = Service("C:/Users/siddh/PycharmProjects/SeleniumProj/chromedriver.exe")

# Set up the WebDriver
driver = webdriver.Chrome(service=ser_obj)

# Variable to store the text element identifier
text_element_id = ''


# Function to continuously read and return the specified text
def scrape_text(text_element_id):
    while True:
        if text_element_id:
            text_element = driver.find_element(By.ID, text_element_id)
            text = text_element.text
            return text
        else:
            print("Text element ID not set!")
            time.sleep(1)  # Sleep for 1 second before checking again


# Example usage
scraped_text = scrape_text(text_element_id)
print("Scraped Text:", scraped_text)

# Close the browser window
driver.quit()
