from random import choice, randint
from lib.news import get_news

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'news' in lowered:
        return get_news()