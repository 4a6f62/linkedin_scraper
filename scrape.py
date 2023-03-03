import requests
from bs4 import BeautifulSoup

# Print header message
print("*******************************************")
print("*                                         *")
print("*      LinkedIn Scraper by 4a6f62          *")
print("*                                         *")
print("*******************************************")

# Read config file for LinkedIn credentials and Hunter.io API key
config = {}
with open('linkedin.cfg, 'r') as f:
    for line in f:
        key, value = line.strip().split('=')
        config[key] = value

# Set up LinkedIn login session
login_url = 'https://www.linkedin.com/uas/login-submit'
client = requests.Session()
html = client.get('https://www.linkedin.com/')
soup = BeautifulSoup(html.content, 'html.parser')
csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')
login_information = {
    'session_key': config['LINKEDIN_USERNAME'],
    'session_password': config['LINKEDIN_PASSWORD'],
    'loginCsrfParam': csrf,
}
client.post(login_url, data=login_information)

# Get company search query from user
search_query = input('Enter the company name to search for: ')

# Perform search on LinkedIn
search_url = f'https://www.linkedin.com/search/results/people/?keywords={search_query}&origin=SWITCH_SEARCH_VERTICAL'
response = client.get(search_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Parse search results for name, position, and profile URL
results = soup.find_all('li', {'class': 'search-result search-result__occluded-item'})
for result in results:
    name = result.find('span', {'class': 'actor-name'}).get_text().strip()
    position = result.find('p', {'class': 'subline-level-1'}).get_text().strip()
    profile_url = result.find('a').get('href')

    # Get email and phone number using Hunter.io
    domain = profile_url.split('/')[4].split('?')[0]
    hunter_url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={config['HUNTER_API_KEY']}"
    hunter_response = requests.get(hunter_url)
    hunter_content = hunter_response.json()
    email = hunter_content['data']['emails'][0]['value'] if hunter_content['data']['emails'] else ''
    phone = hunter_content['data']['phones'][0]['value'] if hunter_content['data']['phones'] else ''

    # Print results
    print('Name:', name)
    print('Position:', position)
    print('Profile URL:', profile_url)
    print('Email:', email)
    print('Phone:', phone)
    print('--------------------------------------')

# Print legal notice
print("***************************************************")
print("*                                                 *")
print("*  DISCLAIMER: This script is for educational      *")
print("*  purposes only. The author is not responsible    *")
print("*  for any actions taken using this script.        *")
print("*                                                 *")
print("***************************************************")
