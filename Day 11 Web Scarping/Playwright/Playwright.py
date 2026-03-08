from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # open page with custom timeout and wait only for DOM content
    page.goto(
        "https://www.scrapethissite.com/pages/forms/",
        wait_until="domcontentloaded",  # wait until the DOM is ready
        timeout=120000                  # wait up to 120 seconds (120000 ms)
    )

    # wait for table rows to appear
    page.wait_for_selector("tr.team")

    # locate all rows
    rows = page.locator("tr.team")

    # lists to store scraped data
    teams = []
    years = []
    wins_list = []
    losses_list = []
    pct_list = []

    # scrape each row
    for i in range(rows.count()):
        cols = rows.nth(i).locator("td")

        team = cols.nth(0).inner_text().strip()
        year = cols.nth(1).inner_text().strip()
        wins = cols.nth(2).inner_text().strip()
        losses = cols.nth(3).inner_text().strip()
        pct = cols.nth(5).inner_text().strip()

        teams.append(team)
        years.append(year)
        wins_list.append(wins)
        losses_list.append(losses)
        pct_list.append(pct)

    browser.close()

# create pandas DataFrame
df = pd.DataFrame({
    "Team": teams,
    "Year": years,
    "Wins": wins_list,
    "Losses": losses_list,
    "Win %": pct_list
})

print(df)