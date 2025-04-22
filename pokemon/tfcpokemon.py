from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# URL de la página
url = "https://gamevlg.com/pokemon-tcg-pocket/cards"

# Configurar Selenium (puedes poner headless=True si quieres ocultar el navegador)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Navegar a la página
driver.get(url)
time.sleep(5)  # esperar a que cargue bien la página y las imágenes

# Crear carpeta para las imágenes
output_dir = 'pokemon_cards'
os.makedirs(output_dir, exist_ok=True)

# Buscar todas las imágenes con class="w-full object-cover"
images = driver.find_elements(By.CSS_SELECTOR, 'img.w-full.object-cover')

# Descargar cada imagen
for img in images:
    img_url = img.get_attribute('src')
    alt_text = img.get_attribute('alt').replace(" ", "_")
    extension = os.path.splitext(img_url)[-1].split('?')[0]
    if not extension:
        extension = '.jpg'
    
    filename = f"{output_dir}/{alt_text}{extension}"
    
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Descargada: {filename}")
    else:
        print(f"Error descargando {img_url}")

# Cerrar el navegador
driver.quit()

print("Descarga completada.")
