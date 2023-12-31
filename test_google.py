import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google_search(browser):
    browser.get("https://www.google.com")
    browser.find_element(By.XPATH, "//*[@id='L2AGLb']/div").click()

    search_bar = browser.find_element(By.NAME, "q")
    search_query = "Python"
    search_bar.send_keys(search_query)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()

    WebDriverWait(browser, 10).until(EC.title_contains(search_query))

    amount_results = browser.find_element(By.ID, "result-stats").text
    num_results = int(amount_results.split()[1].replace(',', ''))
    search_results = browser.find_elements(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/div/a/h3')

    link_elements = browser.find_elements(By.XPATH, '//a[@class="l"]')
    links = [element.get_attribute('href') for element in link_elements]

    string = [result.text for result in search_results]
    generate_json_report(links, string, num_results, search_query)


def generate_json_report(links: list, string: list, num_results: int, search_query: str):
    report = {
        'links': links,
        'first_search_result': string[0],
        'is_first_search_result_contains_query': search_query in string,
        'num_results': num_results,
        'is_num_results_greater_than_1000': num_results > 1000,
    }
    with open('report.json', 'w') as f:
        json.dump(report, f, indent=4)
