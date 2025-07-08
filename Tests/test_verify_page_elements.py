from playwright.sync_api import Page, expect
import logging
import pytest
from POM.webpagePOM import WebPage

@pytest.fixture
def pagePOM(page: Page, request):
    test_name = request.node.name
    pagePOM = WebPage(page)
    logging.info('Navigate to a page')
    pagePOM.navigate_to_page()
    yield pagePOM
    page.screenshot(path="./Results/screenshot_" + test_name + ".png", full_page=True)