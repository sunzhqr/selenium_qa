from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

test_results = []

def log_test_result(test_name, status, details=""):
    """Logs the test result."""
    test_results.append({
        "test_name": test_name,
        "status": status,
        "details": details
    })

try:
    driver.get("https://www.apple.com/")
    time.sleep(3)
    if "Apple" in driver.title:
        log_test_result("Navigate to Apple.com", "Passed")
    else:
        log_test_result("Navigate to Apple.com", "Failed", "Title mismatch")

    try:
        mac_link = driver.find_element(By.XPATH, "//a[contains(@href, '/mac/')]")
        mac_link.click()
        time.sleep(3)
        if "Mac" in driver.title:
            log_test_result("Navigate to Mac Section", "Passed")
        else:
            log_test_result("Navigate to Mac Section", "Failed", "Title mismatch")
    except Exception as e:
        log_test_result("Navigate to Mac Section", "Failed", str(e))

    try:
        search_icon = driver.find_element(By.CLASS_NAME, "ac-gn-search-icon")
        search_icon.click()
        time.sleep(2)
        search_box = driver.find_element(By.CLASS_NAME, "ac-gn-search-input")
        search_box.send_keys("iPhone")
        search_box.submit()
        time.sleep(3)
        if "iPhone" in driver.page_source:
            log_test_result("Search for 'iPhone'", "Passed")
        else:
            log_test_result("Search for 'iPhone'", "Failed", "Search results did not load as expected")
    except Exception as e:
        log_test_result("Search for 'iPhone'", "Failed", str(e))

    try:
        ipad_link = driver.find_element(By.XPATH, "//a[contains(@href, '/ipad/')]")
        ipad_link.click()
        time.sleep(3)
        if "iPad" in driver.title:
            log_test_result("Navigate to iPad Section", "Passed")
        else:
            log_test_result("Navigate to iPad Section", "Failed", "Title mismatch")
    except Exception as e:
        log_test_result("Navigate to iPad Section", "Failed", str(e))

finally:
    driver.quit()

    print("\nTest Report:")
    print("=" * 40)
    total_tests = len(test_results)
    passed_tests = len([t for t in test_results if t['status'] == "Passed"])
    failed_tests = len([t for t in test_results if t['status'] == "Failed"])

    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}\n")

    for result in test_results:
        print(f"Test Name: {result['test_name']}")
        print(f"Status: {result['status']}")
        if result['details']:
            print(f"Details: {result['details']}")
        print("-" * 40)
