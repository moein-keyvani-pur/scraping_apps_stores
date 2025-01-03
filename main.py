from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import myket.constant as cts
from selenium.webdriver.common.action_chains import ActionChains
from myket.get_all_items import get_all_items
from myket.get_detail import get_details
from myket.get_more_link import get_more_link
from myket.data_store import create_csv
from myket.data_store import write_csv


# service = Service("/usr/local/bin/chromedriver/chromedriver")
# options = webdriver.ChromeOptions()
# options.binary_location = "/usr/bin/brave-browser"
# driver = webdriver.Chrome(service=service, options=options)


# Set Chrome options
options = Options()
options.add_argument("--headless")  # Enable headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
# Prevent crashes in resource-constrained environments
options.add_argument("--disable-dev-shm-usage")
# Required for some CI environments
options.add_argument("--remote-debugging-port=9222")

# Initialize Chrome WebDriver
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)


csv_file_path = "myket/data/myket.csv"

header = [
    "name", "link", "img", "subtitle", "version", "last_update",
    "count_download", "rate", "count_viewer", "volume", "type", "category", "app_constructor"
]


def get_apps_games_myket(url, category_list):
    all_links = []
    apps_url = url
    for category in category_list:
        url = f"{apps_url}/{category}"
        all_links.append(get_more_link(driver, url))
    flat_list = [item for sublist in all_links for item in sublist]
    for i in range(len(flat_list)):
        apps = get_all_items(driver, flat_list[i])
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
            write_csv(csv_file_path, header, elements)
            driver.back()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(app))
            time.sleep(1)
        print(flat_list[i])


if __name__ == "__main__":

    create_csv(csv_file_path, header)

    # app_url = f"{cts.base_rul}{cts.app_path}"
    # apps_category = cts.apps_category[7:]  #! change 2 
    # get_apps_games_myket(app_url, apps_category)

    games_url = f"{cts.base_rul}{cts.game_path}"
    games_category = cts.game_category
    get_apps_games_myket(games_url, games_category)

    driver.close()
    driver.quit()
