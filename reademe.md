# WhoKnows

WhoKnows is a simple tool for retrieving domain information. It allows you to quickly gather essential data about any domain, making it ideal for network administrators, cybersecurity analysts, and anyone interested in domain analysis.

## Features

- Performs banner grabbing to extract basic information about the website.
- Retrieves WHOIS details for registrar, registrant, admin, and tech contacts.
- Conducts DNS queries for A, AAAA, MX, SOA, NS, and TXT records.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/JatinChopra/whoknows.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory:

   ```
   cd whoknows
   ```

2. Run the tool with the domain you want to analyze:

   ```
   python whoknows.py
   ```

3. Follow the on-screen instructions to enter the domain name.

4. Sit back and let WhoKnows gather the domain information for you!



## Contributing

Contributions are welcome! Please feel free to submit any issues or pull requests.

## Acknowledgments

- Thanks to [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for providing a simple API for HTML parsing.
- Thanks to [Python-whois](https://pypi.org/project/python-whois/) for providing WHOIS querying capabilities in Python.
