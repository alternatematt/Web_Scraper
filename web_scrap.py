from selenium import webdriver

PATH = 'PATH OF CHROME DRIVER'
driver = webdriver.Chrome(PATH)

driver.get("http://github.com/")
