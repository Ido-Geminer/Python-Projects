from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
def go_to_moodle(userinfo):
    #load driver from its directory
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s=Service("C:\\Users\\ido geminer\\Desktop\\moodleprojcet\\chromedriver.exe")
    driver = webdriver.Chrome(options=options,service=s)

    driver.get("https://moodle.tau.ac.il/login/index.php")

    #elements i want to wait for and then i continue
    username=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,"Ecom_User_ID")))
    user_id=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,"Ecom_User_Pid")))
    password=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,"Ecom_Password")))

    #clear fields i want to use
    username.clear()
    user_id.clear()
    password.clear()

    #sending keys to fields
    username.send_keys(userinfo[0])
    user_id.send_keys(userinfo[1])
    password.send_keys(userinfo[2])

    #submiting fields and logging in
    WebDriverWait(driver,7).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()