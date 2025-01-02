from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import constant as cts


service = Service("/usr/local/bin/chromedriver/chromedriver")
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser"
driver = webdriver.Chrome(service=service, options=options)


def get_all_items(address):
    driver.get(address)
    scroll_pause_time = 2  # Time to wait for loading after each scroll
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

        # Check if the scroll reached the bottom
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    data = []
    child_count = 0
    parent_div = driver.find_elements(
        By.XPATH, '/html/body/article/section/div[1]')[0]
    child_elements = parent_div.find_elements(By.XPATH, "./div")

    for child in child_elements:
        data.append(child)

    child_count += len(child_elements)
    return data


def get_details(address):
    driver.get(address)
    app = driver.find_elements(By.XPATH, "/html/body/div[3]/section[1]")[0]
    app_name = app.find_element(By.XPATH, "./div[1]/div[1]/div[2]/h1").text
    app_link = app.find_element(
        By.XPATH, "./div[1]/div[2]/a").get_attribute("href")
    app_img = app.find_element(
        By.XPATH, "./div[1]/div[1]/div[1]/img").get_attribute("src")
    app_subtitle = app.find_element(By.XPATH, "./div[1]/div[1]/div[2]/h2").text
    app_version = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[1]/td[2]").text
    app_last_update = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[2]/td[2]").text
    app_count_download = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[3]/td[2]").text
    app_rate = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[4]/td[2]").text
    app_count_viewer = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[5]/td[2]").text
    app_volume = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[6]/td[2]").text
    app_type = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[7]/td[2]").text
    app_category = app.find_element(
        By.XPATH, "./div[2]/table/tbody/tr[8]/td[2]").text

    return {
        "name": app_name,
        "link": app_link,
        "img": app_img,
        "subtitle": app_subtitle,
        "version": app_version,
        "last_update": app_last_update,
        "count_download": app_count_download,
        "rate": app_rate,
        "count_viewer": app_count_viewer,
        "volume": app_volume,
        "type": app_type,
        "category": app_category
    }


if __name__ == "__main__":

    # elements = get_details(
    #     "https://myket.ir/app/com.shatelland.namava.mobile")
    # print(elements)

    # *****************************************
    # apps=get_all_items("https://myket.ir/list/most-useful-android-apps-in-daily-life")
    apps = get_all_items("https://myket.ir/list/best-finance-apps")
    print(len(apps))
    # for app in apps:
    #     app.click()
    #     # get_all_items("/html/body/div[3]/section[1]")

    # *****************************************

    driver.close()
    driver.quit()
