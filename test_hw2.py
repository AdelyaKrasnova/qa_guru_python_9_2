import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def open_browser():
    browser.config.window_width = 375
    browser.config.window_height = 667

    yield
    browser.quit()


def test_first_search(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second_search(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('7t77gh8y').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу 7t77gh8y ничего не найдено.'))
