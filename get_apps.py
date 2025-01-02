import constant as cts


def get_more_link(url):
    driver.get(url)
    links = []
    sections_dom = driver.find_elements(
        By.XPATH, "/html/body/article/section[@class='category-list']")
    sections_count = len(sections_dom)
    print(sections_count)
    for i in range(sections_count):
        more_link = sections_dom[i].find_element(
            By.XPATH, f"./div/div/a").get_attribute("href")
        links.append(more_link)
    return links

    all_links = []
    apps_url = f"{cts.base_rul}{cts.app_path}"

    for category in cts.apps_category:
        url = f"{apps_url}/{category}"
        all_links.append(get_more_link(url))
