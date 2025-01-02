from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_all_items(driver, address):
    driver.get(address)
    scroll_pause_time = 2  # Time to wait for loading after each scroll
    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0
    while True and count < 3:
        # Scroll down
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        more_button_list = driver.find_elements(
            By.XPATH, "/html/body/article/section/div[2]/button")
        if len(more_button_list) > 0:
            driver.execute_script("arguments[0].click();", more_button_list[0])
            time.sleep(scroll_pause_time)

        # Check if the scroll reached the bottom
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        count += 1
    time.sleep(scroll_pause_time)
    data = []
    child_count = 0
    parent_div = driver.find_elements(
        By.XPATH, '/html/body/article/section/div[1]')[0]
    child_elements = parent_div.find_elements(By.XPATH, "./div")

    for child in child_elements:
        data.append(child)

    child_count += len(child_elements)
    return data
