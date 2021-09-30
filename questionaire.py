import os

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = Chrome(executable_path="./chrome_drivers/chromedriver.linux64", options=chrome_options)

url = "https://app.pers.ncku.edu.tw/ncov/index.php?auth"

# launch page
driver.get(url)

# login page
username = '/html/body/div/div/form/div/div[2]/div/div/div[4]/div[2]/span[1]/div/input'
password = '/html/body/div/div/form/div/div[2]/div/div/div[4]/div[2]/div/input'
login = '/html/body/div/div/form/div/div[2]/div/div/div[4]/div[6]/button'
driver.find_element(By.XPATH, username).send_keys(os.environ.get("STUDENT_ID"))
driver.find_element(By.XPATH, password).send_keys(os.environ.get("PASSWORD"))
driver.find_element(By.XPATH, login).click()

driver.execute_script('arguments[0].click()', driver.find_element(By.ID,'grid_tool_add'))

driver.implicitly_wait(5)

# form items
abnormal_fever = '/html/body/div[1]/div[1]/div[1]/div[3]/form/div/div/div[2]/span[1]/div[1]/div[1]/div/div[2]/div/ul/li[1]/label/input'
foot_print = '/html/body/div[1]/div[1]/div[1]/div[3]/form/div/div/div[2]/span[1]/div[2]/div[1]/div/div[2]/div/ul/li[1]/label/input'
screen_test = '/html/body/div[1]/div[1]/div[1]/div[3]/form/div/div/div[2]/span[1]/div[3]/div[2]/div/ul/li[1]/label/input'
submit_button = '/html/body/div[1]/div[1]/div[1]/div[3]/form/div/div/div[3]/button[2]'
driver.find_element(By.XPATH, abnormal_fever).click()
driver.find_element(By.XPATH, foot_print).click()
driver.find_element(By.XPATH, screen_test).click()
driver.find_element(By.XPATH, submit_button).click()

driver.implicitly_wait(5)
driver.close()
driver.quit()
