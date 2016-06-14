#!/usr/bin/env python

# import needed libraries
from selenium.webdriver import PhantomJS
from selenium.common.exceptions import NoSuchElementException


# A GoodReads specific PhantomJS browser class
class GoodReadsBrowser(PhantomJS):
    def __init__(self):
        # Call super class constructor
        PhantomJS.__init__(self, "./phantomjs")
        self.next_page = None

    # General shortcut to open a GoodReads page
    def open(self, sub_url, keyword):
        self.get("https://www.goodreads.com" + sub_url + str(keyword))

    # Shortcut to open GoodReads book page
    def open_book(self, book_id):
        self.open("/book/show/", book_id)

    # Shortcut to open GoodReads books list
    def open_list(self, list_id):
        self.open("/list/show/", list_id)

    # Shortcut to open a GoodReads search page for books lists
    def open_list_search(self, keyword):
        self.open("/search?search_type=lists&q=", keyword)

    # Check if there's a next page
    def has_next_page(self):
        # Try to find the next button
        try:
            self.next_page = self.find_element_by_class_name("next_page")
        # Return false if there isn't one
        except NoSuchElementException:
            return False
        # Check if button is click-able (i.e. it's anchor tag)
        return self.next_page.tag_name == 'a'

    # Click the next button to go to next page
    def goto_next_page(self, repeated=False):
        # If nothing is repeated and there's next button
        if not repeated and self.next_page:
            self.next_page.click()
            return True
        return False

    # Get all links in page that has css class "XTitle"
    def links(self, title):
        return self.find_elements_by_class_name(title + "Title")