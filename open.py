from selenium import webdriver
import time

# Initialize a web driver (you need to have the appropriate driver executable installed)
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Run JavaScript code to change background color
javascript_code = """
    document.body.style.backgroundColor = 'blue';
"""

# Execute the JavaScript code
driver.execute_script(javascript_code)

# Wait for a few seconds before closing the browser
time.sleep(100000)  # Adjust the number of seconds as needed

# Close the browser window
driver.quit()