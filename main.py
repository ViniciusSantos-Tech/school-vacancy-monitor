from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from TelegramBot import Bot
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import os
load_dotenv()

matricula = os.getenv('MATRICULA')
datanascimento = os.getenv("DATANASCIMENTO")
nomealuno = os.getenv("NOMEALUNO")
nomemae = os.getenv("NOMEMAE")
indexano = int(os.getenv("INDEXANO"))
indexmunicipio = int(os.getenv("INDEXMUNICIPIO"))
indexbairro = int(os.getenv("INDEXBAIRRO"))

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
hoje = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M")

wait = WebDriverWait(driver, timeout=25)
Grid = ''
try:
    driver.get("https://www.matriculafacil.rj.gov.br/Transferencia/Busca")
    wait.until(EC.presence_of_element_located((By.ID, "st-content-page")))

    Matricula = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.form-control-sm")))
    Matricula.send_keys(matricula)
    Data = wait.until(EC.visibility_of_element_located((By.ID, "DataNascimento")))
    Data.send_keys(datanascimento)
    CampoNome = wait.until(EC.visibility_of_element_located((By.ID, "NomeCompl")))
    CampoNome.send_keys(nomealuno)
    Campomae = wait.until(EC.visibility_of_element_located((By.ID, "NomeMae")))
    Campomae.send_keys(nomemae)
    Botao = wait.until(EC.element_to_be_clickable((By.ID, "BuscarCandidato")))
    Botao.click()
except Exception as e:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 1 - Erro: {e}​")
    raise
#______________________________________________________________
try:
    BotaoPesquisar = wait.until(EC.presence_of_element_located((By.ID, "ListaEscola")))
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        BotaoPesquisar
    )
except Exception as e:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 2 - {e}​")
    raise

sleep(5)
#______________________________________________________________
try:
    select = Select(wait.until(EC.element_to_be_clickable((By.ID, "EtapaEnsinoPesquisa"))))
    select.select_by_index(indexano)

    select2 = Select(wait.until(EC.element_to_be_clickable((By.ID, "MunicipioPesquisa"))))
    select2.select_by_index(indexmunicipio)

     wait.until(
    lambda driver: len(Select(driver.find_element(By.ID, "BairroPesquisa")).options) > indexbairro)


    Manha = wait.until(EC.element_to_be_clickable((By.XPATH,"//label[@for='TurnoManha']")))
    Manha.click()
    BotaoPesquisar.click()
    sleep(5)
    Grid = driver.find_element(By. ID, "ulListGrid" ).text
except Exception as e:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 3​ - {e}")
    raise

#_________________________________________________________________
try:
    if "Sem escolas retornadas" in Grid:
        Bot(f"| DATA - {hoje} | Status - Sem Vagas❌​")
    else:
        Bot(f"| DATA - {hoje} | Status - VAGAS ENCONTRADAS!!✅​")
except Exception as e:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 4​ - {e}")
    raise
finally:
    driver.quit()
