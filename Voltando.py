from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=5)

driver.get("https://www.matriculafacil.rj.gov.br/Transferencia/Busca")
elemento = wait.until(EC.presence_of_element_located((By.ID, "st-content-page")))
driver.maximize_window()
Matricula = driver.find_element(By.CLASS_NAME, "form-control.form-control-sm")
Matricula.send_keys(202505460253566)
sleep(1)
Data = driver.find_element(By.ID, "DataNascimento")
Data.send_keys("06042010")
sleep(1)
Meunome = driver.find_element(By.ID, "NomeCompl")
Meunome.send_keys("VINICIUS RUFINO DA SILVA SANTOS")
sleep(1)
Nomemae = driver.find_element(By.ID, "NomeMae")
Nomemae.send_keys("MONIQUE RUFINO DA SILVA")
sleep(1)
Botao = driver.find_element(By.ID, "BuscarCandidato")
Botao.click()
sleep(1)
#______________________________________________________________

BotaoPesquisar = driver.find_element(By.ID, "ListaEscola")

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    BotaoPesquisar
)
sleep(1)
#______________________________________________________________
select = Select(driver.find_element(By.ID, "EtapaEnsinoPesquisa"))
select.select_by_index(6)
sleep(1)
select2 = Select(driver.find_element(By.ID, "MunicipioPesquisa"))
select2.select_by_index(50)
sleep(1)
select3 = Select(driver.find_element(By.ID, "BairroPesquisa"))
select3.select_by_index(27)
sleep(1)
Manha = driver.find_element(By.XPATH,"//label[@for='TurnoManha']").click()
sleep(1)
BotaoPesquisar.click()
sleep(2)
Grid = driver.find_element(By. ID, "ulListGrid" ).text
if "Sem escolas retornadas" in Grid:
    print("Sem vagas no momento")
else:
    print("VAGA!!!!!!!!!!")

driver.quit()
