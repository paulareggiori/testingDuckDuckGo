"""
These tests cover DuckDuckGo searching using a suggestion.
"""

import pytest as pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize("phrase", ["pas", "tant"])
def test_search_by_suggestion(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "phrase"
    search_page.search_input(phrase)

    # Get the suggestion text clicked
    suggestion_text = search_page.suggestions_text()[0]

    # Click on first suggestion
    search_page.suggestion_elements()[0].click()

    # Assert the "phrase" is in suggestion text
    assert phrase in suggestion_text

    # And the search result links pertain to suggestion text
    titles = result_page.result_link_titles()
    matches = [t for t in titles if suggestion_text.lower() in t.lower()]
    assert len(matches) > 0

    # Then the search result title contains suggestion text
    assert suggestion_text in result_page.title()