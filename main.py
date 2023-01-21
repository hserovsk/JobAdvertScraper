from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.pracuj.pl/praca/programista;kw').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'ceqyuft')
for job in jobs:
    job_title = job.find('h2', class_ = 'tu9xzpe').text
    seniority = job.find('li', class_ = 'iq8b4w2').text
    company_name = job.find('div', class_ = 'text-wrapper wws23ky').text
    #test = jobs.find(attrs={'class': 'brgvnzp'})
    #print(soup.find_all(attrs={'class': 'brgvnzp'}))
    #test = jobs.find('p', class_ = 'brgvnzp.t1c1o3wg')text
    print(job_title)
    print(seniority)
    print(company_name)
#print(test.text)
#for job in jobs:
