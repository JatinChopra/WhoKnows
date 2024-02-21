# WhoKnows

WhoKnows is a simple tool for retrieving domain information. It allows you to quickly gather essential data about any domain, making it ideal for network administrators, cybersecurity analysts, and anyone interested in domain analysis.

## Features

- Performs banner grabbing to extract basic information about the website.
- Retrieves WHOIS details for registrar, registrant, admin, and tech contacts.
- Conducts DNS queries for A, AAAA, MX, SOA, NS, and TXT records.

## Installation

1. Clone the repository:

<<<<<<< HEAD
   ```bash
=======
   ```
>>>>>>> origin/main
   git clone https://github.com/JatinChopra/whoknows.git
   ```

2. Install the required dependencies:

<<<<<<< HEAD
   ```bash
=======
   ```
>>>>>>> origin/main
   pip install -r requirements.txt
   ```

## Usage

<<<<<<< HEAD
### Running the Script

1. Navigate to the project directory:

   ```bash
=======
1. Navigate to the project directory:

   ```
>>>>>>> origin/main
   cd whoknows
   ```

2. Run the tool with the domain you want to analyze:

<<<<<<< HEAD
   ```bash
=======
   ```
>>>>>>> origin/main
   python whoknows.py
   ```

3. Follow the on-screen instructions to enter the domain name.

<<<<<<< HEAD
### Importing the Function

Alternatively, you can import the `fetchDetails` function into your Python code and use it to retrieve domain details programmatically.

```python
from whoknows import fetchDetails

# Call the function and pass the domain name

domain_info = fetchDetails("example.com")

# Process the domain information as needed

print(domain_info)
```


## Output format 
The tool returns domain information in the following format:

{
  "domain_info": {
    "title": "string",                // The title of the website
    "url": "string",                  // The URL of the website
    "port": "integer",                // The port number used for the connection
    "ip_address": "string",           // The IPv4 address of the website
    "status_code": "integer",         // The HTTP status code of the website
    "location_address": "string",     // The physical location address of the website (if available)
    "tech_info": "string"             // Information about the technology stack used by the website (e.g., server, framework)
  },
  "whois_data": {
    "Registrar": {
      "[string]": "string",           // Key-value pairs for registrar information
      "WHOIS Server": "string",       // The WHOIS server used for domain registration information
      "URL": "string",                // The URL of the registrar's website
      "IANA ID": "string",            // The IANA ID of the registrar
      "Abuse Contact Email": "string",// The email address to report abuse to the registrar
      "Abuse Contact Phone": "string",// The phone number to report abuse to the registrar
      "Registration Expiration Date": "string" // The date when the domain registration expires
    },
    "Registrant": {
      "[string]": "string"            // Key-value pairs for registrant information
    },
    "Admin": {
      "[string]": "string"            // Key-value pairs for admin information
    },
    "Tech": {
      "[string]": "string"            // Key-value pairs for tech information
    }
  },
  "dig_data": {
    "A": ["string"],                   // List of IPv4 addresses associated with the domain
    "AAAA": ["string"],                // List of IPv6 addresses associated with the domain
    "MX": [
      {
        "address": "string",           // The mail exchange server address
        "priority": "integer"          // The priority of the mail exchange server
      }
    ],
    "SOA": [
      {
        "primary_ns": "string",        // The primary name server for the domain
        "responsible_party_email": "string", // The email address of the responsible party
        "serial_number": "string"      // The serial number of the SOA record
      }
    ],
    "TXT": ["string"],                 // List of TXT records associated with the domain
    "NS": ["string"]                   // List of name servers associated with the domain
  }
}
=======
4. Sit back and let WhoKnows gather the domain information for you!

>>>>>>> origin/main


## Contributing

Contributions are welcome! Please feel free to submit any issues or pull requests.

## Acknowledgments

- Thanks to [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for providing a simple API for HTML parsing.
<<<<<<< HEAD
- Thanks to [Python-whois](https://pypi.org/project/python-whois/) for providing WHOIS querying capabilities in Python.
=======
- Thanks to [Python-whois](https://pypi.org/project/python-whois/) for providing WHOIS querying capabilities in Python.
>>>>>>> origin/main
