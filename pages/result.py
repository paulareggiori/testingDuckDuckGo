"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    URL = "https://www.duckduckgo.com/?q=panda&ia=web"
    RESULT_LINKS = (By.CLASS_NAME, 'wLL07_0Xnd1QZpzpfR4W')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SEARCH_BUTTON = (By.ID, "search_button")
    MORE_RESULTS = (By.ID, "more-results")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

    def result_links(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        return links

    def result_link_titles(self):
        links = self.result_links()
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def title(self):
        return self.browser.title

    def search_button(self):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def more_results(self):
        more_results = self.browser.find_element(*self.MORE_RESULTS)
        more_results.click()
