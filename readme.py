import time

import feedparser

if __name__ == '__main__':
    URL = "http://waterfogsw.tistory.com/rss"
    RSS_FEED = feedparser.parse(URL)
    MAX_POST = 5

    markdown_text = """
**Interested In**
- Java, Kotlin, Spring, MySQL
- DDD, Clean Architecture, Classicist TDD
- FastAPI, Python, Open AI

**Latest Blog Post**

"""  # list of blog posts will be appended here

    for idx, feed in enumerate(RSS_FEED['entries']):
        if idx > MAX_POST:
            break
        if 'category' in feed:  # Check if the 'category' tag exists
            feed_date = feed['published_parsed']
            markdown_text += f"- [{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

    f = open("README.md", mode="w", encoding="utf-8")
    f.write(markdown_text)
    f.close()
