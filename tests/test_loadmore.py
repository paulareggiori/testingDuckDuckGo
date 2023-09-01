"""
These tests cover loading more results from a DuckDuckGo search.
"""

import pytest as pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("phrase", ["fox", "maria bonita"])
def test_load_more_items(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    total_before = 0
    total_after = 0

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "phrase"
    search_page.search_input(phrase)
    search_page.search_input(Keys.RETURN)

    # And the search result query is "phrase"
    assert phrase in result_page.search_input_value()

    #  Search result counter before load more
    titles = result_page.result_link_titles()
    for t in titles:
        if phrase.lower() in t.lower():
            total_before += 1

    # Click on More Results
    result_page.more_results()

    # Search result counter after load more
    titles = result_page.result_link_titles()
    for t in titles:
        if phrase.lower() in t.lower():
            total_after += 1
    assert total_after > total_before
