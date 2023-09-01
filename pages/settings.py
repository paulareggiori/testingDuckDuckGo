"""
This module contains DuckDuckGoSettingsPage,
the page object for the DuckDuckGo settings page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoSettingsPage:
    REGION_OPTIONS = (By.ID, "setting_kl")
    REGION = (By.XPATH, "//option[@value='br-pt']")
    SAVE_BUTTON = (By.CLASS_NAME, "js-set-exit")


    def __init__(self, browser):
        self.browser = browser

    def region_menu(self):
        region_menu = self.browser.find_element(*self.REGION_OPTIONS)
        region_menu.click()

    def region_select(self):
        region_select = self.browser.find_element(*self.REGION)
        region_select.click()

    def save_button(self):
        save_button = self.browser.find_element(*self.SAVE_BUTTON)
        save_button.click()
