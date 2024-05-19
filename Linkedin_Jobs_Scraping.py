import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import pytz
import time
import csv
import yaml

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")
options.headless = True


def get_url(position, location):
    source = 'https://www.linkedin.com/jobs/search?keywords={}&location={}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    url = source.format(position, location)
    return url

def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'}

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    scroll_pause_time = 20
    last_height = driver.execute_script("return document.body.scrollHeight")

    records = []

    try:
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    except:
        pass

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    divs = soup.find_all('div', 'base-search-card__info')
    all_job_link = soup.find_all('a', class_='base-card__full-link')

    for item1, item2 in zip(divs, all_job_link):
        records.append(get_data(item1, item2))

    driver.quit()

    print(len(records), "jobs scraped.")
    return records

def get_data(div, link):
    job_link = link.get('href')
    job_title = div.h3.text.strip()
    try:
        company_name = div.find('a', 'hidden-nested-link').text.strip()
    except AttributeError:
        company_name = ''

    job_location = div.find('span', 'job-search-card__location').text.strip()

    try:
        salary_element = div.find('span', 'job-search-card__salary-info').text.replace('\n', '').strip()
        job_salary = ''.join(salary_element.split())
    except AttributeError:
        job_salary = 'Salary information is not available'

    try:
        status = div.find('span', 'result-benefits__text').text.strip()
    except AttributeError:
        status = 'Not updated'

    post_date = div.find('time').get('datetime')
    post_date_tag = div.find('time')
    if post_date_tag:
        exact_time = post_date_tag.get_text(strip=True)
    else:
        print("Time not available")

    local_tm = pytz.timezone('Asia/Kolkata')
    today = datetime.now(local_tm).strftime('%Y-%m-%d')

    record = (job_title, company_name, job_location, job_link, job_salary, status, post_date, exact_time, today)
    return record

if __name__ == '__main__':
    with open("config.yaml") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        position = cfg['POSITION']
        location = cfg['LOCATION']
        URL = get_url(position, location)
        records = main(URL)  
        csv_file_path = 'linkedin_job_records.csv'
        column_names = ['Job Title', 'Company', 'Location', 'Link', 'Salary', 'Status', 'Post Date', 'Exact Time', 'Today Date']
                    
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(column_names)
            writer.writerows(records)

        print(f"CSV file '{csv_file_path}' created successfully.")