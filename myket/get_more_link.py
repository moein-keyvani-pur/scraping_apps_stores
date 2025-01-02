from selenium import webdriver
from selenium.webdriver.common.by import By


def get_more_link(driver,url):
    driver.get(url)
    links = []
    sections_dom = driver.find_elements(
        By.XPATH, "/html/body/article/section[@class='category-list']")
    sections_count = len(sections_dom)
    for i in range(sections_count):
        more_link = sections_dom[i].find_element(
            By.XPATH, f"./div/div/a").get_attribute("href")
        links.append(more_link)
    return links
