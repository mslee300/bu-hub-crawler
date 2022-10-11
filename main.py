import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.bu.edu/hub/hub-courses/philosophical-aesthetic-and-historical-interpretation/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

for row in soup.findAll('div', attrs = {'class':'cf-course-card'}):
  table = {}
  college = row.find('span', attrs = 'cf-course-college').text
  dept = row.find('span', attrs = 'cf-course-dept').text
  num = row.find('span', attrs = 'cf-course-number').text
  title = row.find('h3', attrs = 'bu_collapsible').text
  units = row.find('ul', attrs = 'cf-hub-offerings')
  print(f"{college} {dept} {num}: {title}")
  for li in units.find_all("li"):
    print(li.text)
  print("")


# for row in table.findAll('div',
#                          attrs = {'class':'cf-course-id'}):
                           
#     unit = {}
#     unit['theme'] = row.h5.text
#     unit['url'] = row.a['href']
#     unit['img'] = row.img['src']
#     unit['lines'] = row.img['alt'].split(" #")[0]
#     unit['author'] = row.img['alt'].split(" #")[1]
#     unit.append(unit)
   
# filename = 'inspirational_quotes.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['theme','url','img','lines','author'])
#     w.writeheader()
#     for quote in units:
#         w.writerow(quote)