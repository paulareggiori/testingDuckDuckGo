"""
These tests cover DuckDuckGo video searches.
"""
import time
import pytest as pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from pages.videoresults import DuckDuckGoVideoResultsPage
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("phrase", ["panda", "bear"])
def test_duckduckgo_video_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    videos_page = DuckDuckGoVideoResultsPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "phrase"
    search_page.search_input(phrase)
    search_page.search_input(Keys.RETURN)

    # And the search result query is "phrase"
    assert phrase in result_page.search_input_value()
    time.sleep(1)

    # Click on videos
    result_page.videos()

    # Assert the search result links pertain to "phrase"
    titles = videos_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # Then the search result title contains "phrase"
    assert phrase in videos_page.title()
