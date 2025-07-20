from selenium.webdriver.common.by import By
import time
import os

def test_crear_curso_estando_logueado(driver):
    print("\n===== ENTRADAS =====")

    # Esta URL ya es la de home del instructor
    driver.get("https://teammates-hormiga-1.uc.r.appspot.com/web/instructor/home")

    # Crear carpetas de capturas si no existen
    os.makedirs("capturas/entradas", exist_ok=True)
    os.makedirs("capturas/salidas", exist_ok=True)

    # Abrir formulario para nuevo curso
    driver.find_element(By.LINK_TEXT, "Add New Course").click()
    print("Paso: Formulario de nuevo curso abierto")
    time.sleep(2)  # Esperar a que se cargue el formulario

    # Llenar y enviar el formulario
    driver.find_element(By.ID, "course-id").send_keys("CS2025-VAL")
    driver.find_element(By.ID, "course-name").send_keys("%12312")
    
    # Captura de entrada
    driver.save_screenshot("capturas/entradas/CP25_entrada.png")
    print("Captura tomada: capturas/entradas/CP25_entrada.png")
    time.sleep(1)  # Esperar un poco antes de enviar
    
    driver.find_element(By.ID, "btn-submit-course").click()
    time.sleep(5)

    print("\n===== SALIDAS =====")

    # Captura de salida
    driver.save_screenshot("capturas/salidas/CP25_salida.png")
    print("Captura tomada: capturas/salidas/CP25_salida.png")