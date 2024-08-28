import requests
from bs4 import BeautifulSoup


url = "https://github.com/SimplifyJobs/Summer2025-Internships"
r = requests.get(url)
if r.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')
else:
    print("Failed to retrieve the page. Status code:", r.status_code)

soup = BeautifulSoup(r.text, "lxml")
tables = soup.find_all('table')
for table in tables:
    thead = table.find('thead')
    if thead:
        links = table.find_all('a')

if table:
    tr_tags = table.find_all('tr')
    previous_company = None

    for tr in tr_tags:
        td_tags = tr.find_all('td')  # Find all <td> tags within the current <tr> tag

        strong_tag = tr.find("strong")
        if strong_tag:
            # If <strong> tag is found, extract company name
            company_name = strong_tag.get_text(strip=True)
            print("Company:", company_name)
            previous_company = company_name
        else:
            for index, td in enumerate(td_tags):
                if index == 0:
                    if td.get_text(strip=True) == "↳":
                        company = previous_company
                    else:
                        company = td.get_text(strip=True)
                    print("Company:", company)
                    previous_company = company

        for index, td in enumerate(td_tags):
            if index == 1:
                position = td.get_text(strip=True)
                print("Position:", position)

            if index == 2:
                location = td.get_text(strip=True)
                print("Location:", location)

            if index == 3:
                link_tag = td.find('a')
                if link_tag:
                    link = link_tag.get('href', '')
                    print("Link:", link)
                else:
                    print("Link: Link locked")

            if index == 4:
                date_posted = td.get_text(strip=True)
                print("Date_posted:", date_posted)
                print()

