from playwright.sync_api import Page, sync_playwright
import logging
import pytest
import time
from POM.webpagePOM import WebPage

# Logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)

@pytest.fixture
def pagePOM(page: Page, request):
    test_name = request.node.name
    pagePOM = WebPage(page)
    logging.info('Navigate to a page')
    pagePOM.navigate_to_page()
    page.wait_for_load_state('networkidle')
    yield pagePOM
    page.screenshot(path="./Results/screenshot_" + test_name + ".png", full_page=True)

def test_verify_home_page_has_correct_title(pagePOM: WebPage):
    logging.info('Verify the home page title')
    page_title = pagePOM.return_page_title()
    assert pagePOM.PAGE_TITLE in page_title

def test_verify_home_page_has_docs_link(pagePOM: WebPage):
    logging.info('Verify the home page contains Docs link')
    assert pagePOM.is_link_visible(pagePOM.DOCS_LINK)

def test_verify_home_page_has_about_link(pagePOM: WebPage):
    logging.info('Verify the home page contains About link')
    assert pagePOM.is_link_visible(pagePOM.ABOUT_LINK)

def test_verify_navigation_to_docs_page(pagePOM: WebPage, page: Page):
    logging.info('Verify the navigation to Docs page')
    pagePOM.click_on_link(pagePOM.DOCS_LINK)
    page.wait_for_load_state('networkidle')
    time.sleep(3)
    logging.info('Verify the DOCS page heading')
    assert pagePOM.is_heading_visible(pagePOM.DOCS_HEADING)