# First automation study usin Selenium library for automation on Python. 
# Enters site, and download chosen song to convert.
# Made by Leonardo Hoffmann Dias 03/05/2024 (march)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# User add the Youtube link of the song he\she would like to convert to mp3
link = str(input('Cole aqui o link do vídeo do youtube que você deseja converter: '))
# Open Chrome tab
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Open chosen mp3-convertion site, in this case i chose Greenconvert because there is less ads.
navegador.get('https://greenconvert.net/pt6')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="videoUrl"]').send_keys(link)
time.sleep(1)
click_button = navegador.find_element('xpath', '//*[@id="videoDetailButton"]/i')
time.sleep(1)
click_button.click()
time.sleep(30)
navegador.find_element('xpath', '//*[@id="downloadFormat"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="audio_mp3"]/option[1]').click()
time.sleep(30)
navegador.find_element('xpath', '//*[@id="downloadButton"]').click()
time.sleep(5)
# Downloads song and quit Chrome, end of program.
navegador.quit()
