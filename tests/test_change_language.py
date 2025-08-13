import allure
from selenium.webdriver.common.by import By


def test_change_language(project_page_fixture):
    with allure.step('Нажать кнопку изменения языка'):
        project_page_fixture.click_element()

    with allure.step('Проверить что язык изменился'):
        assert project_page_fixture.get_text().strip() == 'Ru'
