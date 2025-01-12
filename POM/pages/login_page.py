from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email1")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.p-password-input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.p-button")

    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
