import os
from typing import Optional

from app.database.connection import engine
from app.database.models import Base
from app.database.repository import Repository
from app.scrapers.anthropic import AnthropicScraper
from app.scrapers.openai import OpenAIScraper
from app.scrapers.youtube import YouTubeScraper


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def scrape_and_store(hours: int = 168, youtube_channel_id: Optional[str] = None) -> dict:
    init_db()

    repo = Repository()
    openai_scraper = OpenAIScraper()
    anthropic_scraper = AnthropicScraper()
    youtube_scraper = YouTubeScraper()

    effective_hours = max(hours, 168)
    openai_articles = openai_scraper.get_articles(hours=effective_hours)
    anthropic_articles = anthropic_scraper.get_articles(hours=effective_hours)

    openai_count = repo.bulk_create_openai_articles([
        {
            "guid": article.guid,
            "title": article.title,
            "url": article.url,
            "published_at": article.published_at,
            "description": article.description,
            "category": article.category,
        }
        for article in openai_articles
    ])

    anthropic_count = repo.bulk_create_anthropic_articles([
        {
            "guid": article.guid,
            "title": article.title,
            "url": article.url,
            "published_at": article.published_at,
            "description": article.description,
            "category": article.category,
        }
        for article in anthropic_articles
    ])

    youtube_channel_id = youtube_channel_id or os.getenv("YOUTUBE_CHANNEL_ID")
    youtube_count = 0
    if youtube_channel_id:
        videos = youtube_scraper.scrape_channel(youtube_channel_id, hours=effective_hours)
        youtube_count = repo.bulk_create_youtube_videos([
            {
                "video_id": video.video_id,
                "title": video.title,
                "url": video.url,
                "channel_id": youtube_channel_id,
                "published_at": video.published_at,
                "description": video.description,
                "transcript": video.transcript,
            }
            for video in videos
        ])

    return {
        "openai_articles": openai_count,
        "anthropic_articles": anthropic_count,
        "youtube_videos": youtube_count,
    }


def main() -> None:
    result = scrape_and_store()
    print("Scraping completed")
    print(result)


if __name__ == "__main__":
    main()
