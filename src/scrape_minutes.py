"""
Scrapes player minutes from Basketball Reference and saves them
for use in value analysis.
"""

import pandas as pd

def main():
    # 1. URL for Advanced Stats
    url = "https://www.basketball-reference.com/leagues/NBA_2023_advanced.html"

    # 2. Read the advanced stats table
    df = pd.read_html(url)[0]

    # 3. Filter to only Player and Minutes Played (MP)
    player_minutes = df[["Player", "MP"]]

    # 4. Remove repeated header rows
    player_minutes = player_minutes[player_minutes["Player"] != "Player"]

    # 5. Convert MP to numeric
    player_minutes["MP"] = pd.to_numeric(player_minutes["MP"], errors="coerce")

    # 6. Reset index
    player_minutes.reset_index(drop=True, inplace=True)

    # 7. Save as CSV
    player_minutes.to_csv("nba_2023_player_minutes.csv", index=False)

    print("✅ CSV created: nba_2023_player_minutes.csv")

if __name__ == "__main__":
    main()
