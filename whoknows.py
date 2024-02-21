import requests
from bs4 import BeautifulSoup
import socket
import subprocess
import re
import json

# domain info banner grabber

def get_title_and_url(domain):
    try:
        # Resolve domain to IP address
        ip_address = socket.gethostbyname(domain)

        # Fetch page content
        response = requests.get(f"http://{domain}")

        # Extract title and URL
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            url = response.url
        else:
            title = "No title found"
            url = f"http://{domain}"
        
        # Extract location address and tech info from response headers
        location_address = response.headers.get('Location', 'N/A')
        tech_info = response.headers.get('Server', 'N/A')

        scheme = url.split(":")[0]
        port = 80
        if(scheme == "https"):
            port = 443

        return {
            "title": title,
            "url": url,
            "port":port,
            "ip_address": ip_address,
            "status_code": response.status_code,
            "location_address": location_address,
            "tech_info": tech_info
        }
    except Exception as e:
        return {"error": f"Error occurred: {str(e)}"}

# who is data

def run_whois(domain):
    whois_output = subprocess.check_output(['whois', domain], text=True)
    return whois_output

def parse_whois_output(whois_output):
    registrar_info = {}
    registrant_info = {}
    admin_info = {}
    tech_info = {}

    # Regular expressions to match relevant information
    registrar_pattern = r'Registrar (.*?): (.*?)\n'
    registrant_pattern = r'Registrant (.*?): (.*?)\n'
    admin_pattern = r'Admin (.*?): (.*?)\n'
    tech_pattern = r'Tech (.*?): (.*?)\n'

    # Extract registrar information
    registrar_matches = re.findall(registrar_pattern, whois_output)
    for match in registrar_matches:
        key = match[0].strip()
        value = match[1].strip()
        registrar_info[key] = value

    # Extract registrant information
    registrant_matches = re.findall(registrant_pattern, whois_output)
    for match in registrant_matches:
        key = match[0].strip()
        value = match[1].strip()
        registrant_info[key] = value

    # Extract admin information
    admin_matches = re.findall(admin_pattern, whois_output)
    for match in admin_matches:
        key = match[0].strip()
        value = match[1].strip()
        admin_info[key] = value

    # Extract tech information
    tech_matches = re.findall(tech_pattern, whois_output)
    for match in tech_matches:
        key = match[0].strip()
        value = match[1].strip()
        tech_info[key] = value

    return {
        "Registrar": registrar_info,
        "Registrant": registrant_info,
        "Admin": admin_info,
        "Tech": tech_info
    }

# dig data

def parse_answer_section(output):
    records = {"A": [], "AAAA": [], "MX": [], "SOA": [], "TXT": [], "NS": set()}  # Using a set for NS to filter duplicates
    lines = output.split('\n')
    for line in lines:
        if line.strip():
            parts = line.split()
            if len(parts) >= 5:
                record_type = parts[3]
                if record_type in records:
                    if record_type == "MX":
                        records[record_type].append({"address": parts[5], "priority": parts[4]})
                    elif record_type == "SOA":
                        records[record_type].append({"primary_ns": parts[4], "responsible_party_email": parts[5], "serial_number": parts[6]})
                    elif record_type == "TXT":
                        records[record_type].append(parts[4].replace("\\", "").replace('"', ''))
                    elif record_type == "NS":
                        records[record_type].add(parts[4])  # Adding NS record to set to filter duplicates
                    else:
                        records[record_type].append(parts[4])

    return records

def run_dig_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode()


def fetchDetails(domain):
    try:
    
        result = get_title_and_url(domain)

        # Run whois command to retrieve information about the domain
        whois_output = run_whois(domain)

        # Parse the whois output
        parsed_data = parse_whois_output(whois_output)


        # for dig command 

        commands = [
            f"dig A {domain}",
            f"dig AAAA {domain}",
            f"dig MX {domain}",
            f"dig SOA {domain}",
            f"dig TXT {domain}",
            f"dig NS {domain}",
        ]
        
        all_records = {}
        
        for command in commands:
            output = run_dig_command(command)
            records = parse_answer_section(output)
            for key, value in records.items():
                all_records.setdefault(key, []).extend(value)
        
        # Filter out duplicates from NS records
        #all_records["NS"] = list(all_records["NS"])

        #print(json.dumps(all_records, indent=4))
        filtered_ns = []
        filtered_a= []
        filtered_aaaa=[]
        for  ns in all_records["NS"] :
            if ns not in filtered_ns:
                filtered_ns.append(ns);
        for a in all_records['A'] :
            if a not in filtered_a:
                filtered_a.append(a);
        for aaaa in all_records['AAAA'] :
            if aaaa not in filtered_aaaa:
                filtered_aaaa.append(aaaa);
        

        all_records["NS"] = filtered_ns;
        all_records["A"] = filtered_a;
        all_records["AAAA"] = filtered_aaaa;


        response = {
            "domain_info":result,
            "whois_data" : parsed_data,
            "dig_data" : all_records
        }
        # print(result)
        # print("======")
        # print(parsed_data)
        # print("========")
        # print(all_records)
        return json.dumps(response);
        # print(json.dumps(response,indent=4));

    except Exception as err:
        print("Error:", err)




if __name__ == "__main__":
    domain = input("Enter domain: ").strip();

    try:
    
        result = get_title_and_url(domain)

        # Run whois command to retrieve information about the domain
        whois_output = run_whois(domain)

        # Parse the whois output
        parsed_data = parse_whois_output(whois_output)


        # for dig command 

        commands = [
            f"dig A {domain}",
            f"dig AAAA {domain}",
            f"dig MX {domain}",
            f"dig SOA {domain}",
            f"dig TXT {domain}",
            f"dig NS {domain}",
        ]
        
        all_records = {}
        
        for command in commands:
            output = run_dig_command(command)
            records = parse_answer_section(output)
            for key, value in records.items():
                all_records.setdefault(key, []).extend(value)
        
        # Filter out duplicates from NS records
        #all_records["NS"] = list(all_records["NS"])

        #print(json.dumps(all_records, indent=4))
        filtered_ns = []
        filtered_a= []
        filtered_aaaa=[]
        for  ns in all_records["NS"] :
            if ns not in filtered_ns:
                filtered_ns.append(ns);
        for a in all_records['A'] :
            if a not in filtered_a:
                filtered_a.append(a);
        for aaaa in all_records['AAAA'] :
            if aaaa not in filtered_aaaa:
                filtered_aaaa.append(aaaa);
        

        all_records["NS"] = filtered_ns;
        all_records["A"] = filtered_a;
        all_records["AAAA"] = filtered_aaaa;


        response = {
            "domain_info":result,
            "whois_data" : parsed_data,
            "dig_data" : all_records
        }
        # print(result)
        # print("======")
        # print(parsed_data)
        # print("========")
        # print(all_records)
        print(json.dumps(response));

    except Exception as err:
        print("Error:", err)

