#--Required--#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.opera.options import Options
from selenium.webdriver.support.wait import WebDriverWait


fN = input("First Name: ")
dep = input("Department: ")
csd = input("Contract Start Date (yyyy-mm-dd): ")
lN = input("Last Name: ")
cm = input("Contract Manager: ")
ecEd = input("Expected Contract End Date: ")
ad = input("Additional Notes: ")
AzureAccess = input("Azure Access (y/n): ")
badge = input("Badge (y/n): ")
computer = input("Computer (y/n): ")
Salesforce = input("Salesforce (y/n): ")
if __name__ == '__main__':
        browser = webdriver.Edge(r"C:\\Users\\alexg\\OneDrive - Indiana University\\Desktop\edgedriver_win64\\msedgedriver.exe")
        browser.get("https://pax8prod.service-now.com/sp?id=sc_cat_item&sys_id=20cf6d4f1bc01010776199b4bd4bcb73")
        try:
                # Get the text box to insert Email using selector ID
                myElem_1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.__class__, 'ng-scope')))
                # Entering the email address
                myElem_1.send_keys(fN)
                sleep(10)
        except TimeoutException:
                print("No element found")
        sleep(10)
        browser.close()


