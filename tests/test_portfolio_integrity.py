"""Standard-library smoke tests for the static GitHub Pages portfolio."""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Extract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = []
        self.lang_controls = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.append(d["id"])
        if tag in {"a", "link", "script", "img"}:
            attr = "href" if tag in {"a", "link"} else "src"
            if d.get(attr):
                self.links.append(d[attr])
        if "data-lang" in d:
            self.lang_controls.append(d["data-lang"])

class PortfolioIntegrity(unittest.TestCase):
    def test_local_html_links_resolve(self):
        for file in ROOT.rglob("*.html"):
            if ".git" in file.parts:
                continue
            with self.subTest(file=str(file.relative_to(ROOT))):
                parser = Extract()
                parser.feed(file.read_text(encoding="utf-8"))
                self.assertEqual(len(parser.ids), len(set(parser.ids)), "Duplicate HTML IDs")
                for href in parser.links:
                    url = urlsplit(href)
                    if url.scheme or url.netloc or href.startswith(("#", "//", "mailto:", "tel:")):
                        continue
                    if url.path.startswith("/"):
                        continue  # deployment-root links need a running server
                    target = (file.parent / unquote(url.path)).resolve() if url.path else file
                    self.assertTrue(target.is_relative_to(ROOT), f"Path escapes repository: {href}")
                    if target.is_dir():
                        target /= "index.html"
                    self.assertTrue(target.is_file(), f"Broken local link in {file}: {href}")
    def test_portfolio_language_and_project_cards(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        parser = Extract()
        parser.feed(html)
        self.assertIn("fr", parser.lang_controls)
        self.assertIn("en", parser.lang_controls)
        for project in ("trafficflow-ai/", "smart-attendance/", "arabic-learning-game/", "nfc-digital-card/"):
            self.assertIn('href="' + project + '"', html)
        self.assertIn("Object.assign(translations,", html)
        self.assertIn("Full catalog, documentation and source status", html)
    def test_demo_pages_have_accessible_titles(self):
        for folder in ("trafficflow-ai", "smart-attendance", "arabic-learning-game", "nfc-digital-card"):
            html = (ROOT / folder / "index.html").read_text(encoding="utf-8")
            self.assertRegex(html, r"(?is)<title>.+?</title>")

if __name__ == "__main__":
    unittest.main()
