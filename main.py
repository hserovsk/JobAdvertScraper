from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook, load_workbook
from datetime import date

html_text = requests.get('https://www.pracuj.pl/praca/programista;kw').text
soup = BeautifulSoup(html_text, 'lxml')
wb = Workbook()
ws = wb.active
ws.title = 'Jobs from Pracuj.pl'
today = date.today()
date_text_month = today.strftime("%d %B %Y")

#jobs = soup.find_all('div', class_='ceqyuft')

print('test')
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
