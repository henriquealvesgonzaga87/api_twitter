import tweepy
from secrets import *
from typing import Any, Dict, List


def get_trends(woe_id: int) -> List[Dict[str, Any]]:

    auth = tweepy.OAuthHandler(api_key=API_KEY, api_key_secret=API_KEY_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = api.trends_place(woe_id)

    return trends[0]["trends"]
