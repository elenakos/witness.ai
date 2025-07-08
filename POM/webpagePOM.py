from playwright.sync_api import Page
import logging

class WebPage:
    # Variables
    URL = "https://rickandmortyapi.com/"

    # Elements - labels/ids
    # -------------------------------
    TITLE = "The Rick and Morty API"
    HOME_LINK = "home page"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_page(self, url=URL):
        logging.info('Navigate to a page')
        self.page.goto(url)

    def return_page_title(self):
        return self.page.title()

    def click_on_link(self, link_name):
        logging.info('Click on a link')
        self.page.get_by_role("link", name=link_name).first.click()

    def is_heading_visible(self, heading_name):
        logging.info('Verify if a heading visible')
        return self.page.get_by_role("heading", name=heading_name).is_visible()

    def is_image_visible(self, image_name):
        logging.info('Verify if an image visible')
        return self.page.get_by_role("img", name=image_name).is_visible()

    def is_text_visible(self, text):
        logging.info('Verify if a text visible')
        return self.page.get_by_text(text).is_visible()