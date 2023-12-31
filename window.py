from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

windowWidth = 600
windowHeight = 800

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--kiosk") #full screen
options.add_argument("--app=https://priyankajudiya123.pythonanywhere.com/#home") #remove addressbar
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(windowWidth, windowHeight, windowHandle='current')


driver.get("https://priyankajudiya123.pythonanywhere.com/#home")
