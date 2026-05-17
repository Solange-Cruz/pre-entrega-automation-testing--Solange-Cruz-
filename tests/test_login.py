#Criterios mínimos:
#Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.
from utils.helpers import login
from selenium.webdriver.common.by import By

def test_login(driver):
    login(driver, "standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
