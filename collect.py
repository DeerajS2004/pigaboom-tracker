from playwright.sync_api import sync_playwright
from datetime import datetime

URL = "https://game.pigaboom.com/flutter/bie/?sessionToken=23a8bfb6-4a8a-486a-be4d-39adca52592e&locale=en&homeUrl=https:%2F%2Fplayinjeet.com&currency=INR&operatorId=2"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    page.wait_for_timeout(10000)

    # All visible results
    values = page.eval_on_selector_all(
        ".multiplier-history-item-value",
        """
        els => els.map(
            e => e.textContent.trim()
        )
        """
    )

    # Mystery rounds only
    mystery_values = page.eval_on_selector_all(
        ".multiplier-history-item.with-mistery-win",
        """
        els => els.map(
            e => e.querySelector('.multiplier-history-item-value')
                  ?.textContent.trim()
        ).filter(Boolean)
        """
    )

    browser.close()

timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# Save all results
with open("data.txt", "a", encoding="utf-8") as f:

    f.write("\n")
    f.write("=" * 60 + "\n")
    f.write(timestamp + "\n")
    f.write("=" * 60 + "\n\n")

    for value in values:
        f.write(value + "\n")

    f.write("\n")

# Save mystery rounds separately
if mystery_values:

    with open("mystery.txt", "a", encoding="utf-8") as f:

        f.write("\n")
        f.write("=" * 60 + "\n")
        f.write(timestamp + "\n")
        f.write("=" * 60 + "\n\n")

        for value in mystery_values:
            f.write(value + "\n")

        f.write("\n")

print(
    f"Saved {len(values)} results and "
    f"{len(mystery_values)} mystery rounds"
)
