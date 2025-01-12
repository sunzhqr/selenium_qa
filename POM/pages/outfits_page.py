from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class OutfitsPage(BasePage):
    OUTFITS_MENU = (By.XPATH, "//a[@href='/outfits']")
    ADD_BUTTON = (By.XPATH, "//button[.//span[text()='Добавить']]")
    TECHNICAL_MAINTENANCE_OPTION = (By.XPATH, "//tr[.//td[text()='Техническое обслуживание']]")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component']")
    EQUIPMENT_FIELD = (By.XPATH, "//input[@placeholder='Оборудование наряда']")
    EXECUTOR_DROPDOWN = (By.XPATH, "//div[@id='pv_id_30']//div[contains(@class, 'p-dropdown-trigger')]")
    EXECUTOR_OPTION = (By.XPATH, "//li[@aria-label='Sanzhar']")
    FINAL_ADD_BUTTON = (By.XPATH, "//button[.//span[text()='Добавить']]")

    def navigate_to_outfits(self):
        self.click(self.OUTFITS_MENU)

    def add_outfit(self, description, equipment, executor):
        self.click(self.ADD_BUTTON)
        self.click(self.TECHNICAL_MAINTENANCE_OPTION)
        self.enter_text(self.DESCRIPTION_FIELD, description)
        self.enter_text(self.EQUIPMENT_FIELD, equipment)
        self.click(self.EXECUTOR_DROPDOWN)
        self.click(self.EXECUTOR_OPTION)
        self.click(self.FINAL_ADD_BUTTON)
