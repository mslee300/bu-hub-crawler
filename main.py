import requests
from bs4 import BeautifulSoup
import csv

# URLs of all BU hub websites
URLS = ["https://www.bu.edu/hub/hub-courses/philosophical-aesthetic-and-historical-interpretation/",
        "https://www.bu.edu/hub/hub-courses/scientific-and-social-inquiry/",
        "https://www.bu.edu/hub/hub-courses/quantitative-reasoning/",
        "https://www.bu.edu/hub/hub-courses/diversity-civic-engagement-and-global-citizenship/",
        "https://www.bu.edu/hub/hub-courses/communication/",
        "https://www.bu.edu/hub/hub-courses/intellectual-toolkit/"]

# Iterate each URL
for i in range(len(URLS)):
    URL = URLS[i]
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml') # If this line causes an error, run 'pip install html5lib' or install html5lib
    unit_list = []   # a list to store units
    course_units = ''
    # Iterate all course cards with id "cf-couse-card"
    for row in soup.findAll('div', attrs = {'class':'cf-course-card'}):
      table = {} # Dictionary to store all values
      college = row.find('span', attrs = 'cf-course-college').text
      dept = row.find('span', attrs = 'cf-course-dept').text
      num = row.find('span', attrs = 'cf-course-number').text
      # Add course to the dictionary 'table'
      table['course'] = college + " " + dept + " " + num
      title = row.find('h3', attrs = 'bu_collapsible').text
      # Add title to the dictionary 'table'
      table['title'] = title
      units = row.find('ul', attrs = 'cf-hub-offerings')
      # Add courses 
      for li in units.find_all("li"):
        course_units += li.text + '&' # Use & to seperate the unit values
      table['units'] = course_units[:-1] # Add the units except the last '&' value
      course_units = ''
      # Add the final dictionary to unit_list
      unit_list.append(table)

    # Create a csv file and name it for its BU hub
    filename = f"{URL[35:-1]}.csv"
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['course','title','units'])
        w.writeheader()
        for unit in unit_list:
          w.writerow(unit)
          
#import pandas module
import pandas as pd
#read the csv file into a dataframe
csv_files = [
    "philosophical-aesthetic-and-historical-interpretation.csv",
    "scientific-and-social-inquiry.csv",
    "quantitative-reasoning.csv",
    "diversity-civic-engagement-and-global-citizenship.csv",
    "communication.csv",
    "intellectual-toolkit.csv"
    ]
df_append = pd.DataFrame()

#append all files together
for file in csv_files:
            df_temp = pd.read_csv(file)
            df_append = df_append.append(df_temp, ignore_index=True)
#Save the combined csv file to 'downloads'
df_append.to_csv('/Users/minseoklee/Downloads/Combined_files.csv')
          
