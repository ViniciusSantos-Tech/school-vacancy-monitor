from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from TelegramBot import Bot
from datetime import datetime
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
hoje = datetime.now().strftime("%d/%m/%Y %H:%M")
wait = WebDriverWait(driver, timeout=25)
Grid = ''
try:
    driver.get("https://www.matriculafacil.rj.gov.br/Transferencia/Busca")

    sleep(5)

    print("URL ATUAL:", driver.current_url)
    print("TÍTULO:", driver.title)

    driver.save_screenshot("inicio.png")

    Matricula = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control.form-control-sm"))
    )

    print("Campo matrícula encontrado!")

except Exception as e:
    print("ERRO FASE 1:", e)
    driver.save_screenshot("erro_fase1.png")
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
    driver.save_screenshot("erro_fase2.png")
sleep(5)
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
    sleep(10)
    Grid = driver.find_element(By. ID, "ulListGrid" ).text
except Exception as e:
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 3​ - {e}")
    driver.save_screenshot("erro_fase3.png")

if "Sem escolas retornadas" in Grid:
    Bot(f"| DATA - {hoje} | Status - Sem Vagas❌​")
else:
    Bot(f"| DATA - {hoje} | Status - VAGAS ENCONTRADAS!!✅​")

driver.quit()
