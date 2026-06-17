from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://sistema-4-urna-v2.netlify.app/")

navegador.maximize_window()

time.sleep(1)

navegador.find_element(By.XPATH, "//button[text()='6']").click()
time.sleep(0.5)

navegador.find_element(By.XPATH, "//button[text()='4']").click()

time.sleep(0.5)

navegador.find_element(By.CLASS_NAME, "btn-confirma").click()

time.sleep(1)

navegador.save_screenshot("printScreenSistema4.png")
