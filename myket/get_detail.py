from selenium import webdriver
from selenium.webdriver.common.by import By


def get_details(driver,address):
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
