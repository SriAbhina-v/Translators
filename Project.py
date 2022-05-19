import os
from time import sleep
try:
    from selenium import webdriver
except:
    os.system("pip3 install selenium --quiet")
    from selenium import webdriver
from selenium.webdriver.chrome.service import Service
try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system("pip3 install webdriver_manager --quiet")

fren = "https://www.wordreference.com/fren/"
enfr = "https://www.wordreference.com/enfr/"
def EXEMAIN():

    query = input("Word: ").lower()
    f = os.popen('curl -s -L https://www.wordreference.com/enfr/' + query)
    try:
        if "No translation found for" in f.read():
            query = 'https://www.wordreference.com/fren/' + query
        else:
            query = "https://www.wordreference.com/enfr/" + query
        f.close()
    except:
        dsfew = 0
    try:
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(query)

        sleep(15)

        browser.quit()
        return EXEMAIN()
    except:
        return EXEMAIN()
EXEMAIN()