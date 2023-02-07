import selene
from selene.support.shared import browser


class Datepicker:
    def __init__(self, element: selene.Element):
        self.element = element

    def select(self, birthday):
        browser.element(self.element).click()
        browser.element('.react-datepicker__month-select').type(birthday[0])
        browser.element('.react-datepicker__year-select').type(birthday[1])
        browser.element(f'.react-datepicker__day--0{birthday[2]}').click()
