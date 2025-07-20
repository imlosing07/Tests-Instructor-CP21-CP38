from selenium.webdriver.common.by import By
import time

def test_cp34_buscar_estudiante_por_nombre(driver):
    print("\n========== CASO DE PRUEBA: CP37 - Buscar por nombre de equipo ==========\n")

    print("=== ENTRADAS ===")
    driver.get("https://teammates-hormiga-1.uc.r.appspot.com/web/instructor/home")
    print("1. Navegando al home del instructor...")

    driver.find_element(By.LINK_TEXT, "Search").click()
    time.sleep(1)
    print("2. Click en 'Search'.")

    search_input = driver.find_element(By.ID, "search-keyword")
    search_input.click()
    search_input.send_keys("Team 1")
    time.sleep(1)
    print("3. Se ingresó el nombre de equipo: 'Team 1'.")

    # Captura de la entrada
    driver.save_screenshot("capturas/entradas/CP37_entrada.png")
    print("✓ Captura tomada: entrada registrada correctamente.")

    driver.find_element(By.CSS_SELECTOR, ".text-muted li:nth-child(1)").click()
    print("4. Se seleccionó la primera sugerencia del criterio de búsqueda.")
    time.sleep(1)

    driver.find_element(By.ID, "btn-search").click()
    print("5. Se ejecutó la búsqueda.")
    time.sleep(5)

    print("\n=== SALIDAS ===")
    # Intentar expandir el resultado si existe
    try:
        result_section = driver.find_element(By.CSS_SELECTOR, "#main-content > .ng-star-inserted:nth-child(2)")
        driver.execute_script("arguments[0].scrollIntoView(true);", result_section)
        time.sleep(1)
        result_section.click()
        print("✓ Primer resultado expandido correctamente.")
    except Exception as e:
        print(f"✗ No se pudo expandir el resultado: {e}")
    
    # Captura del resultado
    driver.save_screenshot("capturas/salidas/CP37_salida.png")
    print("✓ Captura tomada: resultado de búsqueda almacenado.")
    
    print("\n✅ Resultado: Team 'Team 1' buscado exitosamente.\n")