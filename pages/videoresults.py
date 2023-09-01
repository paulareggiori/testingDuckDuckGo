"""
This module contains DuckDuckGoVideoResultsPage,
the page object for the DuckDuckGo video result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoVideoResultsPage:
	RESULT_VIDEOS = (By.XPATH, "//h6[@class='tile__title  tile__title--2']")

	def __init__(self, browser):
		self.browser = browser

	def results(self):
		links = self.browser.find_elements(*self.RESULT_VIDEOS)
		return links

	def result_link_titles(self):
		links = self.results()
		titles = [link.text for link in links]
		return titles

	def title(self):
		return self.browser.title

	def scroll_down(self):
		self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


