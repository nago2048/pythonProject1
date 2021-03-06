from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

eBay = "https://www.ebay.com/"
eBay_deals = "https://www.ebay.com/deals"
eBay_bo = "https://www.ebay.com/b/Brand-Outlet/bn_7115532402"
eBay_help = "https://www.ebay.com/help/home"


@step('Navigate to eBay')
def test(context):
    context.driver = webdriver.Chrome()
    context.driver.get(eBay)
# !!!!without "context.driver" each step opens new browser!!!


@step('Type "{text}" in search input')
def step_impl(context, text):
    search_input = context.driver.find_element_by_xpath("//input[@id='gh-ac']")
    search_input.send_keys(text)


@step("Search by click")
def step_impl(context):
    search_btn = context.driver.find_element_by_xpath("//input[@id='gh-btn']")
    search_btn.click()


@step('Verify that "{text}" in results')
def step_impl(context, text):
    result_block = context.driver.find_element_by_xpath("//div[@id='srp-river-results']")
    result_text = result_block.text
    result_text.index(text)


@step('Verify that "{text}" not in results')
def step_impl(context, text):
    result_block = context.driver.find_element_by_xpath("//div[@id='srp-river-results']")
    result_text = result_block.text
    if result_text.find(text) != -1:
        raise Exception("Test failed")


@step("Search by enter")
def step_impl(context):
    search_input = context.driver.find_element_by_xpath("//input[@id='gh-ac']")
    search_input.send_keys(Keys.ENTER)


@step("Hover all navigation elements")
def step_impl(context):
    context.driver.maximize_window()
    sleep(5)

    sign_in = context.driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")
    register = context.driver.find_element_by_xpath("//a[contains(text(),'register')]")
    daily_deals = context.driver.find_element_by_xpath("//a[contains(text(),'Daily Deals') and @class='gh-p']")
    brand_outlet = context.driver.find_element_by_xpath("//a[contains(text(),'Brand Outlet')]")
    help_and_contact = context.driver.find_element_by_xpath("//a[contains(text(),' Help & Contact') and @class='gh-p']")
    sell = context.driver.find_element_by_xpath("//a[contains(text(),' Sell') and @class='gh-p']")
    watchlist = context.driver.find_element_by_xpath("//a[@title='Watchlist']")
    my_ebay = context.driver.find_element_by_xpath("//a[@title='My eBay']")
    alrt = context.driver.find_element_by_xpath("//i[@id='gh-Alerts-i']/..")
    cart = context.driver.find_element_by_xpath("//a[@title='Your shopping cart']")

    action = ActionChains(context.driver)
    action.move_to_element(sign_in).move_to_element(register).move_to_element(daily_deals).move_to_element(brand_outlet).move_to_element(help_and_contact).move_to_element(sell).move_to_element(watchlist).move_to_element(my_ebay).move_to_element(alrt).move_to_element(cart).perform()


@step('Change width to "{value}"')
def step_impl(context, value):
    context.driver.set_window_size(value, 800)
    sleep(2)


@step("Verify that Watchlist link is visible")
def step_impl(context):
    watchlist = context.driver.find_element_by_xpath("//a[@title='Watchlist']")
    watchlist.click()


@step("Verify that Watchlist link is not visible")
def step_impl(context):
    watchlist = context.driver.find_element_by_xpath("//a[@title='Watchlist']")
    if watchlist.is_displayed():
        raise Exception("Test failed")
