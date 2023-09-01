"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:
    URL = "https://www.duckduckgo.com"
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.searchbox_searchButton__F5Bwq")
    SUGGESTIONS = (By.CLASS_NAME, "searchbox_suggestion__csrUQ")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

    def search_button(self):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def suggestion_elements(self):
        suggestions_el = self.browser.find_elements(*self.SUGGESTIONS)
        return suggestions_el

    def suggestions_text(self):
        suggestions = []
        suggestion_el = self.suggestion_elements()
        for el in suggestion_el:
            suggestions.append(el.text)
        return suggestions
