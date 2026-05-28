import requests
import feedparser
from datetime import datetime

def main():
    feeds = [
        'https://news.google.com/rss?hl=en-ZA&gl=ZA&ceid=ZA:en',  # South Africa
        'https://techcrunch.com/feed/'
    ]
    report = f'# Daily Automation Digest - {datetime.now().date()}\n\n'
    for url in feeds:
        try:
            feed = feedparser.parse(url)
            report += f'## {feed.feed.get("title", "Feed")}\n'
            for entry in feed.entries[:5]:
                report += f'- [{entry.title}]({entry.link})\n'
        except:
            report += '## Error fetching feed\n'
    with open('reports/daily_digest.md', 'w', encoding='utf-8') as f:
        f.write(report)
    print('News digest completed.')

if __name__ == "__main__":
    main()