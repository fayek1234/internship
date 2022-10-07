import allure
from app.application import Application
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'fayekchowdhury_tbOEx5'
bs_key = 'KzMb64qmGyt9XoQiUQ9E'



def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # context.driver = webdriver.Chrome(executable_path='/Users/khizi/PycharmProjects/internship2/chromedriver.exe')
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Firefox(executable_path='/Users/khizi/PycharmProjects/internship2/geckodriver.exe')
    # context.driver = webdriver.Safari()
    #
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options)



    # Mobile - run tests on mobile web browser
    options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "Nexus 5"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(chrome_options=options,executable_path='/Users/khizi/PycharmProjects/internship2/chromedriver.exe')



    mobile_emulation = {

        "deviceMetrics": {"width": 360, "height": 1120, "pixelRatio": 3.0},

        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    chrome_options = Options()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    context.driver = webdriver.Chrome(chrome_options=chrome_options)

    mobile_emulation = {"deviceName": "Nexus 5"}

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Remote(command_executor='https://fayekchowdhury_tbOEx5:KzMb64qmGyt9XoQiUQ9E@hub-cloud.browserstack.com/wd/hub',

                              desired_capabilities=chrome_options.to_capabilities())



    # for browerstack ###
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
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