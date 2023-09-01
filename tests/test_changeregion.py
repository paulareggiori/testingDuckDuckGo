"""
These tests cover DuckDuckGo region change.
"""
from pages.result import DuckDuckGoResultPage
from pages.settings import DuckDuckGoSettingsPage


def test_change_search_region(browser):
    result_page = DuckDuckGoResultPage(browser)
    settings_page = DuckDuckGoSettingsPage(browser)

    # Given the DuckDuckGo home page is displayed
    result_page.load()

    # User clicks on settings button
    result_page.settings_button()

    # User clicks on all settings button
    result_page.all_settings_button()

    # User selection regions menu
    settings_page.region_menu()

    # User selection selects region
    settings_page.region_select()

    # User selection saves settings
    settings_page.save_button()

    # Assert that the new region is the expected value
    assert result_page.current_region() == "Brazil"
