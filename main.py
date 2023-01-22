from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook, load_workbook
from datetime import date
from configparser import ConfigParser
import logging


# Config
config = ConfigParser()
config.read("JobAdvertScraper_config.ini")

# Creating Excel File
wb = Workbook()
ws = wb.active
ws.title = 'Jobs from Pracuj.pl'

# Actual Date
today = date.today()
date_text_month = today.strftime("%d %B %Y")

# Logger
logger = logging.getLogger("JobAdvertScraper")
logging.basicConfig(level=logging.INFO)
log_filename = 'logfile_{}.log'.format(date_text_month)


file_handler = logging.FileHandler(log_filename)
formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)


#jobs = soup.find_all('div', class_='ceqyuft')

print("###################### SCRAPER STARTING EXECUTION ######################")
logger.info("###################### SCRAPER STARTING EXECUTION ######################")
# Scraper

try:
    html_text = requests.get('https://www.pracuj.pl/praca/programista;kw').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div', class_='c1dwhfs6')
    ws.append(['Job title', 'Seniority', 'Company name'])
    for job in jobs:
        job_title = job.find('h2', class_='tu9xzpe').text
        seniority = job.find('li', class_='iq8b4w2').text
        company_name = job.find('div', class_='text-wrapper wws23ky').text
        company_url = job.a['href']
        ws.append([job_title, seniority, company_name])
        # test = jobs.find(attrs={'class': 'brgvnzp'})
        # print(soup.find_all(attrs={'class': 'brgvnzp'}))
        # test = jobs.find('p', class_ = 'brgvnzp.t1c1o3wg')text
        print(job_title)
        print(seniority)
        print(company_name)
        print(company_url)
    #print(test.text)
    wb.save('jobs {}.xlsx'.format(date_text_month))
    #for job in jobs:
except:
    logger.critical("CRITICAL ERROR OCCURED")

print("###################### SCRAPER EXECUTION ENDED ######################")
logger.info("###################### SCRAPER EXECUTION ENDED ######################")