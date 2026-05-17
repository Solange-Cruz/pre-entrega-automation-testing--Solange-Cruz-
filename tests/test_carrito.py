#Criterios mínimos:
#Agrega primer producto 
#Verifica ítem en carrito.
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_agregar_al_carrito():
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)

    nombre_producto = driver.find_element(By.CSS_SELECTOR, "[data-test 'inventory_item_name']").text

    btn_agregar = wait.until(EC.element_to_be_clickable(By.XPATH,"//button[contains(text(),'Add to cart')]"))

    btn_agregar.click()

    contador_carrito = driver.find_element(By.CSS_SELECTOR, "[data-test 'shopping_cart_badge']")
    assert contador_carrito.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    producto_carrito = driver.find_element (By.CSS_SELECTOR "[data-test 'inventory_item_name']")
    assert producto_carrito == nombre_producto

