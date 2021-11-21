import time
import random
import self as self
import tk as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import clipboard


Comment = "Hi"
driver = webdriver.Chrome(executable_path="C:\\Users\\alaaa\\OneDrive\\Desktop\\New folder (3)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.ID, "email").send_keys("lastafurtu@vusra.com")
driver.find_element(By.ID, "pass").send_keys("aassddff88")
driver.find_element(By.XPATH, "//*[text()='Log In']").click()
time.sleep(3)
driver.get("https://www.facebook.com/watch/live/?ref=search&v=274161941321468")
driver.find_element(By.XPATH, "//div[text()='Comment']").click()
day = Select(driver.find_element(By.XPATH, "//span[@data-outline-text()='true']").send_keys(Comment))
act = ActionChains(driver)
act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

time.sleep(10)


