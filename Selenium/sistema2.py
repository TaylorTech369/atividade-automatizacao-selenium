from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://sistema-2-loja.netlify.app ")

navegador.maximize_window()

time.sleep(2)

navegador.find_element(By.XPATH, "//*[contains(text(), 'Criar Conta')]").click()

time.sleep(1)

navegador.find_element(By.ID, "name").send_keys("joão")
navegador.find_element(By.ID, "email").send_keys("joao@gmail.com")
navegador.find_element(By.ID, "password").send_keys("123456Ph")
time.sleep(1)
botoes = navegador.find_elements(By.XPATH, "//button[contains(., 'Cadastrar')]")[0].click()
navegador.switch_to.alert.accept()

time.sleep(1)

navegador.find_element(By.ID, "email").send_keys("joao@gmail.com")
navegador.find_element(By.ID, "password").send_keys("123456Ph")
navegador.find_element(By.ID, "loginButton").click()
time.sleep(1)

navegador.find_element(By.ID, "depositInput").send_keys("100000000000000000000000000004500")
navegador.find_element(By.ID, "depositButton").click()
navegador.switch_to.alert.accept()

time.sleep(1)

navegador.find_element(By.ID, "productsTabButton").click()

navegador.find_elements(By.XPATH, "//button[contains(., 'Adicionar ao Carrinho')]")[0].click()
time.sleep(0.5)
navegador.switch_to.alert.accept()

time.sleep(1)

navegador.find_element(By.XPATH, "//a[contains(text(), 'Carrinho')]").click()

navegador.find_element(By.CLASS_NAME, "checkout").click()

navegador.save_screenshot("printScreenSistema2-1.png")

navegador.find_element(By.ID, "finishButton").click()
navegador.switch_to.alert.accept()

# navegador.save_screenshot("printScreenSistema2-2.png")

time.sleep(3)