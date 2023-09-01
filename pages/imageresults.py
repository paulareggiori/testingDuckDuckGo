"""
This module contains DuckDuckGoImageResultsPage,
the page object for the DuckDuckGo image result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoImageResultsPage:
	RESULT_LINKS = (By.CLASS_NAME, 'tile--img__sub')

	def __init__(self, browser):
		self.browser = browser

	def result_links(self):
		links = self.browser.find_elements(*self.RESULT_LINKS)
		return links

	def result_link_titles(self):
		links = self.result_links()
		titles = [link.text for link in links]
		return titles

	def title(self):
		return self.browser.title

	def scroll_down(self):
		self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


