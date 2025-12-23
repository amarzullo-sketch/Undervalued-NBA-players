Undervalued NBA Players Analysis
Overview

This project analyzes NBA player performance to identify undervalued players—those who provide high on-court impact relative to their salary cost. By combining advanced impact metrics with contract and playing-time data, the analysis highlights players who may outperform the expectations implied by their contracts.

The goal is not to predict future performance, but to evaluate value efficiency: how much impact a player delivers per dollar spent.

Motivation

NBA teams operate under strict salary caps, making efficient allocation of payroll critical. Traditional box-score statistics often fail to capture a player’s full impact, while advanced metrics can be difficult to interpret in isolation.

This project bridges that gap by:

Using RAPTOR (a well-known advanced metric) to measure impact

Normalizing impact by salary

Filtering by minutes played to avoid misleading small-sample results

Data Sources

This project combines multiple public datasets:

RAPTOR Metrics
Source: FiveThirtyEight
Provides advanced offensive, defensive, and total impact ratings.

Player Salaries
Source: Kaggle
Contains NBA contract data (raw dollar amounts).

Minutes Played
Source: Basketball Reference
Used to filter out players with insufficient playing time.

All datasets are publicly available and used for educational purposes.

Project Structure
Undervalued-NBA-players/
├── src/
│   ├── main.py
│   └── scrape_minutes.py
├── data/
│   ├── raw/
│   │   ├── raptor.csv
│   │   ├── salaries.csv
│   │   └── minutes.csv
│   └── processed/
│       └── output.csv
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

Methodology
1. Data Loading

Each dataset is loaded using pandas, with columns renamed and standardized to enable reliable merging across sources.

2. Data Cleaning

Salaries are converted from raw dollars to millions for interpretability

Minutes played are converted to numeric values

Players with missing or invalid data are removed

3. Filtering

To avoid misleading results from small sample sizes, players must meet a minimum minutes threshold:

MIN_MINUTES = 800


This roughly corresponds to consistent rotational players across a season.

4. Value Metric

A value score is computed as:

value_score = RAPTOR_total / salary_millions


This measures impact per dollar spent, allowing fair comparison across contracts of different sizes.

5. Ranking

Players are ranked by value score, and the top performers are saved to a CSV file for inspection.

Output

The final output is saved to:

data/processed/output.csv


This file contains:

Player name

Minutes played

Salary (millions)

RAPTOR total

Value score

How to Run
1. Clone the repository
git clone https://github.com/amarzullo-sketch/Undervalued-NBA-players
cd Undervalued-NBA-players

2. Install dependencies
pip install -r requirements.txt

3. Run the analysis
python src/main.py

4. View results

Open data/processed/output.csv.

Assumptions & Limitations

RAPTOR values are taken as-is and reflect the latest available season in the dataset

Salaries represent contract values, not actual in-game performance incentives

Injuries, role changes, and team context are not explicitly modeled

This analysis is descriptive, not predictive

Future Improvements

Possible extensions to this project include:

Adding data visualizations (bar charts of top value players)

Incorporating additional metrics (e.g., BPM, EPM)

Adjusting for position or role-based expectations

Extending analysis to multiple seasons

Automating data updates for new seasons

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

FiveThirtyEight for RAPTOR metrics

Basketball Reference for minutes data

Kaggle contributors for salary datasets
