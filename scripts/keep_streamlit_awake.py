"""
Visita la app de Streamlit Community Cloud para evitar que entre en
modo sleep (se duerme tras 12h sin trafico). Si ya esta dormida,
busca y hace click en el boton "Yes, get this app back up!".

Pensado para correr desde un GitHub Action programado
(.github/workflows/keep-streamlit-awake.yml), pero tambien se puede
correr localmente:

    pip install -r scripts/requirements-keepalive.txt
    STREAMLIT_APP_URL=https://tu-app.streamlit.app python scripts/keep_streamlit_awake.py
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

STREAMLIT_URL = os.environ.get(
    "STREAMLIT_APP_URL", "https://portafolio-data-science-2026.streamlit.app"
)

WAKE_BUTTON_XPATH = "//button[contains(., 'get this app back up')]"


def main() -> None:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(STREAMLIT_URL)
        time.sleep(5)

        try:
            wake_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, WAKE_BUTTON_XPATH))
            )
            wake_button.click()
            print("App estaba dormida - se hizo click en el boton de reactivacion.")
            time.sleep(20)
        except TimeoutException:
            print("App activa - no se encontro boton de reactivacion.")

        print(f"Visita completada a {STREAMLIT_URL}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
