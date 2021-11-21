import time
import random
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#s = Service("C:\\Users\\alaaa\\Downloads\\chromedriver.exe")

driver = webdriver.Chrome(executable_path="C:\\Users\\alaaa\\OneDrive\\Desktop\\New folder (3)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
#driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//*[text()='Create new account']").click()
time.sleep(3)

letters = ["Harry","Ross", "Bruce","Cook", "Carolyn","Morgan", "Albert","Walker", "Randy","Reed", "Larry","Barnes", "Lois","Wilson", "Jesse","Campbell", "Ernest","Rogers", "Theresa","Patterson", "Henry","Simmons", "Michelle","Perry", "Frank","Butler", "Shirley","Brooks", "Rachel","Edwards", "Christopher","Perez", "Thomas","Baker", "Sara","Moore", "Chris","Bailey", "Roger","Johnson", "Marilyn","Thompson", "Anthony","Evans", "Julie","Hall", "Paula","Phillips", "Annie","Hernandez", "Dorothy","Murphy", "Alice","Howard"]
name = letters[random.randint(0,len(letters)-1)]
last = letters[random.randint(0,len(letters)-1)]

Years = "19"
numbers = ['80', '70', '82', '90', '99', '79', '75', '68', '87', '98', '51' , '52' , '53' , '77']
Years += numbers[random.randint(0,len(numbers)-1)]


Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct' , 'Nov' , 'Dec']
Months = Months[random.randint(0,len(Months)-1)]

Days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23']
Days = Days[random.randint(0,len(Days)-1)]

driver.find_element(By.NAME, "firstname").send_keys(name)
driver.find_element(By.NAME, "lastname").send_keys(last)
driver.find_element(By.NAME, "reg_email__").send_keys("0780228892")
driver.find_element(By.ID, "password_step_input").send_keys("aassddff88")
month = Select(driver.find_element(By.NAME, "birthday_month"))
month.select_by_visible_text(Months)
day = Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text(Days)
year = Select(driver.find_element(By.NAME, "birthday_year"))
year.select_by_visible_text(Years)
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
