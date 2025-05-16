from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random

class WebAutomation:
    def __init__(self, driver_path=None):
        """
        Inicializa o driver do Selenium
        :param driver_path: Caminho para o driver (opcional)
        """
        if driver_path:
            self.driver = webdriver.Chrome(executable_path=driver_path)
        else:
            self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator, by=By.XPATH):
        """
        Clica em um elemento
        :param locator: Localizador do elemento
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, locator)))
            element.click()
        except TimeoutException:
            print(f"Elemento não encontrado: {locator}")

    def digitar(self, locator, texto, by=By.XPATH):
        """
        Digita texto em um elemento
        :param locator: Localizador do elemento
        :param texto: Texto a ser digitado
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            element.clear()
            element.send_keys(texto)
        except TimeoutException:
            print(f"Elemento não encontrado: {locator}")

    def select_by_value(self, locator, value, by=By.XPATH):
        """
        Seleciona uma opção em um elemento select pelo valor
        :param locator: Localizador do elemento select
        :param value: Valor da opção
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            select = Select(element)
            select.select_by_value(value)
        except TimeoutException:
            print(f"Elemento select não encontrado: {locator}")

    def select_by_text(self, locator, text, by=By.XPATH):
        """
        Seleciona uma opção em um elemento select pelo texto visível
        :param locator: Localizador do elemento select
        :param text: Texto da opção
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            select = Select(element)
            select.select_by_visible_text(text)
        except TimeoutException:
            print(f"Elemento select não encontrado: {locator}")

    def get_text(self, locator, by=By.XPATH):
        """
        Obtém o texto de um elemento
        :param locator: Localizador do elemento
        :param by: Tipo de localizador (padrão: XPATH)
        :return: Texto do elemento
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            return element.text
        except TimeoutException:
            print(f"Elemento não encontrado: {locator}")
            return None

    def is_element_present(self, locator, by=By.XPATH):
        """
        Verifica se um elemento está presente na página
        :param locator: Localizador do elemento
        :param by: Tipo de localizador (padrão: XPATH)
        :return: True se o elemento estiver presente, False caso contrário
        """
        try:
            self.wait.until(EC.presence_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    def wait_for_element(self, locator, timeout=10, by=By.XPATH):
        """
        Aguarda um elemento ficar visível
        :param locator: Localizador do elemento
        :param timeout: Tempo máximo de espera em segundos
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator, by=By.XPATH):
        """
        Rola a página até um elemento
        :param locator: Localizador do elemento
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            print(f"Elemento não encontrado: {locator}")

    def close(self):
        """
        Fecha o navegador
        """
        self.driver.quit()

    def digitar_como_humano(self, locator, texto, by=By.XPATH, delay_min=0.1, delay_max=0.3):
        """
        Digita texto em um elemento simulando digitação humana
        :param locator: Localizador do elemento
        :param texto: Texto a ser digitado
        :param by: Tipo de localizador (padrão: XPATH)
        :param delay_min: Delay mínimo entre teclas em segundos
        :param delay_max: Delay máximo entre teclas em segundos
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            element.clear()
            for char in texto:
                element.send_keys(char)
                time.sleep(random.uniform(delay_min, delay_max))
        except TimeoutException:
            print(f"Elemento não encontrado: {locator}")

    def executar_javascript(self, script, *args):
        """
        Executa um script JavaScript
        :param script: Script JavaScript a ser executado
        :param args: Argumentos para o script
        :return: Resultado da execução do script
        """
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            print(f"Erro ao executar JavaScript: {str(e)}")
            return None

    def click_por_javascript(self, locator, by=By.XPATH):
        """
        Clica em um elemento usando JavaScript
        :param locator: Localizador do elemento
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            print(f"Elemento não encontrado: {locator}")

    def digitar_por_javascript(self, locator, texto, by=By.XPATH):
        """
        Digita texto em um elemento usando JavaScript
        :param locator: Localizador do elemento
        :param texto: Texto a ser digitado
        :param by: Tipo de localizador (padrão: XPATH)
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, locator)))
            self.driver.execute_script("arguments[0].value = arguments[1];", element, texto)
        except TimeoutException:
            print(f"Elemento não encontrado: {locator}")
