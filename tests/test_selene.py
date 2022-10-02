from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_selene():
    browser.open("https://github.com")
    s(".header-search-input").click()
    s(".header-search-input").send_keys("Elena0808/qa_guru_8_allure")
    s(".header-search-input").submit()
    s(by.link_text("Elena0808/qa_guru_8_allure")).click()
    s("#issues-tab").click()
    s(by.partial_text("#1")).should(be.visible)

