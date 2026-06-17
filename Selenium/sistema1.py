from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://sistema-1-login.netlify.app ")

navegador.maximize_window()

time.sleep(0.5)

navegador.find_element(By.ID, "goRegister").click()

time.sleep(1)

navegador.find_element(By.ID, "name").send_keys("João Victor")
navegador.find_element(By.ID, "email").send_keys("Joao@gmail.com")
navegador.find_element(By.ID, "password").send_keys("123456Ph")
navegador.find_element(By.ID, "confirmPassword").send_keys("123456Ph")
navegador.find_element(By.ID, "terms").click()

time.sleep(1)

navegador.find_element(By.ID, "createAccountButton").click()

time.sleep(3)


navegador.find_element(By.ID, "email").send_keys("Joao@gmail.com")
navegador.find_element(By.ID, "password").send_keys("123456Ph")

navegador.find_element(By.ID, "loginButton").click()
time.sleep(3)

# botoes = navegador.find_elements(By.CLASS_NAME, "Excluir").text










botoes = navegador.find_elements(By.XPATH, "//button[contains(., 'Excluir')]")[0].click()
navegador.switch_to.alert.accept()

time.sleep(1)

botoes = navegador.find_elements(By.XPATH, "//button[contains(., 'Excluir')]")[0].click()
navegador.switch_to.alert.accept()






















# navegador.find_elements(By.XPATH, "//button[contains(., ' Excluir ')]")[1].click()

# botoes = navegador.find_elements(By.XPATH, "//*[text()='Excluir']")

# navegador.find_element(By.ID, "botao").click()

# mensagem = navegador.find_element(By.ID, "Excluir").text


# linhas = navegador.find_elements(By.TAG_NAME, "tr")

# <button class="btn delete" onclick="deleteUser(2)"> Excluir </button>



navegador.save_screenshot("printScreenSistema1.png")

navegador.find_element(By.ID, "logoutButton").click()

time.sleep(5)