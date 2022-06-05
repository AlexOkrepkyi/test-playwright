import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page):
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()
