import requests
from configparser import ConfigParser
from tabulate import tabulate
from linkedin_api import Linkedin

# Print header message
print("*******************************************")
print("*                                         *")
print("*      LinkedIn Scraper by 4a6f62          *")
print("*                                         *")
print("*******************************************")

# Load config file
config = ConfigParser()
config.read('linkedin.cfg')
api_key = config.get('hunterio', 'api_key')
access_token = config.get('linkedin', 'access_token')
access_secret = config.get('linkedin', 'access_secret')

# Login to LinkedIn
api = Linkedin(access_token, access_secret)

# Prompt user for search query
search_query = input('Enter company name to search for: ')

# Search for company on LinkedIn
search_results = api.search_company(search_query)

# Get company page URL from search results
if not search_results:
    print('No search results found')
    exit()
company = search_results[0]

# Retrieve company page data
company_id = company['companyId']
company_data = api.get_company(company_id)

# Extract company name and description
company_name = company_data['basicCompany']['localizedName']
company_description = company_data['basicCompany']['description']

# Enrich data with Hunter API
suffix = company_data['basicCompany']['url'].split('/')[-2]
url = f"https://api.hunter.io/v2/domain-search?domain={suffix}&api_key={api_key}"
r = requests.get(url)
content = r.json()
emails = []
if 'data' in content:
    for email in content['data']['emails']:
        emails.append(email['value'])

# Extract contact info from company page
contact_info_dict = {}
if 'headquarters' in company_data:
    contact_info_dict['Website'] = company_data['headquarters']['website']
    contact_info_dict['Phone'] = company_data['headquarters']['phone']
    contact_info_dict['Email'] = company_data['headquarters']['email']

# Add enriched data to contact_info_dict
if emails:
    contact_info_dict['Emails'] = ', '.join(emails)

# Print results in table format
data = [['Company Name', company_name], ['Company Description', company_description]]
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
