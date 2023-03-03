import configparser
import linkedin_api
from tabulate import tabulate
import hunterio

# Read the access token and secret from the configuration file
config = configparser.ConfigParser()
config.read('linkedin.cfg')
access_token = config.get('linkedin', 'access_token')
access_secret = config.get('linkedin', 'access_secret')
hunter_api_key = config.get('hunter', 'api_key')

# Authenticate with the LinkedIn API using your access token and secret key
linkedin = linkedin_api.Linkedin(access_token=access_token, access_secret=access_secret)

# Initialize the Hunter.io client with your API key
hunter = hunterio.Hunterio(hunter_api_key)

# Print header message
print("*******************************************")
print("*                                         *")
print("*      LinkedIn Scraper by 4a6f62          *")
print("*                                         *")
print("*******************************************")

# Prompt user for company search query
search_query = input("Enter the company name to search: ")

# Search for the company by its name
company = linkedin.search_company(search_query)

# Get a list of the company's employees
employees = linkedin.search_people(company)

# Create a list of dictionaries to hold the employee information
employee_info = []
for employee in employees:
    name = employee.name
    function = employee.function
    phone_number = employee.phone_number

    # Use the Hunter.io API to look up the employee's email address
    hunter_result = hunter.email_finder(domain=company.website, full_name=name)

    # Extract the email address from the Hunter.io result
    email = hunter_result['data']['email']

    # Add the employee information to the list
    employee_info.append({'Name': name, 'Function': function, 'Email': email, 'Phone Number': phone_number})

# Format the employee information as a table using the tabulate library
table_headers = ['Name', 'Function', 'Email', 'Phone Number']
table = tabulate(employee_info, headers=table_headers)

# Print the table
print(table)

# Print legal notice
print("***************************************************")
print("*                                                 *")
print("*  DISCLAIMER: This script is for educational      *")
print("*  purposes only. The author is not responsible    *")
print("*  for any actions taken using this script.        *")
print("*                                                 *")
print("***************************************************")
