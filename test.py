from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome('/path/to/chromedriver')

profile_urls = [
  'https://twitter.com/BarackObama',
  'https://twitter.com/justinbieber',
]

with open('output.csv', 'w', newline='') as csvfile:

  writer = csv.writer(csvfile)
  writer.writerow(['Name', 'Username', 'Bio', 'Location', 'Profile URL'])

  for url in profile_urls:
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    name = soup.find('li', {'class': 'ProfileHeaderCard-nameLink u-textInheritColor js-nav'}).text.strip()
    username = soup.find('h2', {'class': 'ProfileHeaderCard-screennameLink u-linkComplex js-nav'}).text.strip()
    bio = soup.find('section', {'class': 'ProfileHeaderCard-bio u-dir'}).text.strip()
    location = soup.find('span', {'class': 'ProfileHeaderCard-locationText u-dir'}).text.strip()
print('Name: {}'.format(name))
print('Username: {}'.format(username))
print('Bio: {}'.format(bio))
print('Location: {}'.format(location))
