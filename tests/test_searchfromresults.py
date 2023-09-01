"""
These tests cover DuckDuckGo searches starting from a search page.
"""
import pytest as pytest
from pages.result import DuckDuckGoResultPage
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("phrase", ["holanda", "Brasil"])
def test_from_results_page(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    result_page.load()

    # Erase current search box value
    length = result_page.search_input_value()
    for i in length:
        result_page.search_input(Keys.BACKSPACE)

    # Add new search box value
    result_page.search_input(phrase)

    # User clicks on search button
    result_page.search_button()

    # And the search result query is "phrase"
    assert phrase in result_page.search_input_value()

    # And the search result links of the new instance pertain to "phrase"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # Then the search result title contains "phrase"
    assert phrase in result_page.title()
