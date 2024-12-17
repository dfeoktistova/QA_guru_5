from selene import browser, have, by
import os


first_name = 'Santa'
last_name = 'Claus'
email = f'{first_name}@mail.com'
user_number = '1234567890'
birth_day = '11'
birth_month = 'April'
birth_year = '2007'
gender = "Male"
subjects = 'Maths'
hobby = 'Reading'
picture = 'pic.webp'
address = 'Zamshina street, 11/5'
state = 'NCR'
city = 'Noida'


def test_fill_form():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').click().type(first_name)
    browser.element('#lastName').click().type(last_name)
    browser.element('#userEmail').click().type(email)
    browser.element(by.text(gender)).click()
    browser.element('#userNumber').click().type(user_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]').click().element(by.text(birth_year)).click()
    browser.element('[class="react-datepicker__month-select"]').click().element(by.text(birth_month)).click()
    browser.element('[class="react-datepicker__day react-datepicker__day--011"]').click()
    browser.element('[id="subjectsInput"]').click().type('Maths').press_enter()
    browser.element(by.text(hobby)).click()
    browser.element('#uploadPicture').set_value(os.path.abspath(f'../test/{picture}'))
    browser.element('#currentAddress').click().type(address)
    browser.element('#state').click().element(by.text(state)).click()
    browser.element('#city').click().element(by.text(city)).click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element("[class='table-responsive']").should(have.text(f'{first_name} {last_name}'))
    browser.element("[class='table-responsive']").should(have.text(email))
    browser.element("[class='table-responsive']").should(have.text(gender))
    browser.element("[class='table-responsive']").should(have.text(user_number))
    browser.element("[class='table-responsive']").should(have.text(f'{birth_day} {birth_month},{birth_year}'))
    browser.element("[class='table-responsive']").should(have.text(subjects))
    browser.element("[class='table-responsive']").should(have.text(picture))
    browser.element("[class='table-responsive']").should(have.text(address))
    browser.element("[class='table-responsive']").should(have.text(f'{state} {city}'))
