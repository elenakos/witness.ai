from playwright.sync_api import Page
import logging

class WebPage:
    # Variables
    URL = "https://rickandmortyapi.com/"
    TIMEOUT = 3

    # Elements - labels/ids
    # -------------------------------
    PAGE_TITLE = "The Rick and Morty API"
    HOME_LINK = "home page"
    DOCS_LINK = "Docs"
    ABOUT_LINK = "About"
    DOCS_HEADING = "Documentation"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_page(self, url=URL):
        print('Navigate to a page {}'.format(url))
        self.page.goto(url)

    def return_page_title(self):
        return self.page.title()

    def click_on_link(self, link_name):
        print('Click on a link')
        self.page.get_by_role("link", name=link_name).first.click()

    def is_heading_visible(self, heading_name):
        print('Verify if a heading visible')
        return self.page.get_by_role("heading", name=heading_name).is_visible()

    def is_image_visible(self, image_name):
        print('Verify if an image visible')
        return self.page.get_by_role("img", name=image_name).is_visible()

    def is_text_visible(self, text):
        print('Verify if a text visible')
        return self.page.get_by_text(text).is_visible()

    def is_link_visible(self, link_name):
        print('Verify if a link visible')
        return self.page.get_by_role("link", name=link_name).is_visible()

    def verify_text_on_page(page: Page, text_to_verify: str):
        print("Verify this text on page: " + text_to_verify)
        content = page.locator("body").text_content()
        if text_to_verify in content:
            print("--> Text found!")
            return True
        else:
            print("--> Text not found!")
            return False