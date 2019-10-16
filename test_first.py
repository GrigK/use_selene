import time
from selene.api import browser, s, ss, have, be


def test_heroku(set_browser):
    browser.open_url('https://todomvc4tasj.herokuapp.com')
    s("#new-todo").should(be.blank).set_value(1), "Not found this element"
    time.sleep(1)
    s("#new-todo").press_enter()
    ss("#todo-list>li").should(have.exact_texts("1")), "Not found list TODO"

