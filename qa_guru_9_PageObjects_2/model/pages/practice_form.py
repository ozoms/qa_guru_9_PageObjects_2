from selene import have, command
from selene.support.shared import browser
from qa_guru_9_PageObjects_2.data.user import User, sasha
from qa_guru_9_PageObjects_2.model.controls.checkbox import Checkbox
from qa_guru_9_PageObjects_2.model.controls.datepicker import Datepicker
from qa_guru_9_PageObjects_2.model.controls.dropdown import Dropdown
from qa_guru_9_PageObjects_2.model.controls.radio import Radio
from qa_guru_9_PageObjects_2.utils.resource import Path


class PracticePage:
    def __init__(self):
        self.url = '/automation-practice-form'
        self.first_name = browser.element('#firstName')
        self.surname = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = Radio('[name=gender]')
        self.number = browser.element('#userNumber')
        self.birthday = Datepicker('#dateOfBirthInput')
        self.subject = browser.element('#subjectsInput')
        self.hobby = Checkbox('[for^=hobbies-checkbox]')
        self.picture = Path('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.region = Dropdown('#react-select-3-input')
        self.city = Dropdown('#react-select-4-input')
        self.submit = browser.element('#submit')
        self.form = browser.element('.table').all('td')

    def open(self):
        browser.open(self.url)
        browser.driver.set_window_size(1920, 1080)
        return self

    def fill(self, user: User):
        self.first_name.type(user.first_name)
        self.surname.type(user.last_name)
        self.email.type(user.email)
        self.gender.select_by_value(user.gender)
        self.number.type(user.number)
        self.birthday.select(user.birthday)
        self.subject.type(user.subject).press_enter()
        self.hobby.select(user.hobby)
        self.picture.path(user.name_file)
        self.address.type(user.address)
        self.region.select_option(user.region)
        self.city.select_option(user.city)
        self.submit.press_enter()
        return self

    def assert_form(self, user: User):
        self.form.even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.number,
            f'{user.birthday[2]} {user.birthday[0]},{user.birthday[1]}',
            user.subject,
            user.hobby,
            user.name_file,
            user.address,
            f'{user.region} {user.city}'))
        return self
