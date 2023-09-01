"""
These tests cover DuckDuckGo suggestions.
"""

import pytest as pytest
from pages.search import DuckDuckGoSearchPage
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("phrase", ["pas", "con"])
def test_match_suggestions(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "phrase"
    search_page.search_input(phrase)

    # Assert that the suggestions list contains the "phrase"
    suggestions = search_page.suggestions_text()
    matches = [t for t in suggestions if phrase in t]
    assert len(matches) > 0
