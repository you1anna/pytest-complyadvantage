import os

from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from ..tests.page_objects.politician_page import PoliticanPage

# run all tests
scenarios('features')


@fixture()
def browser():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.name == 'nt':
        _browser = WebDriver(os.path.join(dir_path, "chromedriver.exe"))
    else:
        _browser = WebDriver(os.path.join(dir_path, "chromedriver"))
    yield _browser
    _browser.close()
    _browser.quit()


@given('I visit the new entity page')
def given_visit_new_entity_page(browser):
    PoliticanPage(browser).open()


@when(parsers.parse('I add details for "{politician}"'))
def when_add_details_politican(browser, politician):
    PoliticanPage(browser) \
        .add_full_name(politician) \
        .add_country("UK")\
        .add_yob("19011963")\
        .add_position("MP")\
        .add_url("https://www.johnbercow.co.uk")\
        .select_risk("High")\
        .click_save()


@then(parsers.parse('"{politician}" should be added to the list'))
def then_should_add_filter(browser, politician):
    modal = PoliticanPage(browser).save_record()
    confirmation_text = modal.get_attribute("innerText")
    assert politician in confirmation_text

