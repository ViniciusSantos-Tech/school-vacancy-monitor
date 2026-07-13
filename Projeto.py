from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from TelegramBot import Bot
from datetime import datetime

hoje = datetime.now().strftime("%d/%m/%Y")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=5)
try:
    driver.get("https://www.matriculafacil.rj.gov.br/Transferencia/Busca")
    wait.until(EC.presence_of_element_located((By.ID, "st-content-page")))
    driver.maximize_window()
    Matricula = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.form-control-sm")))
    Matricula.send_keys(202505460253566)
    Data = wait.until(EC.visibility_of_element_located((By.ID, "DataNascimento")))
    Data.send_keys("06042010")
    CampoNome = wait.until(EC.visibility_of_element_located((By.ID, "NomeCompl")))
    CampoNome.send_keys("VINICIUS RUFINO DA SILVA SANTOS")
    Campomae = wait.until(EC.visibility_of_element_located((By.ID, "NomeMae")))
    Campomae.send_keys("MONIQUE RUFINO DA SILVA")
    Botao = wait.until(EC.element_to_be_clickable((By.ID, "BuscarCandidato")))
    Botao.click()
except:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 1​")
#______________________________________________________________
try:
    BotaoPesquisar = driver.find_element(By.ID, "ListaEscola")
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        BotaoPesquisar
    )
except:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 2​")
sleep(1)
#______________________________________________________________
try:
    select = Select(wait.until(EC.element_to_be_clickable((By.ID, "EtapaEnsinoPesquisa"))))
    select.select_by_index(6)

    select2 = Select(wait.until(EC.element_to_be_clickable((By.ID, "MunicipioPesquisa"))))
    select2.select_by_index(50)

    select3 = Select(wait.until(EC.element_to_be_clickable((By.ID, "BairroPesquisa"))))
    select3.select_by_index(27)

    Manha = wait.until(EC.element_to_be_clickable((By.XPATH,"//label[@for='TurnoManha']")))
    Manha.click()
    BotaoPesquisar.click()
    sleep(2)
    Grid = driver.find_element(By. ID, "ulListGrid" ).text
except:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 3​")

if "Sem escolas retornadas" in Grid:
    Bot(f"| DATA - {hoje} | Status - Sem Vagas❌​")
else:
    Bot(f"| DATA - {hoje} | Status - VAGAS ENCONTRADAS!!✅​")

driver.quit()
