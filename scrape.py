import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser
from tabulate import tabulate

# Print header message
print("*******************************************")
print("*                                         *")
print("*      LinkedIn Scraper by 4a6f62          *")
print("*                                         *")
print("*******************************************")

# Load config file
config = ConfigParser()
config.read('linkedin.cfg')
username = config['LINKEDIN']['username']
password = config['LINKEDIN']['password']
api_key = config['HUNTERIO']['api_key']

# Get LinkedIn login page to retrieve CSRF token
session = requests.Session()
login_page = session.get('https://www.linkedin.com/login')
soup = BeautifulSoup(login_page.content, 'html.parser')
csrf_token = soup.find('input', {'name': 'loginCsrfParam'}).get('value')

# Login to LinkedIn
login_data = {
    'session_key': username,
    'session_password': password,
    'loginCsrfParam': csrf_token,
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.linkedin.com/',
}
login_response = session.post('https://www.linkedin.com/checkpoint/lg/login-submit', data=login_data, headers=headers)

# Check if login was successful
if 'Sign Out' not in login_response.text:
    print('Login failed')
    exit()

# Prompt user for search query
search_query = input('Enter company name to search for: ')

# Search for company on LinkedIn
search_url = f'https://www.linkedin.com/search/results/companies/?keywords={search_query}'
search_response = session.get(search_url)

# Get company page URL from search results
soup = BeautifulSoup(search_response.content, 'html.parser')
search_results = soup.find_all('a', {'class': 'app-aware-link', 'data-control-name': 'search_srp_result'})
if not search_results:
    print('No search results found')
    exit()
company_url = search_results[0]['href']

# Retrieve company page HTML
company_response = session.get(company_url)
soup = BeautifulSoup(company_response.content, 'html.parser')

# Extract company name and description
company_name = soup.find('h1', {'class': 'org-top-card-summary__title'}).text.strip()
company_description = soup.find('p', {'class': 'org-top-card-summary__description'}).text.strip()

# Use Hunter API to get email addresses
suffix = company_url.split('/')[-2]
url = f"https://api.hunter.io/v2/domain-search?domain={suffix}&api_key={api_key}"
r = requests.get(url)
content = r.json()
emails = []
if 'data' in content:
    for email in content['data']['emails']:
        emails.append(email['value'])

# Extract contact info from company page
contact_info = soup.find('section', {'class': 'org-page-details__contact-info'})
contact_info_dict = {}
if contact_info:
    contact_info_dict['Website'] = contact_info.find('a', {'class': 'org-page-details__website-link'})['href']
    contact_info_dict['Phone'] = contact_info.find('span', {'class': 'org-page-details__contact-info-item-icon'}).next_sibling.strip()
    for link in contact_info.find_all('a', {'class': 'org-page-details__email-link'}):
        if 'aria-label' in link.attrs:
            label = link['aria-label'].strip()
            if label.startswith('Email'):
                contact_info_dict['Email'] = link.text.strip()
                break

# Print results in table format
data = [['Company Name', company_name], ['Company Description', company_description], ['Emails', ', '.join(emails)]]
for key, value in contact_info_dict.items():
    data.append([key, value])

# Print table
print(tabulate(data, headers=['Field', 'Value']))

# Print legal notice
print("***************************************************")
print("*                                                 *")
print("*  DISCLAIMER: This script is for educational      *")
print("*  purposes only. The author is not responsible    *")
print("*  for any actions taken using this script.        *")
print("*                                                 *")
print("***************************************************")
