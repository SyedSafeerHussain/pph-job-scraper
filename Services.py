from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
driver=webdriver.Chrome()
url="https://www.peopleperhour.com/"
driver.get(url)
wait=WebDriverWait(driver,4)
#------------------------------------------------------check-cookie-banner-----------------------------------------------------------
try:
    accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
    )
    accept.click()
    print("✅ Cookie accepted using direct XPath")
except:
    print("❌ Cookie accept button not found or not clickable.")
#------------------------------------------------------------Search-Keywords--------------------------------------------------------
try:
    search=driver.find_element(By.XPATH,"//*[@id='reactContainer']/div/div[3]/section/main/section[1]/div/div/div/div[3]/div[2]/form/div/div/input")
    search.send_keys("Web Scraping")
    search.submit()
    time.sleep(5)
except:
    print("LOL")
#---------------------------------------------------------Next-Page------------------------------------------------------------------
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='startRow']/div/div[2]"))
)
# check cookie banner
try:
    accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='cookie-banner']/div/div[2]/a"))
    )
    accept.click()
    print("✅ Cookie accepted using direct XPath")
except:
    print("❌ Cookie accept button not found or not clickable.")

#-----------------------------------------------------------------File-Handling--------------------------------------------------------

posts=driver.find_elements(By.XPATH,"//*[@id='startRow']/div/div[2]/ul/li")
with open("Services.csv",'w') as file:
    writer=csv.writer(file)
    writer.writerow(['JOB Title','Link','Price'])
    for post in posts:
        try:
            title=post.find_element(By.TAG_NAME,"a").text
            j_link=post.find_element(By.TAG_NAME,'a')
            link=j_link.get_attribute('href')
            price=post.find_element(By.XPATH,"//*[@id='startRow']/div/div[2]/ul/li/div/div[3]/div[2]/span").text
        except:
            title='N/A'
            link='n/a'
            price='n/a'
        writer.writerow([title,link,price])
driver.quit()
