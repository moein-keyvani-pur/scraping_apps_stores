from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def get_details(driver, address):
    driver.get(address)
    app = driver.find_elements(By.XPATH, "/html/body/div[3]/section[1]")[0]

    # Fixed items
    try:
        app_name = app.find_element(By.XPATH, "./div[1]/div[1]/div[2]/h1").text
    except NoSuchElementException:
        app_name = ""

    try:
        app_link = app.find_element(
            By.XPATH, "./div[1]/div[2]/a").get_attribute("href")
    except NoSuchElementException:
        app_link = ""

    try:
        app_img = app.find_element(
            By.XPATH, "./div[1]/div[1]/div[1]/img").get_attribute("src")
    except NoSuchElementException:
        app_img = ""

    try:
        app_subtitle = app.find_element(
            By.XPATH, "./div[1]/div[1]/div[2]/h2").text
    except NoSuchElementException:
        app_subtitle = ""

    # Iterating from the 4th row onward in the table
    table_data = {}
    rows = app.find_elements(By.XPATH, "./div[2]/table/tbody/tr")

    for i in range(4, len(rows) + 1):
        try:
            td1 = app.find_element(
                By.XPATH, f"./div[2]/table/tbody/tr[{i}]/td[1]").text
            td2 = app.find_element(
                By.XPATH, f"./div[2]/table/tbody/tr[{i}]/td[2]").text
            if td1 == "نسخه":
                td1 = "version"
            elif td1 == "آخرین بروزرسانی":
                td1 = "last_update"
            elif td1 == "تعداد دانلود":
                td1 = "count_download"
            elif td1 == "امتیاز":
                td1 = "rate"
            elif td1 == "تعداد نظرات":
                td1 = "count_viewer"
            elif td1 == "حجم":
                td1 = "volume"
            elif td1 == "نوع":
                td1 = "type"
            elif td1 == "دسته‌بندی":
                td1 = "category"
            elif td1 == "سازنده":
                td1 = "app_constructor"
            else:
                td1 = "data_file"
            table_data[td1] = td2
        except NoSuchElementException:
            continue

    # Returning the collected data
    return {
        "name": app_name,
        "link": app_link,
        "img": app_img,
        "subtitle": app_subtitle,
        **table_data
    }
