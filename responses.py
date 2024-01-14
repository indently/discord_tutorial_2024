from random import choice, randint
from economic_calendar import get_fomarted_news

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'news' in lowered:
        return get_fomarted_news()