from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_details(driver, address):
    driver.get(address)
    app = driver.find_elements(By.XPATH, "/html/body/div[3]/section[1]")[0]

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

    try:
        app_version = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[1]/td[2]").text
    except NoSuchElementException:
        app_version = ""

    try:
        app_last_update = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[2]/td[2]").text
    except NoSuchElementException:
        app_last_update = ""

    try:
        app_count_download = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[3]/td[2]").text
    except NoSuchElementException:
        app_count_download = ""

    try:
        app_rate = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[4]/td[2]").text
    except NoSuchElementException:
        app_rate = ""

    try:
        app_count_viewer = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[5]/td[2]").text
    except NoSuchElementException:
        app_count_viewer = ""

    try:
        app_volume = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[6]/td[2]").text
    except NoSuchElementException:
        app_volume = ""

    try:
        app_type = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[7]/td[2]").text
    except NoSuchElementException:
        app_type = ""

    try:
        app_category = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[8]/td[2]").text
    except NoSuchElementException:
        app_category = ""

    try:
        app_constructor = app.find_element(
            By.XPATH, "./div[2]/table/tbody/tr[9]/td[2]").text
    except NoSuchElementException:
        app_constructor = ""

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
        "category": app_category,
        "app_constructor": app_constructor
    }
