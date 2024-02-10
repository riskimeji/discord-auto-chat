from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep

def auto_type_and_enter(driver, text):
    actions = webdriver.ActionChains(driver)
    actions.send_keys(text)
    actions.perform()
    sleep(1)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    sleep(2)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

# Meminta input URL dari pengguna
url_input = input("Masukkan URL Discord Channel: ")

# Inisialisasi WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(url_input)

# Tunggu 10 detik setelah membuka web
sleep(10)

messages_to_send = [
    "Hallo guys",
    "how are you doing?",
    "How are you?",
    "Congratulations",
    "This is my first time participating in such a project.",
    "good project",
    "hi",
    "hii everyone",
    "keep chatting",
    "up level",
    "fast go",
    "how to get gold role here",
    "Gomble is big project"
]

while True:
    for message in messages_to_send:
        auto_type_and_enter(driver, message)
        print(f"Message '{message}' successfully sent")
        sleep(60)
