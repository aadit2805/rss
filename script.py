#!/Users/aaditshah/Documents/code/projects/rss/.venv/bin/python3
import feedparser
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv('KEY')
SUBREDDIT = os.getenv('SUBREDDIT')

client = OpenAI(api_key=KEY)

def get_feed(subreddit):
    feed_url = f'https://www.reddit.com/r/{subreddit}/top/.rss'
    feed = feedparser.parse(feed_url)
    return feed

def summarize(feed, client):
    titles = [entry.title for entry in feed.entries]
    text = " ".join(titles)
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Give me a summary of this subreddit's RSS feed: {text}",
        max_tokens=3500)
    return response.choices[0].text.strip()

def main():
    feed = get_feed(SUBREDDIT)
    summary = summarize(feed, client)
    print("Summary of the Subreddit RSS Feed:\n" + summary)


main()
