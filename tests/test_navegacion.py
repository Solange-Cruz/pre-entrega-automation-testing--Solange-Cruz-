#Criterios mínimos:
#Valida título
#Valida presencia de productos 
#Lista nombre/precio del primero.
from utils.helpers import login
from selenium.webdriver.common.by import By

def test_catalogo():
    login(driver, "standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"


    productos = driver.find_elements(By.CSS_SELECTOR,"[data-test 'inventory-item']")

    assert len(productos) > 0
    nombre = productos[0].find_element(By.CSS_SELECTOR, "[data-test 'inventory-item']").text
    assert nombre == "Sauce Labs Backpack"

    nombre = productos[1].find_element(By.CSS_SELECTOR, "[data-test 'inventory-item']").text
    assert nombre == "Sauce Labs Bike Light"

    nombre = productos[2].find_element(By.CSS_SELECTOR, "[data-test 'inventory-item']").text
    assert nombre == "Sauce Labs Bolt T-Shirt"

    nombre = productos[3].find_element(By.CSS_SELECTOR, "[data-test 'inventory-item']").text
    assert nombre == "Sauce Labs Fleece Jacket"

    nombre = productos[4].find_element(By.CSS_SELECTOR, "[data-test 'inventory-item']").text
    assert nombre == "Sauce Labs Onesie"

    nombre = productos[5].find_element(By.CSS_SELECTOR, "[data-test 'inventory-item']").text
    assert nombre == "Test.allTheThings() T-Shirt (Red)"




