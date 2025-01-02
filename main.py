from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import myket.constant as cts
from selenium.webdriver.common.action_chains import ActionChains
from myket.get_all_items import get_all_items
from myket.get_detail import get_details
from myket.get_more_link import get_more_link


service = Service("/usr/local/bin/chromedriver/chromedriver")
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser"
driver = webdriver.Chrome(service=service, options=options)


if __name__ == "__main__":

    all_links = []
    apps_url = f"{cts.base_rul}{cts.app_path}"
    for category in cts.apps_category:
        url = f"{apps_url}/{category}"
        all_links.append(get_more_link(driver, url))
        break
    flat_list = [item for sublist in all_links for item in sublist]
    for i in range(len(flat_list)):
        apps = get_all_items(driver, flat_list[i+2])
        print(f"length of apps is --------> {len(apps)}")
        for app in apps:
            app.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1')))
            time.sleep(1)
            elements = get_details(driver,
                                   driver.current_url)
            print(elements)
            print("\n-----------------------------\n")
            driver.back()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(app))
            time.sleep(1)
        break

    driver.close()
    driver.quit()
