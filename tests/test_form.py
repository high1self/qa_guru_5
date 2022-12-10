import time
import os
from selene.support.shared import browser
from selene import by, be, have, command

current_dir = os.path.dirname(os.path.abspath(__file__))
res_dir = os.path.join(current_dir, 'img')
test_file = os.path.join(res_dir, 'Screenshot_1.jpg')


def test_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('first_name')
    browser.element('#lastName').type('last_name')
    browser.element('#userEmail').type('test@gm.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('5113250530')
    browser.element('#dateOfBirthInput').click()

    browser.element('.react-datepicker-popper').should(be.enabled)

    browser.element('.react-datepicker__month-select').click()
    browser.element("//option[text()='January']").click()
    browser.element('.react-datepicker__year-select').click().type('1984').press_enter()
    browser.element('[aria-label="Choose Thursday, January 12th, 1984"]').click()
    browser.element('#subjectsInput').type('Eng').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(test_file)
    browser.element('#currentAddress').type('test adress')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#fixedban').perform(command.js.remove)

    browser.element('#submit').should(be.clickable).press_enter()
    browser.all(".modal-body tr td + td").should(have.texts("first_name last_name", "test@gm.ru", "Male", "5113250530",
                                                            "12 January,1984", "English", "Sports, Reading, Music",
                                                            "Screenshot_1.jpg",
                                                            "test adress", "NCR Delhi"))