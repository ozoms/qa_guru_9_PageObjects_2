import selene
from selene.support.shared import browser
from selene import have


class Radio:
    def __init__(self, element: selene.Element):
        self.element = element

    def select_by_value(self, text):
        browser.all(self.element).element_by(have.value(text)).element('..').click()
