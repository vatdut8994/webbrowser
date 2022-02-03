from selenium import webdriver

PATH = "D:/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com/search?q=')