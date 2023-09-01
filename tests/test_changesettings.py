"""
These tests cover DuckDuckGo settings.
"""
from pages.result import DuckDuckGoResultPage


def test_change_search_settings(browser):
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    result_page.load()

    # User clicks on settings button
    result_page.settings_button()

    # User clicks on all settings button
    result_page.all_settings_button()

    # Checking page title for Settings
    assert "Settings" in result_page.title()
