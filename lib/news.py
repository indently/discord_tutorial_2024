from lib.emojis import get_emoji
from lib.storage import should_fetch_live_data, store_data, get_data
from lib.scrapper import scrape_news
from lib.utils import formart_date


def order_news_by_day(raw_news):
    ordered_news = {}
    
    for news in raw_news:
        
        if news['day'] not in ordered_news.keys():
            ordered_news[news['day']] = []
            
        ordered_news[news['day']].append(news)
    return ordered_news
 
def get_news_string(ordered_news, impact=['High']):
    news_string = ""
    
    for day in ordered_news.keys():   
        news_string += f"\n`{formart_date(day)}`\n"
        
        for news in ordered_news[day]: 
            if (news['impact'] in impact ):
                cleaned_name = ' '.join(news['name'].splitlines())
                news_string += f"{get_emoji(news['pair'])}   {news['time']}   **{cleaned_name}**\n"
                
    return news_string
    
def get_news() -> str:
    if should_fetch_live_data():
        print("[log] Fetching live data...")
        raw_news = scrape_news()
        store_data(raw_news)
    else: 
        print("[log] Using stored data...")
        raw_news = get_data()
    
    ordered_news = order_news_by_day(raw_news)
    news_string = get_news_string(ordered_news)
        
    return news_string