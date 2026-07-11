import unittest

from app.scrapers.anthropic import AnthropicScraper


class AnthropicScraperImportTest(unittest.TestCase):
    def test_import_and_instantiation(self):
        scraper = AnthropicScraper()
        self.assertIsInstance(scraper, AnthropicScraper)


if __name__ == "__main__":
    unittest.main()
