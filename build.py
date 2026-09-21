#!/usr/bin/env python3
"""Generates the static site pages from shared header/footer + per-page content.
Run: python3 build.py
"""
import os

PAGES = [
    ("index.html", "Home", "/"),
    ("vehicles.html", "Vehicles", "/vehicles.html"),
    ("real-estate.html", "Real Estate", "/real-estate.html"),
    ("other-assets.html", "Other Assets", "/other-assets.html"),
    ("formation.html", "Formation Guide", "/formation.html"),
    ("risks-faq.html", "Risks & FAQ", "/risks-faq.html"),
    ("contact.html", "Contact", "/contact.html"),
]

SITE_NAME = "Ledger &amp; Title"
SITE_TAGLINE = "A field guide to buying through your LLC"

ICON_SUN = '''<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M4.6 4.6l1.7 1.7M17.7 17.7l1.7 1.7M2.5 12h2.4M19.1 12h2.4M4.6 19.4l1.7-1.7M17.7 6.3l1.7-1.7" stroke-linecap="round"/></svg>'''
ICON_MOON = '''<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.8 6.8 0 0 0 10.5 10.5Z" stroke-linejoin="round"/></svg>'''
ICON_MENU = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h16" stroke-linecap="round"/></svg>'''


def nav_links(active_href):
    items = []
    for fname, label, href in PAGES:
        current = ' aria-current="page"' if href == active_href else ""
        items.append(f'<a href="{fname}"{current}>{label}</a>')
    return "\n        ".join(items)


def header(active_href):
    return f'''  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html">
        <span class="brand-mark" aria-hidden="true"></span>
        {SITE_NAME}
      </a>
      <button class="nav-toggle" type="button" data-nav-toggle aria-label="Toggle navigation" aria-expanded="false">
        {ICON_MENU}
      </button>
      <nav class="primary-nav" aria-label="Primary">
        {nav_links(active_href)}
      </nav>
      <div class="header-controls">
        <div class="font-size-control" role="group" aria-label="Text size">
          <button type="button" data-font-dec aria-label="Decrease text size">A&minus;</button>
          <button type="button" data-font-reset aria-label="Reset text size">A</button>
          <button type="button" data-font-inc aria-label="Increase text size">A&plus;</button>
        </div>
        <button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch to dark mode" aria-pressed="false">
          {ICON_SUN}
          {ICON_MOON}
        </button>
      </div>
    </div>
  </header>'''


FOOTER = f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">{SITE_NAME}</div>
          <p>An independent guide to titling vehicles, real estate, and other major purchases in a business entity's name instead of your own. Built for owners doing their own research before they talk to a professional.</p>
        </div>
        <div>
          <h4>Guide</h4>
          <ul>
            <li><a href="vehicles.html">Vehicles</a></li>
            <li><a href="real-estate.html">Real estate</a></li>
            <li><a href="other-assets.html">Other assets</a></li>
            <li><a href="formation.html">Formation steps</a></li>
          </ul>
        </div>
        <div>
          <h4>Know before you buy</h4>
          <ul>
            <li><a href="risks-faq.html">Risks &amp; FAQ</a></li>
            <li><a href="risks-faq.html#liability">Liability limits</a></li>
            <li><a href="risks-faq.html#disclaimer">Disclaimer</a></li>
          </ul>
        </div>
        <div>
          <h4>Work with Lamar</h4>
          <ul>
            <li><a href="mailto:ai.agent.lamar@gmail.com">ai.agent.lamar@gmail.com</a></li>
            <li><a href="https://linkedin.com/in/lamar-myers-ai" target="_blank" rel="noopener">linkedin.com/in/lamar-myers-ai</a></li>
            <li><a href="contact.html">Contact page</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 {SITE_NAME}. Independent educational resource, built by Lamar Myers.</span>
        <span class="footer-disclaimer">Not legal, tax, or financial advice &mdash; see the disclaimer.</span>
      </div>
    </div>
  </footer>
  <script src="js/script.js"></script>'''


def page(active_href, title, description, body):
    href = active_href
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · {SITE_NAME}</title>
<meta name="description" content="{description}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2224%22 fill=%22%230d6e78%22/><text x=%2250%22 y=%2266%22 font-size=%2258%22 text-anchor=%22middle%22 fill=%22%23a8ecd9%22 font-family=%22Georgia,serif%22>&amp;</text></svg>">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{header(href)}
{body}
{FOOTER}
</body>
</html>
'''


def write(fname, html):
    out_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname)
