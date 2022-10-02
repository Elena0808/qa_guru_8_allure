import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Elena0808")
@allure.description("Тесты по GitHub")
@allure.feature("Поиск в репозитории")
@allure.story("Ищем Issues в репозитории")
@allure.link("https://github.com")
def test_allure_decorator_step():
    open_page('https://github.com')
    search_repository('Elena0808/qa_guru_8_allure')
    go_to_the_repository('Elena0808/qa_guru_8_allure')
    open_issues()
    search_issues_test('test')


@allure.step('Открываем страницу Github')
def open_page(url):
    browser.open(url)


@allure.step('Ищем репозиторий')
def search_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step('Переходим в репозиторий')
def go_to_the_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем вкладку Issues')
def open_issues():
    s("#issues-tab").click()


@allure.step('Ищем в репозитории Issues c названием test')
def search_issues_test(name_issues):
    s(by.partial_text(name_issues)).should(be.visible)
