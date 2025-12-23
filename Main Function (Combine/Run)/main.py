import pandas as pd

# ---------- LOAD ----------
raptor = pd.read_csv("data/raptor.csv")
salaries = pd.read_csv("data/salaries.csv")
minutes = pd.read_csv("data/minutes.csv")

# ---------- DEBUG: SEE REAL COLUMNS ----------
print("SALARIES COLS:", salaries.columns.tolist())
print("MINUTES COLS:", minutes.columns.tolist())

# ---------- FIX COLUMN NAMES ----------
salaries.columns = salaries.columns.str.strip()
minutes.columns = minutes.columns.str.strip()

salaries = salaries.rename(columns={
    "Player_Name": "player_name"
})

minutes = minutes.rename(columns={
    "Player": "player_name",
    "MP": "minutes"
})

# ---------- CLEAN TYPES ----------
salaries["salary_millions"] = pd.to_numeric(
    salaries["salary_millions"], errors="coerce"
) / 1_000_000

minutes["minutes"] = pd.to_numeric(minutes["minutes"], errors="coerce")

# ---------- FILTER RAPTOR TO LATEST SEASON ----------
latest_season = int(raptor["season"].max())
raptor = raptor[raptor["season"] == latest_season]

# ---------- KEEP ONLY WHAT WE NEED ----------
raptor = raptor[["player_name", "raptor_total"]]
salaries = salaries[["player_name", "salary_millions"]]
minutes = minutes[["player_name", "minutes"]]

# ---------- MERGE ----------
df = raptor.merge(salaries, on="player_name", how="inner")
df = df.merge(minutes, on="player_name", how="inner")

# ---------- FILTER + SCORE + SORT ----------
df = df[(df["minutes"] >= 800) & (df["salary_millions"] > 0)]
df["value_score"] = df["raptor_total"] / df["salary_millions"]
df = df.sort_values("value_score", ascending=False)

# ---------- OUTPUT ----------
top_20 = df.head(20)
print(f"\nUsing RAPTOR season: {latest_season}")
print(top_20)

top_20.to_csv("data/top_20_undervalued_players.csv", index=False)
print("\nSaved: data/top_20_undervalued_players.csv")
