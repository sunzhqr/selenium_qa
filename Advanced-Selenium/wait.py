from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# •  Implicit Wait: Sets a global wait of 10 seconds to locate the search bar and execute a search for "laptops."
# •  Explicit Wait: Waits up to 15 seconds for the "Computers & Accessories" link to be clickable before clicking it.
# •  Fluent Wait: Checks every 2 seconds, up to 20 seconds, for the "HP 15 Laptop" product link to become clickable before clicking it.

def use_implicit_wait(driver):
    driver.implicitly_wait(10)
    try:
        print("Using Implicit Wait:")
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("laptops")
        search_box.submit()
        print("Search executed using implicit wait.")
    except Exception as e:
        print("Implicit wait failed:", e)

def use_explicit_wait(driver):
    try:
        print("\nUsing Explicit Wait:")
        wait = WebDriverWait(driver, 15)
        category_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Computers & Accessories")))
        category_link.click()
        print("Category clicked using explicit wait.")
    except Exception as e:
        print("Explicit wait failed:", e)

def use_fluent_wait(driver):
    try:
        print("\nUsing Fluent Wait:")
        fluent_wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[Exception])
        product_link = fluent_wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='HP 15 Laptop']")))
        product_link.click()
        print("Product link clicked using fluent wait.")
    except Exception as e:
        print("Fluent wait failed:", e)

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/")

    try:
        use_implicit_wait(driver)
        use_explicit_wait(driver)
        use_fluent_wait(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
