from playwright.sync_api import Page, sync_playwright
import pytest
import time
from POM.webpagePOM import WebPage

@pytest.fixture
def pagePOM(page: Page, request):
    test_name = request.node.name
    pagePOM = WebPage(page)
    pagePOM.navigate_to_page()
    page.wait_for_load_state('networkidle')
    yield pagePOM
    page.screenshot(path="./Results/screenshot_" + test_name + ".png", full_page=True)

def test_verify_home_page_has_correct_title(pagePOM: WebPage):
    print('\n*** TC: Verify the home page title')
    page_title = pagePOM.get_page_title()
    assert pagePOM.PAGE_TITLE in page_title, f"Page title is incorrect: {page_title}"

def test_verify_home_page_has_docs_link(pagePOM: WebPage):
    print('\n*** TC: Verify the home page contains Docs link')
    assert pagePOM.is_link_visible(pagePOM.DOCS_LINK), "Docs link is not visible"

def test_verify_home_page_has_about_link(pagePOM: WebPage):
    print('\n*** TC: Verify the home page contains About link')
    assert pagePOM.is_link_visible(pagePOM.ABOUT_LINK), "About link is not visible"

def test_verify_navigation_to_docs_page(pagePOM: WebPage, page: Page):
    print('\n*** TC: Verify the navigation to Docs page')
    pagePOM.click_on_link(pagePOM.DOCS_LINK)
    page.wait_for_load_state('networkidle')
    time.sleep(pagePOM.TIMEOUT)
    print('\nVerify the DOCS page heading')
    assert pagePOM.is_heading_visible(pagePOM.DOCS_HEADING), "DOCS heading is not visible"