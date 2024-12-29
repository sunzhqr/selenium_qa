from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://admin.keep-lift.kz/auth/login")

    time.sleep(3)

    email_field = driver.find_element(By.ID, "email1")
    email_field.clear()
    email_field.send_keys("login_email")

    password_field = driver.find_element(By.CSS_SELECTOR, "input.p-password-input")
    password_field.clear()
    password_field.send_keys("password")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.p-button")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/outfits']"))
    )

    outfits_menu = driver.find_element(By.XPATH, "//a[@href='/outfits']")
    outfits_menu.click()

    time.sleep(3)

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Добавить']]"))
    )
    add_button.click()

    technical_maintenance_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//tr[.//td[text()='Техническое обслуживание']]"))
    )
    technical_maintenance_option.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-dialog-content"))
    )

    description_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component']"))
    )
    description_field.clear()
    description_field.send_keys("Shynar apa")

    equipment_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Оборудование наряда']"))
    )
    equipment_field.clear()
    equipment_field.send_keys("kamal4 eq")

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element((By.CLASS_NAME, "p-dialog-mask"))
    )

    executor_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='pv_id_30']//div[contains(@class, 'p-dropdown-trigger')]"))
    )
    executor_dropdown.click()

    executor_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Sanzhar']"))
    )
    executor_option.click()

    add_button_final = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Добавить']]"))
    )
    add_button_final.click()

    time.sleep(3)

    print("Новый наряд успешно создан!")

finally:
    driver.quit()
