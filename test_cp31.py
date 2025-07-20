from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

def test_inscribir_estudiante(driver):
    print("\n=== ENTRADAS ===")
    
    # Crear carpetas de capturas si no existen
    os.makedirs("capturas/entradas", exist_ok=True)
    os.makedirs("capturas/salidas", exist_ok=True)

    # Ir al home del instructor
    driver.get("https://teammates-hormiga-1.uc.r.appspot.com/web/instructor/home")
    time.sleep(1)

    # Ir a "Students"
    driver.find_element(By.LINK_TEXT, "Students").click()
    time.sleep(0.5)

    # Abrir el curso
    driver.find_element(By.CSS_SELECTOR, ".course-table:nth-child(3) .card-header").click()
    time.sleep(0.8)

    # Clic en el botón "Enroll Students"
    driver.find_element(By.ID, "btn-enroll").click()
    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "newStudentsHOT")))

    datos = {
        1: "Tutorial Group 1",  # Section
        2: "Team 1",            # Team
        3: "Tom Jacobs",        # Name
        4: "a@b"    # Email
    }

    def insertar_dato_en_celda(fila, columna, dato):
        max_intentos = 4
        for intento in range(max_intentos):
            try:
                print(f"Insertando '{dato}' en celda ({fila}, {columna}) - Intento {intento + 1}")
                celda_selector = f"#newStudentsHOT tbody tr:nth-child({fila+1}) td:nth-child({columna+1})"
                celda = driver.find_element(By.CSS_SELECTOR, celda_selector)
                ActionChains(driver).double_click(celda).perform()
                time.sleep(0.3)
                try:
                    editor = driver.find_element(By.CSS_SELECTOR, ".handsontableInput:not(.ht_editor_hidden)")
                    editor.clear()
                    editor.send_keys(dato)
                    editor.send_keys(Keys.ENTER)
                    print(f"✓ Editor funcionó para '{dato}'")
                    time.sleep(0.2)
                    return True
                except:
                    celda.send_keys(Keys.CONTROL + "a")
                    celda.send_keys(dato)
                    celda.send_keys(Keys.TAB)
                    print(f"✓ Entrada directa funcionó para '{dato}'")
                    time.sleep(0.2)
                    return True
            except Exception as e:
                print(f"✗ Fallo intento {intento + 1} para celda ({fila}, {columna}): {e}")
                time.sleep(0.5)
        print(f"✗ No se pudo insertar '{dato}' después de {max_intentos} intentos")
        return False

    for columna, dato in datos.items():
        print(f"\n--- Procesando columna {columna}: '{dato}' ---")
        success = insertar_dato_en_celda(0, columna, dato)
        if not success:
            print(f"ADVERTENCIA: No se pudo insertar '{dato}' en la columna {columna}")
        time.sleep(0.8)

    print("\nCaptura tomada: después de insertar datos en la tabla")
    driver.save_screenshot("capturas/entradas/CP31_entrada.png")
    print("Archivo: capturas/entradas/CP31_entrada.png")

    print("\n=== SALIDAS ===")

    # Confirmar inscripción
    print("Confirmando inscripción...")
    driver.find_element(By.ID, "btn-enroll").click()
    time.sleep(3)

    # Captura final
    driver.save_screenshot("capturas/salidas/CP31_salida.png")
    print("Captura tomada: capturas/salidas/CP31_salida.png")

    # Verificación visual
    try:
        toast = driver.find_element(By.CLASS_NAME, "toast-message")
        print("Resultado: Inscripción exitosa -", toast.text)
    except:
        print("Resultado: No se encontró mensaje de éxito. Posible fallo en la inscripción.")
