"""
These tests cover DuckDuckGo settings.
"""
import time
from pages.result import DuckDuckGoResultPage


def test_infinite_scroll(browser):
    result_page = DuckDuckGoResultPage(browser)
    total_before = 0
    total_after = 0

    # Given the DuckDuckGo home page is displayed
    result_page.load()

    # User clicks on settings button
    result_page.settings_button()

    # User enables infinite scroll
    result_page.infinite_scroll()

    #  Search result counter before scrolling down
    phrase = result_page.search_input_value()
    titles = result_page.result_link_titles()
    for t in titles:
        if phrase.lower() in t.lower():
            total_before += 1

    # Scroll down
    result_page.scroll_down()
    time.sleep(1)

    # Search result counter after scroll
    titles = result_page.result_link_titles()
    for t in titles:
        if phrase.lower() in t.lower():
            total_after += 1
    assert total_after > total_before
