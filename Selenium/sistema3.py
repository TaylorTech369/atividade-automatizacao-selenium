from selenium import webdriver
from selenium.webdriver.common.by import By
import time


produtos = [
    {"nome": "Teclado Mecânico", "categoria": "Periféricos", "quantidade": "15", "preco": "250"},
    {"nome": "Mouse Gamer", "categoria": "Periféricos", "quantidade": "30", "preco": "120"},
    {"nome": "Monitor 24'", "categoria": "Monitores", "quantidade": "5", "preco": "899"},
    {"nome": "Headset HyperX", "categoria": "Áudio", "quantidade": "12", "preco": "349"},
    {"nome": "Webcam Full HD", "categoria": "Periféricos", "quantidade": "8", "preco": "199"},
    {"nome": "Cadeira Gamer", "categoria": "Móveis", "quantidade": "4", "preco": "1200"},
    {"nome": "Mousepad Extended", "categoria": "Acessórios", "quantidade": "25", "preco": "59"},
    {"nome": "SSD 1TB NVMe", "categoria": "Hardware", "quantidade": "20", "preco": "450"},
    {"nome": "Memória RAM 16GB", "categoria": "Hardware", "quantidade": "18", "preco": "299"},
    {"nome": "Gabinete ATX RGB", "categoria": "Hardware", "quantidade": "6", "preco": "380"}
]








navegador = webdriver.Chrome()
navegador.get("https://sistema-3-estoque.netlify.app/")
navegador.maximize_window()

time.sleep(3)






for produto in produtos:
    input_nome = navegador.find_element(By.ID, "nome-produto")
    input_categoria = navegador.find_element(By.ID, "categoria-produto")
    input_qtd = navegador.find_element(By.ID, "quantidade-produto")
    input_preco = navegador.find_element(By.ID, "preco-produto")
    btn_cadastrar = navegador.find_element(By.ID, "btn-cadastrar")
    


    input_nome.clear()
    input_categoria.clear()
    input_qtd.clear()
    input_preco.clear()


    
    input_nome.send_keys(produto["nome"])
    input_categoria.send_keys(produto["categoria"])
    input_qtd.send_keys(produto["quantidade"])
    input_preco.send_keys(produto["preco"])
    


    btn_cadastrar.click()
    
    time.sleep(1)


navegador.save_screenshot("printScreenSistema3.png")

time.sleep(1)