import selene
from selene import have
from selene.support.shared import browser


class Checkbox:
    def __init__(self, element: selene.Element):
        self.element = element

    def select(self, text):
        browser.all(self.element).element_by(have.text(text)).click()
