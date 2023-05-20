import tweepy
from secrets import CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN_SECRET, ACCESS_TOKEN
from typing import Any, Dict, List


def get_trends(woe_id: int) -> List[Dict[str, Any]]:

    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = api.trends_place(woe_id)

    return [trend for trend in trends]
