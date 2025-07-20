from selenium.webdriver.common.by import By
import time
import os

def test_crear_curso_estando_logueado(driver):
    print("\n===== ENTRADAS =====")
    # Datos de entrada para el nuevo curso
    course_id = "ST01_2025_S1"
    course_name = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(f"Entradas: course_id = {course_id}")
    print(f"Entradas: course_name = {course_name}")
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
    driver.find_element(By.ID, "course-id").send_keys("ST01_2025_S1")
    driver.find_element(By.ID, "course-name").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
    # Captura de entrada
    driver.save_screenshot("capturas/entradas/CP28_entrada.png")
    print("Captura tomada: capturas/entradas/CP28_entrada.png")
    time.sleep(1)  # Esperar un poco antes de enviar
    
    driver.find_element(By.ID, "btn-submit-course").click()
    time.sleep(5)

    print("\n===== SALIDAS =====")

    # Captura de salida
    driver.save_screenshot("capturas/salidas/CP28_salida.png")
    print("Captura tomada: capturas/salidas/CP28_salida.png")