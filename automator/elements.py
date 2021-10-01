from selenium.webdriver.common.by import By

class WebFormElement:
    USERNAME_INPUT = {
        "by": By.XPATH,
        "value": "/html/body/div/div/form/div/div[2]/div/div/div[4]/div[2]/span[1]/div/input",
    }

    PASSWORD_INPUT = {
        "by": By.XPATH,
        "value": "/html/body/div/div/form/div/div[2]/div/div/div[4]/div[2]/div/input",
    }

    LOGIN_BUTTON = {
        "by": By.XPATH,
        "value": "/html/body/div/div/form/div/div[2]/div/div/div[4]/div[6]/button",
    }

    FORM_MODAL = {
        "by": By.CSS_SELECTOR,
        "value": "#arch_grid > div.modal.fade.form"
    }

    FORM_FILLING_BUTTON = {
        "by": By.ID,
        "value": "grid_tool_add"
    }

    FEVER = {
        "by": By.ID,
        "value": "fs_upd_N",
    }

    FOOTPRINT = {
        "by": By.XPATH,
        "value": "/html/body/div[1]/div[1]/div[1]/div[3]/form/div/div/div[2]/span[1]/div[2]/div[1]/div/div[2]/div/ul/li[1]/label/input",
    }

    SCREEN_TEST = {
        "by": By.XPATH,
        "value": "/html/body/div[1]/div[1]/div[1]/div[3]/form/div/div/div[2]/span[1]/div[3]/div[2]/div/ul/li[1]/label/input",
    }

    SUBMIT_BUTTON = {
        "by": By.XPATH,
        "value": "/html/body/div[1]/div[1]/div[1]/div[3]/form/div/div/div[3]/button[2]",
    }
