# LinkedIn Job Scrapping

## Overview
This project aims to provide a comprehensive tool for analyzing the job's market by scraping job listings from various online platforms and extracting key insights such as job titles, companies, locations, salaries, and more. By leveraging web scraping techniques and data analysis, this tool empowers professionals, job seekers, and recruiters to navigate the dynamic landscape of data science employment.

## Features
- **Web Scraping Mastery**: Utilizes Selenium and BeautifulSoup to efficiently gather job listings from platforms like LinkedIn, Indeed, Naukri, Glassdoor, and AngelList.
- **Data Symphony**: Cleanses and organizes extracted data, including job titles, company names, locations, salaries, and post dates.
- **Market Wizardry**: Analyzes trends in job demand, geographic distribution, salary variations, preferred qualifications, and emerging skill demands.
- **Visual Magic**: Presents insights through captivating charts, graphs, and visual representations to aid user understanding.

## Usage
1. **Setup**:
   - Ensure necessary packages are installed by following the installation instructions provided in the code.
   - Customize web scraping parameters like job position and location in the `get_url()` function.
2. **Scraping Data**:
   - Execute the main script to scrape job data from selected online platforms.
   - Data will be saved to a CSV file (`linkedin_job_records.csv`).
3. **Data Analysis**:
   - Import the CSV file into a DataFrame and perform data cleaning and analysis using provided scripts.
   - Extract insights such as job count by location, average salary, most in-demand job titles, etc.
4. **Visualization**:
   - Utilize matplotlib and seaborn libraries to create visual representations of analyzed data for easier interpretation.
   
## Sample Outputs
1. **Job Count by Location**:
   ![Job Count by Location](images/job_count_by_location.png)
2. **Salary Distribution by Job Title**:
   ![Salary Distribution by Job Title](images/salary_distribution.png)
3. **Locations with Highest Average Salary for Specific Job Type**:
   ![Locations with Highest Average Salary](images/highest_salary_locations.png)