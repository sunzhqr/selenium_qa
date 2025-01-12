import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.outfits_page import OutfitsPage

class TestOutfitCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin.keep-lift.kz/auth/login")
        self.driver.maximize_window()

    def test_create_outfit(self):
        # Login
        login_page = LoginPage(self.driver)
        login_page.login("login_email", "password")

        # Navigate to outfits and add a new outfit
        outfits_page = OutfitsPage(self.driver)
        outfits_page.navigate_to_outfits()
        outfits_page.add_outfit("Test Sanzhar", "kamal4 eq", "Sanzhar")

        success_message_locator = (By.XPATH, "//div[contains(text(), 'Наряд успешно добавлен')]")
        success_message = outfits_page.wait_for_element(success_message_locator, timeout=10)
        self.assertIsNotNone(success_message, "Success message not found, outfit creation may have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
