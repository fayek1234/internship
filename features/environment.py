
from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait





def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    context.driver = webdriver.Chrome(executable_path='/Users/khizi/PycharmProjects/internship2/chromedriver.exe')
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Firefox(executable_path='/Users/svetlanalevinsohn/JobEasy/11-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Safari()



    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
     print('\nStarted scenario: ', scenario.name)
     browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)



def after_step(context, step):
    if step.status == 'failed':
      print('\nStep failed: ', step)



def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()