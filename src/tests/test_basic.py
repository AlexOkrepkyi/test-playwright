import pytest

from src.pom.LoginPage import LoginPage


@pytest.mark.login
def test_standard_login(set_up):
    page = set_up
    login_page = LoginPage(page)

    login_page.login_standard_user()
