import selene
from selene.support.shared import browser


class Dropdown:
    def __init__(self, element: selene.Element):
        self.element = element

    def select_option(self, text):
        browser.element(self.element).type(text).press_enter()
