# LinkedIn Company Scraper
This is a Python script for scraping company information from LinkedIn, enriching it with the Hunter API, and displaying it in a table format.  

## Usage
1. Clone the repository to your local machine.
2. Install the required packages with `pip install -r requirements.txt`.
3. Obtain LinkedIn API access tokens and secrets:
- Go to the [LinkedIn Developer Portal](https://www.linkedin.com/developers/) and create a new app.
- Obtain an access token and secret by following the instructions [here](https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context).  

**Note:** Keep your access token and secret private, and do not share them with anyone.

4. Obtain a Hunter.io API key:
- Go to the [Hunter.io website](https://hunter.io/) and sign up for an account.
- Obtain an API key from the [API settings](https://hunter.io/api_keys) page.  

**Note:** Keep your API key private, and do not share it with anyone.

5. Create a `linkedin.cfg` file with your LinkedIn and Hunter API keys. The file should be in the following format:  

[linkedin]
access_token = YOUR_ACCESS_TOKEN
access_secret = YOUR_ACCESS_SECRET  

[hunterio]
api_key = YOUR_API_KEY

6. Run the script with `python linkedin_scraper.py`.
7. Enter the name of the company you want to search for.
8. The script will display the company name, description, and contact information in a table format.  

## Legal Notice
This script is for educational purposes only. The author is not responsible for any actions taken using this script.