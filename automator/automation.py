import os

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from elements import WebFormElement

def environment_factory():
    executable_path = os.environ.get("WEBDRIVER", "./chrome_drivers/chromedriver.mac64_m1")
    username = os.environ.get("STUDENT_ID")
    password = os.environ.get("PASSWORD")
    assert username, "STUDENT_ID is not set, please add it to environment variable"
    assert password, "PASSWORD is not set, please add it to environment variable"
    assert os.path.isfile(executable_path), f"WEBDRIVER is set (or default) to {executable_path}, not found, please add it to environment variable"
    return {
        "username": username,
        "password": password,
        "executable_path": executable_path,
    }


def perform_submission():
    env_values = environment_factory()
    chrome_options = Options()
    if os.environ.get("HEADLESS", False):
        chrome_options.add_argument("--headless")
    driver = Chrome(executable_path=env_values["executable_path"], options=chrome_options)
    url = "https://app.pers.ncku.edu.tw/ncov/index.php?auth"
    # launch page
    driver.get(url)
    # login page
    driver.find_element(**WebFormElement.USERNAME_INPUT).send_keys(env_values["username"])
    driver.find_element(**WebFormElement.PASSWORD_INPUT).send_keys(env_values["password"])
    driver.find_element(**WebFormElement.LOGIN_BUTTON).click()
    driver.implicitly_wait(20)
    # modal appears first
    if not driver.find_element(**WebFormElement.FORM_MODAL).get_attribute("class") == "model fade form in":
        driver.execute_script('arguments[0].click()', driver.find_element(**WebFormElement.FORM_FILLING_BUTTON))
    driver.implicitly_wait(5)
    # form items
    driver.find_element(**WebFormElement.FEVER).click()
    driver.find_element(**WebFormElement.FOOTPRINT).click()
    driver.find_element(**WebFormElement.SCREEN_TEST).click()
    driver.implicitly_wait(5)
    driver.find_element(**WebFormElement.SUBMIT_BUTTON).click()
    # end
    driver.close()
    driver.quit()
