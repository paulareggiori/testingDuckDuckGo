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
    SETTINGS = (By.CLASS_NAME, "dropdown--settings")
    ALL_SETTINGS = (By.CLASS_NAME, "settings-dropdown--button")
    SCROLL = (By.XPATH, "//label[@for='setting_kav']")
    CURRENT_REGION = (By.XPATH, "//a[@class ='dropdown__button dropdown__button js-dropdown-button ']")
    IMAGES = (By.CLASS_NAME, "js-zci-link--images")
    VIDEOS = (By.XPATH, "//a[@data-zci-link='videos']")
    NEWS = (By.CLASS_NAME, "js-zci-link--news")

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

    def more_results_is_displayed(self):
        return self.browser.find_element(*self.MORE_RESULTS).is_displayed()

    def settings_button(self):
        settings_button = self.browser.find_element(*self.SETTINGS)
        settings_button.click()

    def all_settings_button(self):
        all_settings_button = self.browser.find_element(*self.ALL_SETTINGS)
        all_settings_button.click()

    def infinite_scroll(self):
        infinite_scroll = self.browser.find_element(*self.SCROLL)
        infinite_scroll.click()

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def current_region(self):
        current_region = self.browser.find_element(*self.CURRENT_REGION).get_attribute("text")
        return current_region

    def images(self):
        images = self.browser.find_element(*self.IMAGES)
        images.click()

    def videos(self):
        videos = self.browser.find_element(*self.VIDEOS)
        videos.click()

    def news(self):
        news = self.browser.find_element(*self.NEWS)
        news.click()
