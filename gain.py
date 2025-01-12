from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_search_functionality():
    print("Begin Search")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Selenium WebDriver" in driver.title
    driver.quit()
    print("Searched")


def test_login_logout():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Login
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@id='submit']")

    username.send_keys("student")
    password.send_keys("Password123")
    login_button.click()
    time.sleep(2)

    assert "Logged In Successfully" in driver.page_source

    # Logout
    logout_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
    logout_button.click()
    time.sleep(2)

    assert "Login" in driver.page_source
    driver.quit()


def test_flight_booking():
    driver = webdriver.Chrome()
    driver.get("https://example-flight-booking.com")
    driver.find_element(By.CSS_SELECTOR, "#departure").send_keys("New York")
    driver.find_element(By.CSS_SELECTOR, "#destination").send_keys("Los Angeles")
    driver.find_element(By.XPATH, "//input[@id='departure-date']").click()
    driver.find_element(By.XPATH, "//td[text()='15']").click()
    driver.find_element(By.CSS_SELECTOR, "#search-flights").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Book Now']").click()
    time.sleep(3)
    assert "Your Booking" in driver.page_source, "Booking title checkpoint failed"


def main():
    test_search_functionality()
    test_login_logout()


if __name__ == "__main__":
    main()