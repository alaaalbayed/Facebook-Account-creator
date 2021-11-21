import time
import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import clipboard
import secrets
import string

#PROXY = "176.9.119.170:3128" # IP:PORT or HOST:PORT
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
#chrome = webdriver.Chrome(chrome_options=chrome_options)

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path="C:\\Users\\alaaa\\OneDrive\\Desktop\\New folder (3)\\chromedriver.exe")
driver.get("https://tempail.com/en/")
time.sleep(2)

driver.find_element(By.ID, "eposta_adres").click()
driver.get("https://www.facebook.com/")
#act = ActionChains(driver)
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.find_element(By.XPATH, "//*[text()='Create new account']").click()
time.sleep(2)

letters = ["Harry","Ross", "Bruce","Cook", "Carolyn","Morgan", "Albert","Walker", "Randy","Reed", "Larry","Barnes", "Lois","Wilson", "Jesse","Campbell", "Ernest","Rogers", "Theresa","Patterson", "Henry","Simmons", "Michelle","Perry", "Frank","Butler", "Shirley","Brooks", "Rachel","Edwards", "Christopher","Perez", "Thomas","Baker", "Sara","Moore", "Chris","Bailey", "Roger","Johnson", "Marilyn","Thompson", "Anthony","Evans", "Julie","Hall", "Paula","Phillips", "Annie","Hernandez", "Dorothy","Murphy", "Alice","Howard","Liam","Olivia","Noah","Emma","Oliver","Ava","William","Sophia","Elijah","Isabella","James","Charlotte","Benjamin","Amelia","Lucas","Mia","Mason","Harper","Ethan","Evelyn"]
name = letters[random.randint(0,len(letters)-1)]
last = letters[random.randint(0,len(letters)-1)]

Years = "19"
numbers = ['80', '70', '82', '90', '99', '79', '75', '68', '87', '98', '51' , '52' , '53' , '77']
Years += numbers[random.randint(0,len(numbers)-1)]


Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct' , 'Nov' , 'Dec']
Months = Months[random.randint(0,len(Months)-1)]

Days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23']
Days = Days[random.randint(0,len(Days)-1)]

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(10))

driver.find_element(By.NAME, "firstname").send_keys(name)
driver.find_element(By.NAME, "lastname").send_keys(last)
text = clipboard.paste()
driver.find_element(By.NAME, "reg_email__").send_keys(text)
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(text)
driver.find_element(By.ID, "password_step_input").send_keys(password)
print(text)
print(password)
month = Select(driver.find_element(By.NAME, "birthday_month"))
month.select_by_visible_text(Months)
day = Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text(Days)
year = Select(driver.find_element(By.NAME, "birthday_year"))
year.select_by_visible_text(Years)
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
time.sleep(25)
#act = ActionChains(driver)
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
#time.sleep(3)
#act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
#time.sleep(10)
driver.get("https://tempail.com/en/")
time.sleep(5)
driver.find_element(By.XPATH, "//*[text()='Refresh']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[text()='FB-Facebook confirmation code']").click()
time.sleep(3)
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
time.sleep(5)
with open("Output.txt", "a") as text_file:
    print(f"{text}:{password}", file=text_file)
driver.quit()

