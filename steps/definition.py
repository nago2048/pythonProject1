from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings

eBay = "https://www.ebay.com/"
eBay_deals = "https://www.ebay.com/deals"
eBay_bo = "https://www.ebay.com/b/Brand-Outlet/bn_7115532402"
eBay_help = "https://www.ebay.com/help/home"


@step('Navigate to eBay')
def test(context):
    context.driver = webdriver.Chrome()
    context.driver.get(eBay)


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


@step("Maximize window")
def step_impl(context):
    context.driver.maximize_window()


@step("Hover all navigation elements")
def step_impl(context):
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


@step('Verify that "{text}" link is visible in header')
def step_impl(context, text):
    watchlist = context.driver.find_element_by_xpath(f"//*[contains(@title, '{text}') or contains(text(), '{text}')]")
    if not watchlist.is_displayed():
        raise Exception("Test failed")


@step('Verify that "{text}" link is not visible in header')
def step_impl(context, text):
    watchlist = context.driver.find_element_by_xpath(f"//*[contains(@title, '{text}') or contains(text(), '{text}')]")
    if watchlist.is_displayed():
        raise Exception("Test failed")


@step('Click on "{text}" link in header')
def step_impl(context, text):
    link = context.driver.find_element_by_xpath(f"//*[contains(@class, 'gh-') and contains(text(),'{text}')]")
    link.click()
    sleep(2)


@step("Go back")
def step_impl(context):
    context.driver.back()


@step('Filter results by "{par1}" and "{par2}" and "{par3}" and print results')
def step_impl(context, par1, par2, par3):
    results_list = context.driver.find_elements_by_xpath(f"//li[@class='s-item    '][.//span[text()='{par1}']][.//span[text()='{par2}']][.//span[text()='{par3}']]")
    for x in results_list:
        print(x)


@step('Verify that "{text}" in results in {n:d} pages')
def step_impl(context, text, n):
    current_page = 1
    mismatches = []
    while current_page <= n:
        result_items = context.driver.find_elements_by_xpath("//li[starts-with(@class,'s-item')]//h3")
        mismatches_local = 0
        for i in result_items:
            if text.lower() not in i.text.lower():
                mismatches.append(' >>>  mismatch on page ' + str(current_page) + " >>> " + i.text)
                mismatches_local += 1
        if mismatches_local > 35:
            raise Exception("Early fail")
        current_page += 1
        if current_page <= n:
            arrow = context.driver.find_element_by_xpath("//a[@type='next']")
            arrow.click()

    if len(mismatches) > n*2.5:
        for i in mismatches:
            print(i)
        raise Exception("fail")
    elif len(mismatches) > 0:
        for i in mismatches:
            print(i)
            warnings.warn('>>>>>> Normal amount of mismatches')
    else:
        print("No mismatches")


@step('filter by "{var1}" in "{var2}" category')
def step_impl(context, var1, var2):


    cb = context.driver.find_elements_by_xpath(f"//li[@class='x-refine__main__list '][.//h3[text()='{var2}']]//div[@class='x-refine__select__svg'][.//span[text()='{var1}']]//input")
    for i in cb:
        i.click()

    if not cb:
        raise Exception("fail")


@step("Apply following filters")
def step_impl(context):
    for y in context.table.rows:
        var2 = y['Filter :']
        var1 = y['value :']

        category_btn = context.driver.find_elements_by_xpath(f"//li[@class='x-refine__main__list '][.//h3[text()='{var2}']]//div[@aria-expanded='false']")

        if not category_btn:
            cb = context.driver.find_elements_by_xpath(f"//li[@class='x-refine__main__list '][.//h3[text()='{var2}']]//div[@class='x-refine__select__svg'][.//span[text()='{var1}']]//input")
            for i in cb:
                i.click()
        else:
            category_btn[0].click()
            cb = context.driver.find_elements_by_xpath(
                f"//li[@class='x-refine__main__list '][.//h3[text()='{var2}']]//div[@class='x-refine__select__svg'][.//span[text()='{var1}']]//input")
            for i in cb:
                i.click()

