from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import csv
driver=webdriver.Chrome()
url="https://www.peopleperhour.com/freelance-jobs"
driver.get(url)
WebDriverWait(driver,5)

#----------------------------------------------------check-cookie-banner-----------------------------------

try:
    accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
    )
    accept.click()
    print("✅ Cookie accepted using direct XPath")
except:
    print("❌ Cookie accept button not found or not clickable.")


#---------------------------------------------------Search-Keywords----------------------------------------


try:
    search=driver.find_element(By.XPATH,"//*[@id='reactContainer']/div/div[3]/section/main/div/div[1]/div[1]/div[3]/div/div/div[1]/form/div/div/input")
    search.send_keys("Web Scraping")
    search.submit()
    time.sleep(10)
except:
    print("LOL")


#--------------------------------------------------check-cookie-banner---------------------------------------


try:
    accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
    )
    accept.click()
    print("✅ Cookie accepted using direct XPath")
except:
    print("❌ Cookie accept button not found or not clickable.")

time.sleep(5)

import os

folder_path = os.path.dirname(os.path.abspath(__file__))  # Get current file's directory
csv_path = os.path.join(folder_path, "jobs.csv")
#-----------------------------------------------------------File-Handling-----------------------------------------


with open('jobs.csv','w')as file:
    writer=csv.writer(file)
    writer.writerow(["Job Title",'Job Description','link','price'])
    posts=driver.find_elements(By.XPATH,"//*[@id='reactContainer']/div/div[3]/section/main/div/div[3]/div/div[2]/ul/li")
    for post in posts:
        try:
            title=post.find_element(By.XPATH,".//h6").text
            desc=post.find_element(By.XPATH,".//p[2]").text
            link=post.find_element(By.XPATH,'.//h6/a').get_attribute('href')
            price=post.find_element(By.XPATH,".//span[contains(@class, 'title-nano')]").text
        except:
            title='N/A'
            desc='N/A'
            link='N/A'
            price='N/A'
        writer.writerow([title,desc,link,price])
print("Done")
#-------------------------------------------------------------WhatsApp integration with Twilio--------------------------------------
import os
from twilio.rest import Client

# Load environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Twilio client setup
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+1XXXXXXXX  ',  # Twilio sandbox number
    body='🚀 New Job Alert: Web Scraping Project is live!',
    to='whatsapp:+92XXXXXXXXXX'     # Your personal number (with country code)
)

print("✅ Message sent:", message.sid)

