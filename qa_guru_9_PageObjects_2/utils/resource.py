import selene
from selene.support.shared import browser
import os
import tests


class Path:
    def __init__(self, element: selene.Element):
        self.element = element

    def path(self, name_file):
        browser.element(self.element).set_value(
            os.path.abspath(os.path.join(
                os.path.dirname(tests.__file__), f'resources/{name_file}')
            )
        )
