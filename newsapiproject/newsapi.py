import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options



#request function to get news by api call to website
def Extract_Headlines(api_key,country="il"):
    #url for call with api key and country news that i want
    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    #sending request and getting response
    response=requests.get(url)
    #converting response to python dictionary from json
    data= response.json()
    #returning the articles in the dictionary
    return data["articles"]


#sending the email with the articles using selenium
def send_email(email,password,recipient,subject,message):
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://mail.google.com")
    time.sleep(2)
    driver.find_element(By.ID,'identifierId').send_keys(email)
    time.sleep(2)
    driver.find_element(By.ID,'identifierNext').click()
    time.sleep(3)
    driver.find_element(By.NAME,"Passwd").send_keys(password)
    time.sleep(3)
    driver.find_element(By.ID,"passwordNext").click()
    time.sleep(3)
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    time.sleep(10)
    driver.find_element(By.ID,':b5').send_keys(recipient)
    time.sleep(4)
    driver.find_element(By.NAME,'subjectbox').send_keys(subject)
    driver.find_element(By.ID,':8r').send_keys(message)
    driver.find_element(By.ID,':77').click()
    time.sleep(5)
    driver.quit()

#main
if __name__=="__main__":
    #configuring api key, and email login
    api_key = ""
    email = "@gmail.com"
    password = ""
    recipient = ""
    subject = "Daily News Digest - " + datetime.now().strftime("%Y-%m-%d")
    articles = Extract_Headlines(api_key)
    message = "\n\n".join([f"{article['title']}\n{article['url']}" for article in articles])
    send_email(email, password, recipient, subject, message)