"""
These tests cover opening a DuckDuckGo search result.
"""

import pytest as pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("phrase", ["panda", "python"])
def test_click_on_result(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user types "phrase"
    search_page.search_input(phrase)

    # When the user clicks on search button
    search_page.search_button()

    # And the search result query is "phrase"
    assert phrase in result_page.search_input_value()

    # And the search result links pertain to "phrase"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # Click on first link
    result_page.result_links()[0].click()

    # Then the clicked search result title contains "phrase"
    assert phrase in result_page.title().lower()

