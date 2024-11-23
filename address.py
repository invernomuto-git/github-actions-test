import requests

# Set the URL and headers for the API request
url = 'https://atip.piercecountywa.gov/api/salesSearch'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json',
    'Origin': 'https://atip.piercecountywa.gov',
    'Referer': 'https://atip.piercecountywa.gov/app/v2/salesSearch/search',
    'Cookie': 'wisepops=%7B%22popups%22%3A%7B%22210955%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1684632831159%2C%22c%22%3A1684632841876%7D%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A1%2C%22cid%22%3A%2246235%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%2C%22csd%22%3A1%7D; wisepops_visitor=%7B%22YSpHL5eMJs%22%3A%22d7df75e8-9345-4ef0-9f45-c797f7d509d2%22%7D; wisepops_visits=%5B%222024-11-12T00%3A34%3A29.353Z%22%2C%222024-10-21T22%3A20%3A52.309Z%22%2C%222024-09-26T03%3A14%3A47.444Z%22%2C%222024-09-26T03%3A14%3A03.157Z%22%2C%222024-09-26T03%3A12%3A27.366Z%22%2C%222024-09-13T18%3A03%3A37.443Z%22%2C%222024-09-13T18%3A03%3A30.681Z%22%2C%222024-09-13T18%3A03%3A17.800Z%22%2C%222024-09-09T21%3A28%3A37.330Z%22%2C%222024-08-19T04%3A55%3A08.047Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222024-11-12T00%3A34%3A29.353Z%22%2C%22mtime%22%3A1731371671066%2C%22pageviews%22%3A1%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22sticky%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D; SESSION=057ce568-fe35-42a3-8722-49c4ed3837eb',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

# Define the data payload
payload = {
    "parameterValue": "type=Both,salesdate=6mo,minx=1097113.58614769,miny=642458.5681671248,maxx=1220046.9194810234,maxy=769525.2348337915,salesreturned=100000"
}

# Make the POST request and process the response
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    # Parse JSON response
    data = response.json()

    # List of deed descriptions to exclude
    exclude_deeds = {"Statutory Warranty Deed", "Bill of Sale"}
    unique_addresses = set()

    # Extract and save unique deed descriptions and addresses
    for item in data.get("list", []):
        deed_desc = item.get("dEEDDESC")
        address = item.get("aCCOUNTADDRESS") or item.get("pRIMACCOUNTADDRESS")

        # Filter out excluded deeds and duplicate addresses
        if deed_desc and address and deed_desc not in exclude_deeds:
            unique_addresses.add(address)

    # Sort the addresses and write them to file
    sorted_addresses = sorted(unique_addresses)
    with open("pierce_addresses.txt", "w") as output_file:
        for address in sorted_addresses:
            output_file.write(f"{address}\n")

    print("Sorted unique addresses saved to pierce_addresses.txt")

except requests.exceptions.RequestException as e:
    print("Request failed:"), e
