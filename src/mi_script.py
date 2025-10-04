import warnings
warnings.filterwarnings("ignore", category=UserWarning)  # Silenciar warnings de urllib3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def flujo_nopcommerce():
    # === Configurar navegador ===
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    # === Crear carpeta de evidencias ===
    base_path = os.path.dirname(os.path.abspath(__file__))
    evidencia_path = os.path.join(base_path, "../reports/evidencias")
    os.makedirs(evidencia_path, exist_ok=True)

    # === Función auxiliar para evidencias con scroll ===
    def tomar_evidencias_scroll(nombre):
        driver.save_screenshot(f"{evidencia_path}/{nombre}_01.png")
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(1)
        driver.save_screenshot(f"{evidencia_path}/{nombre}_02_scroll.png")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.save_screenshot(f"{evidencia_path}/{nombre}_03_final.png")
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

    # === Paso 1: Abrir página principal ===
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    time.sleep(2)
    tomar_evidencias_scroll("01_home")

    # === Paso 2: Navegar por menú "Computers > Notebooks" ===
    computers = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Computers")))
    actions.move_to_element(computers).perform()
    notebooks = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Notebooks")))
    notebooks.click()
    time.sleep(2)
    tomar_evidencias_scroll("02_computers_notebooks")

    # === Paso 3: Ir a "Electronics" ===
    electronics = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Electronics")))
    electronics.click()
    time.sleep(2)
    tomar_evidencias_scroll("03_electronics")

    # === Paso 4: Ir a "Apparel" ===
    apparel = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Apparel")))
    apparel.click()
    time.sleep(2)
    tomar_evidencias_scroll("04_apparel")

    # === Paso 5: Buscar "computer" ===
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.clear()
    search_box.send_keys("computer")
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-box-button")))
    search_button.click()
    time.sleep(2)
    tomar_evidencias_scroll("05_busqueda_computer")

    # === Paso 6: Ir a "Jewelry" ===
    jewelry = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Jewelry")))
    jewelry.click()
    time.sleep(2)
    tomar_evidencias_scroll("06_jewelry")

    # === Paso 7: Ir a "Books" ===
    books = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Books")))
    books.click()
    time.sleep(2)
    tomar_evidencias_scroll("07_books")

    # === Paso 8: Ir a "Gift Cards" ===
    gift_cards = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Gift Cards")))
    gift_cards.click()
    time.sleep(2)
    tomar_evidencias_scroll("08_gift_cards")

    # === Paso 9: Ir a "Apple" ===
    apple = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Apple")))
    driver.execute_script("arguments[0].scrollIntoView(true);", apple)
    time.sleep(1)
    apple.click()
    time.sleep(2)
    tomar_evidencias_scroll("09_apple")

    # === Paso 10: Ir a "Log in" ===
    log_in = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
    log_in.click()
    time.sleep(2)

    # === Paso 11: Ingresar correo ===
    for _ in range(3):
        try:
            email_input = wait.until(EC.element_to_be_clickable((By.ID, "Email")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email_input)
            email_input.clear()
            email_input.send_keys("ignacioacevedo123@hotmail.com")
            driver.save_screenshot(f"{evidencia_path}/11_login_email_ingresado.png")
            break
        except StaleElementReferenceException:
            time.sleep(0.3)

    # === Paso 12: Ingresar contraseña ===
    for _ in range(3):
        try:
            pass_input = wait.until(EC.element_to_be_clickable((By.ID, "Password")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pass_input)
            pass_input.clear()
            pass_input.send_keys("1234456")
            driver.save_screenshot(f"{evidencia_path}/12_login_password_ingresado.png")
            break
        except StaleElementReferenceException:
            time.sleep(0.3)

    # === Paso 13: Click en botón Log in ===
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button")))
    login_button.click()
    driver.save_screenshot(f"{evidencia_path}/13_login_boton_click.png")

    # === Paso 14: Click en link Register ===
    header_register = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header_register)
    header_register.click()
    driver.save_screenshot(f"{evidencia_path}/14_register_link_click.png")
    time.sleep(2)

    # === Paso 15: Ingresar nombre ===
    for _ in range(3):
        try:
            first_name_input = wait.until(EC.element_to_be_clickable((By.ID, "FirstName")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_name_input)
            first_name_input.clear()
            first_name_input.send_keys("Ignacio")
            driver.save_screenshot(f"{evidencia_path}/15_register_nombre_ingresado.png")
            break
        except StaleElementReferenceException:
            time.sleep(0.3)

    # === Paso 16: Ingresar apellido ===
    for _ in range(3):
        try:
            last_name_input = wait.until(EC.element_to_be_clickable((By.ID, "LastName")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", last_name_input)
            last_name_input.clear()
            last_name_input.send_keys("Acevedo Pajarito")
            driver.save_screenshot(f"{evidencia_path}/16_register_apellido_ingresado.png")
            break
        except StaleElementReferenceException:
            time.sleep(0.3)

    # === Paso 17: Ingresar correo ===
    for _ in range(3):
        try:
            email_input = wait.until(EC.element_to_be_clickable((By.ID, "Email")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email_input)
            email_input.clear()
            email_input.send_keys("ignacio.acevedo.qa@gmail.com")
            driver.save_screenshot(f"{evidencia_path}/17_register_email_ingresado.png")
            break
        except StaleElementReferenceException:
            time.sleep(0.3)

    # === Paso 18: Ingresar empresa ===
    for _ in range(3):
        try:
            company_input = wait.until(EC.element_to_be_clickable((By.ID, "Company")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", company_input)
            company_input.clear()
            company_input.send_keys("Vamos QA 123")
            driver.save_screenshot(f"{evidencia_path}/18_register_company_ingresado.png")
            break
        except StaleElementReferenceException:
            time.sleep(0.3)

    # === Paso 19: Ingresar contraseña registro ===
    for _ in range(3):
        try:
            password_input = wait.until(EC.element_to_be_clickable((By.NAME, "Password")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", password_input)
            password_input.clear()
            password_input.send_keys("ignacio12312323123")
            driver.save_screenshot(f"{evidencia_path}/19_register_password_ingresado.png")
            break
        except StaleElementReferenceException:
            time.sleep(0.3)

 # === Paso 20: Ingresar  confirmar contraseña registro ===
    for _ in range(3):
        try:
            confirmPassword_input = wait.until(EC.element_to_be_clickable((By.ID, "ConfirmPassword")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirmPassword_input)
            confirmPassword_input.clear()
            confirmPassword_input.send_keys("ignacio12312323123")
            driver.save_screenshot(f"{evidencia_path}/19_register_ConfirmPassword.png")
            break
        except StaleElementReferenceException:
            time.sleep(5)



if __name__ == "__main__":
    flujo_nopcommerce()
