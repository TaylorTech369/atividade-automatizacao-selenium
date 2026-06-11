# nome-produto
# categoria-produto
# quantidade-produto
# preco-produto

# btn-cadastrar

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://sistema-3-estoque.netlify.app/")

navegador.maximize_window()

time.sleep(2)
