# LinkedIn Job Scrapping

## Overview

This project is a web scraper designed to extract job listings for Data Analyst positions from LinkedIn. It utilizes Python along with libraries such as BeautifulSoup and Selenium for web scraping. The scraped data is then stored in a CSV file for further analysis.

## Objective

The main objective of this project is to provide a tool for job seekers interested in Data Analyst positions to easily access and organize job listings from LinkedIn. It aims to streamline the job searching process by automating the collection of relevant job data.

## Features

- Scrapes job listings for Data Analyst positions from LinkedIn.
- Extracts key information such as job title, company, location, salary, etc.
- Stores the scraped data in a CSV file for easy access and analysis.

## Technologies Used

- Python: Main programming language used for development.
- BeautifulSoup: Python library for web scraping.
- Selenium: Python library for automating web browser interaction.
- ChromeDriver: WebDriver tool for controlling web browsers.
- Pytz: Python library for working with timezones.

## Outcomes

- Successfully scraped job listings for Data Analyst positions from LinkedIn.
- Extracted key information such as job title, company, location, salary, etc.
- Stored the scraped data in a CSV file for further analysis and reference.

## Future Use

Potential future uses of this project include:
- Adding additional features such as email notifications for new job listings.
- Integrating with other job search platforms to expand the scope of job listings.
- Implementing advanced filtering options for refining search results.

## Usage

To use this scraper, follow these steps:
1. Install the required Python libraries mentioned in the `requirements.txt` file.
2. Ensure you have Chrome browser installed on your system.
3. Update the `config.yaml` file with your desired position and location.
4. Run the `main.py` script to start scraping job listings.
5. The scraped data will be saved in a CSV file named `linkedin_job_records.csv`.
