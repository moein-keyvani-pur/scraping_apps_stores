import time
from myket.data_store import write_csv
from myket.get_all_items import get_all_items
from myket.get_detail import get_details
from myket.get_more_link import get_more_link
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import myket.constant as cts


def get_apps_games_myket(csv_file_path, driver, url, category_list):
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
            write_csv(csv_file_path, cts.csv_header, elements)
            driver.back()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(app))
            time.sleep(1)
        print(flat_list[i])
