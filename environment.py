from selenium import webdriver
import re


def before_all(context):
    context.url = "https://www.ebay.com/"


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()


def before_step(context, step):
    ...


def after_step(context, step):
    if step.status == "failed":
        file_name = re.sub('[^a-zA-z0-9 \n\.]', '', step.name)
        context.driver.save_screenshot(f'./screenshots/{file_name}.png')


def after_scenario(context, scenario):
    context.driver.quit()


def after_all(context):
    print("end")
