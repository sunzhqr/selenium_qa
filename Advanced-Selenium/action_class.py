from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# •  Navigates to Google: Opens the Google homepage.
# •  Search Box Interaction: Locates and interacts with the search input field.
# •  Search Query Execution: Types "Selenium WebDriver" and submits the search.
# •  Scroll Actions: Demonstrates scrolling down and up on the search results page using PAGE_DOWN and PAGE_UP keys.


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    time.sleep(3)

    search_box = driver.find_element(By.NAME, "q")
    actions = ActionChains(driver)

    actions.move_to_element(search_box).perform()
    time.sleep(1)
    search_box.click()
    time.sleep(1)

    search_box.send_keys("Selenium WebDriver")
    time.sleep(2)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(5)

    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)

    actions.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)

finally:
    driver.quit()

