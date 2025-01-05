import sys
import os
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import myket.constant as cts
from selenium.webdriver.common.action_chains import ActionChains
from myket.data_store import create_csv
from myket.main import get_apps_games_myket


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


csv_file_path = "myket/data/myket_apps.csv"


if __name__ == "__main__":

    create_csv(csv_file_path, cts.csv_header)

    app_url = f"{cts.base_rul}{cts.app_path}"
    apps_category = cts.apps_category[18:]
    get_apps_games_myket(csv_file_path, driver, app_url, apps_category)
    print("end of apps")

    driver.close()
    driver.quit()
