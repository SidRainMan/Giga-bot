import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:/Users/siddh/PycharmProjects/SeleniumProj/chromedriver.exe")

# Set up the WebDriver
driver = webdriver.Chrome(service=ser_obj)

class GUI:
    def __init__(self):
        self.driver = driver
        self.button_id = None

        self.root = tk.Tk()
        self.root.title("Button ID Retrieval")
        self.root.geometry("400x100")  # Set the window size to 400x100

        # Create button
        select_button = tk.Button(self.root, text="Select Button", command=self.select_button)

        # Create label
        self.button_id_label = tk.Label(self.root, text="Button ID:")

        # Pack button and label
        select_button.pack()
        self.button_id_label.pack()

        self.root.mainloop()

    def select_button(self):
        print("Select the button on the website...")
        self.driver.get("https://www.google.com/")  # Replace with your website URL

        # Register click event
        self.driver.execute_script(
            '''
            var buttons = document.getElementsByTagName("button");
            for (var i = 0; i < buttons.length; i++) {
                buttons[i].addEventListener("click", function(event) {
                    window.clickedButtonId = event.target.id;
                });
            }
            '''
        )

        # Wait for the button to be clicked
        self.driver.execute_script("while (!window.clickedButtonId) {}")
        self.button_id = self.driver.execute_script("window.clickedButtonId;")
        self.driver.execute_script("window.clickedButtonId = undefined;")

        if self.button_id:
            print("The element ID is:", self.button_id)
            self.button_id_label.configure(text="Button ID: " + str(self.button_id))
        else:
            print("No button ID found.")

# Set up the Selenium WebDriver
driver_path = "C:/Users/siddh/PycharmProjects/SeleniumProj/chromedriver.exe"  # Replace with your driver path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Create an instance of the GUI
gui = GUI()
gui.driver = driver
