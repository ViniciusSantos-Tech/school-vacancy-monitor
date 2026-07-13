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
wait = WebDriverWait(driver, timeout=30)
try:
    driver.get("https://www.matriculafacil.rj.gov.br/Transferencia/Busca")

    wait.until(EC.presence_of_element_located((By.ID, "st-content-page")))

    Matricula = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control.form-control-sm"))
    )
    Matricula.send_keys("202505460253566")

    Data = wait.until(
        EC.visibility_of_element_located((By.ID, "DataNascimento"))
    )
    Data.send_keys("04062010")

    CampoNome = wait.until(
        EC.visibility_of_element_located((By.ID, "NomeCompl"))
    )
    CampoNome.send_keys("VINICIUS RUFINO DA SILVA SANTOS")

    Campomae = wait.until(
        EC.visibility_of_element_located((By.ID, "NomeMae"))
    )
    Campomae.send_keys("MONIQUE RUFINO DA SILVA")

    Botao = wait.until(
        EC.element_to_be_clickable((By.ID, "BuscarCandidato"))
    )
    Botao.click()
    sleep(5)

    print("Depois do clique:")
    print(driver.current_url)
    print(driver.title)
    
    driver.save_screenshot("depois_clique.png")

    print("Fase 1 OK")

except Exception as e:
    print("ERRO FASE 1:", e)
    driver.save_screenshot("erro_fase1.png")
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 1")


#______________________________________________________________
try:
    sleep(5)

    print(driver.page_source[:1000])

    BotaoPesquisar = wait.until(
        EC.element_to_be_clickable((By.ID, "ListaEscola"))
    )

except Exception as e:
    print("ERRO FASE 2:", e)
    raise
#______________________________________________________________
Grid = ""
try:
    select = Select(wait.until(
        EC.element_to_be_clickable((By.ID, "EtapaEnsinoPesquisa"))
    ))
    select.select_by_index(6)

    select2 = Select(wait.until(
        EC.element_to_be_clickable((By.ID, "MunicipioPesquisa"))
    ))
    select2.select_by_index(50)

    select3 = Select(wait.until(
        EC.element_to_be_clickable((By.ID, "BairroPesquisa"))
    ))
    select3.select_by_index(27)

    Manha = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='TurnoManha']"))
    )
    Manha.click()

    BotaoPesquisar.click()

    Grid = wait.until(
        EC.presence_of_element_located((By.ID, "ulListGrid"))
    ).text

    print("Fase 3 OK")

except Exception as e:
    print("ERRO FASE 3:", e)
    driver.save_screenshot("erro_fase3.png")
    Bot(f"| DATA - {hoje} | Status - Erro no Script!!⚠️ - Fase 3")
#______________________________________________________________

if "Sem escolas retornadas" in Grid:
    Bot(f"| DATA - {hoje} | Status - Sem Vagas❌")
else:
    Bot(f"| DATA - {hoje} | Status - VAGAS ENCONTRADAS!!✅")
driver.quit()
