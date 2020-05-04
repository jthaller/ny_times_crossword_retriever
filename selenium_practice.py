from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie(executable_path = "C:\\Users\\jerem\\Documents\\Python\\ny_times_crossword_retriever\\IEDriverServer.exe")
# driver = msedgedriver(executable_path = "C:\\Users\\jerem\\Documents\\Python\\ny_times_crossword_retriever\\msedgedriver.exe")

driver.get("https://selenium.dev")
url = driver.current_url
print(url)
# print(driver.getTitle())
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
driver.close()
