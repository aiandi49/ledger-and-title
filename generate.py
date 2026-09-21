import build
import content_index
import content_vehicles
import content_real_estate
import content_other_assets
import content_formation
import content_risks_faq
import content_contact

PAGES = [
    ("index.html", "Home", "/", "A plain-language guide to titling vehicles, real estate, and other major purchases under an LLC instead of your personal name.", content_index.BODY),
    ("vehicles.html", "Vehicles", "/vehicles.html", "How to title a vehicle to your LLC \u2014 transferring one you own, buying new through the business, insurance, and the tax factors that actually matter.", content_vehicles.BODY),
    ("real-estate.html", "Real Estate", "/real-estate.html", "How to close on real estate in an LLC's name, cash vs. commercial financing, and the 2026 FinCEN reporting rule for entity cash purchases.", content_real_estate.BODY),
    ("other-assets.html", "Other Assets", "/other-assets.html", "Buying boats, equipment, aircraft shares, and other big purchases through an LLC \u2014 cash routes vs. building real business credit.", content_other_assets.BODY),
    ("formation.html", "Formation Guide", "/formation.html", "The seven things to set up \u2014 state, EIN, operating agreement, registered agent, bank account \u2014 before your LLC buys anything.", content_formation.BODY),
    ("risks-faq.html", "Risks & FAQ", "/risks-faq.html", "What an LLC actually protects against, what it doesn't, and answers to the questions people ask before forming one.", content_risks_faq.BODY),
    ("contact.html", "Contact", "/contact.html", "Get in touch with Lamar Myers to set up an LLC purchase structure for your own business.", content_contact.BODY),
]

for fname, title, href, desc, body in PAGES:
    html = build.page(href, title, desc, body)
    build.write(fname, html)

print("Done.")
