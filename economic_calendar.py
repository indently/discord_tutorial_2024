import requests
from bs4 import BeautifulSoup
from emojis import get_emoji


def scrape_news():
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
        
        
def formart_date(day):
    # day,time = date.split(",")
    from datetime import datetime
    
    date_string = f"{day} {datetime.now().year}"


    # Convert the original date string to a datetime object
    date_object = datetime.strptime(date_string, "%b %d %Y")

    # Format the datetime object to the desired output
    return date_object.strftime("%a %b %d")


    
            

def get_fomarted_news():
    news_object = scrape_news()
    
    news_string = ""
    
    formated_news_object = {}
    
    
    
    for news in news_object:
        
        if news['day'] not in formated_news_object.keys():
            formated_news_object[news['day']] = []
            
        formated_news_object[news['day']].append(news)

    for day in formated_news_object.keys():   
        news_string += f"\n`{formart_date(day)}`\n"
        
        for news in formated_news_object[day]: 
            if (news['impact'] == 'High'):
                cleaned_name = ' '.join(news['name'].splitlines())
                news_string += f"{get_emoji(news['pair'])}   {news['time']}   **{cleaned_name}**\n"
        
    return news_string