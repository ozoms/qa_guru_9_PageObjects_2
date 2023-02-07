from qa_guru_9_PageObjects_2.data import user
from qa_guru_9_PageObjects_2.model.pages.practice_form import PracticePage


def test_student_registration_form():
    PracticePage().open().fill(user.sasha).assert_form(user.sasha)
