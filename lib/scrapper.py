import requests
from bs4 import BeautifulSoup

def scrape_news() -> dict:
    # Specify the URL you want to scrape
    url = 'https://www.myfxbook.com/forex-economic-calendar'

    # Make a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('tr', class_='economicCalendarRow')
        
        results = []
        
        # Print the extracted links
        for link in links:
            # if (link["data-ignore-row"] == True)
            cells = link.find_all('td', class_='calendarToggleCell')
            
            row = {}
            
            if len(cells) > 1:
                row['date'] = cells[0].get_text().strip()
                row['day'] = row['date'].split(",")[0].strip()
                row['time'] = row['date'].split(",")[1].strip()
                row['time_left'] = cells[1].get_text().strip()
                row['flag'] = cells[2].get_text().strip()
                row['pair'] = cells[3].get_text().strip()
                row['name'] = cells[4].get_text().strip()
                row['impact'] = cells[5].get_text().strip()
                row['previous'] = cells[6].get_text().strip()
                row['consensus'] = cells[7].get_text().strip()
                row['actual'] = cells[8].get_text().strip()
            results.append(row)    

        return results
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        