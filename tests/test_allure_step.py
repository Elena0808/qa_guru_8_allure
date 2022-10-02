import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_with_allure_step():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label("owner", "Elena0808")
    allure.dynamic.description("Тесты github")
    allure.dynamic.feature("Тесты по поиску в репозитории")
    allure.dynamic.story("Ищем Issues в репозитории")
    allure.dynamic.link("https://github.com")
    with allure.step('Открываем страницу Github'):
        browser.open('https://github.com')
    with allure.step('Ищем репозиторий'):
        s(".header-search-input").click()
        s(".header-search-input").send_keys('Elena0808/qa_guru_8_allure')
        s(".header-search-input").submit()
    with allure.step('Переходим в репозиторий'):
        s(by.link_text("Elena0808/qa_guru_8_allure")).click()
    with allure.step('Открываем вкладку Issues'):
        s("#issues-tab").click()
    with allure.step('Ищем в репозитории Issues c названием test'):
        s(by.partial_text("test")).should(be.visible)
