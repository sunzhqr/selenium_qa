from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def use_select_class(driver):
    try:
        print("Navigating to Apple Refurbished Products page...")
        driver.get("https://www.apple.com/shop/refurbished")

        print("Waiting for the sort dropdown menu to appear...")
        wait = WebDriverWait(driver, 15)
        dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "as-dimension-filter-type-price-asc")))

        dropdown = Select(dropdown_element)

        print("Selecting 'Lowest Price' by visible text...")
        dropdown.select_by_visible_text("Lowest Price")

        print("Selecting 'Highest Price' by value...")
        dropdown.select_by_value("price-desc")

        print("Selecting the second option by index...")
        dropdown.select_by_index(1)

    except Exception as e:
        print("An error occurred while using the Select class:", e)

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.apple.com/")

    try:
        use_select_class(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

