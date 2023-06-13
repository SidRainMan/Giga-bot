from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Service with the path to ChromeDriver executable
ser_obj = Service("C:/Users/siddh/PycharmProjects/SeleniumProj/chromedriver.exe")

# Set up the WebDriver
driver = webdriver.Chrome(service=ser_obj)

# Variables to store the buy and sell button identifiers
buy_button_id = ''
sell_button_id = ''


# Function to trigger buy order
def trigger_buy_order():
    if buy_button_id:
        buy_button = driver.find_element(By.ID, buy_button_id)
        buy_button.click()
    else:
        print("Buy button ID not set!")


# Function to trigger sell order
def trigger_sell_order():
    if sell_button_id:
        sell_button = driver.find_element(By.ID, sell_button_id)
        sell_button.click()
    else:
        print("Sell button ID not set!")


# Example usage
trigger_buy_order()  # Trigger a buy order
# or
trigger_sell_order()  # Trigger a sell order

# Close the browser window
driver.quit()
