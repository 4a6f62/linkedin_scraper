# LinkedIn Scraper

This is a Python script that uses the LinkedIn API and the Hunter.io API to retrieve employee information for a given company name. The script can retrieve employee name, job title, phone number, and email address, and outputs the information in a table format using the `tabulate` library.

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python packages using pip:
pip install -r requirements.txt


3. Obtain LinkedIn API access tokens and secrets:

- Go to the [LinkedIn Developer Portal](https://www.linkedin.com/developers/) and create a new app.
- Obtain an access token and secret by following the instructions [here](https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context).

**Note:** Keep your access token and secret private, and do not share them with anyone.

4. Obtain a Hunter.io API key:

- Go to the [Hunter.io website](https://hunter.io/) and sign up for an account.
- Obtain an API key from the [API settings](https://hunter.io/api_keys) page.

**Note:** Keep your API key private, and do not share it with anyone.

5. Create a `linkedin.cfg` file in the same directory as the Python script, and add your access tokens and API key:
[linkedin]
access_token = YOUR_ACCESS_TOKEN
access_secret = YOUR_ACCESS_SECRET

[hunter]
api_key = YOUR_HUNTER_API_KEY


Replace `YOUR_ACCESS_TOKEN`, `YOUR_ACCESS_SECRET`, and `YOUR_HUNTER_API_KEY` with your actual LinkedIn access token, LinkedIn access secret, and Hunter.io API key, respectively. Make sure there are no spaces around the equals sign (=) in each line. 

**Note:** Keep your `linkedin.cfg` file private, and do not share it with anyone.

## Usage

1. Run the script using the following command:

python scrape.py


2. Enter the company name you want to search for when prompted.

3. The script will retrieve employee information for the given company and display it in a table format.

**Legal Notice:** This script is provided for educational and research purposes only. The use of this script for any other purpose is strictly prohibited. The author of this script is not responsible for any actions taken by users of this script. Use at your own risk.```
