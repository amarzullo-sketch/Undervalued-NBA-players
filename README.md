# Undervalued NBA Players (2022–23 Season)

---

## Overview

This project analyzes **2022–23 NBA season data** to identify *undervalued players*—those who deliver strong on-court impact relative to their salary cost. By combining advanced impact metrics with contract and playing-time data, the analysis highlights players who may outperform the expectations implied by their contracts.

The goal is **not to predict future performance**, but to evaluate **value efficiency**: how much impact a player provides per dollar spent.

---

## Motivation

NBA teams operate under strict salary caps, making efficient payroll allocation critical. Traditional box-score statistics often fail to capture a player’s full impact, while advanced metrics can be difficult to interpret in isolation.

This project bridges that gap by:

- Using **RAPTOR** to measure overall on-court impact  
- Normalizing impact by **salary** to compare contracts fairly  
- Filtering by **minutes played** to reduce noise from small sample sizes  

---

## Data Sources (2022–23 Season)

All datasets are publicly available and used for educational purposes.

- **RAPTOR Metrics**  
  *Source:* FiveThirtyEight  
  Advanced offensive, defensive, and total impact ratings

- **Player Salaries**  
  *Source:* Kaggle  
  NBA contract values in raw dollars

- **Minutes Played**  
  *Source:* Basketball Reference  
  Used to filter out players with insufficient playing time

---

## Project Structure

Undervalued-NBA-players/
├── src/
│ ├── main.py
│ └── scrape_minutes.py
├── data/
│ ├── raw/
│ │ ├── raptor.csv
│ │ ├── salaries.csv
│ │ └── minutes.csv
│ └── processed/
│ └── output.csv
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

yaml
Copy code

---

## Methodology

### Data Loading
Each dataset is loaded using **pandas**, with standardized column names to enable reliable merging across sources.

### Data Cleaning
- Salaries converted from raw dollars to **millions**
- Minutes played converted to numeric values
- Players with missing or invalid data removed

### Filtering
To avoid misleading results from small sample sizes, players must meet a minimum playing-time threshold:

```python
MIN_MINUTES = 800
This threshold roughly corresponds to consistent rotation players across a full NBA season.

Value Metric
A value score is computed as:

ini
Copy code
value_score = RAPTOR_total / salary_millions
This measures impact per dollar, allowing fair comparison across contracts of different sizes.

Ranking
Players are ranked by value score, and the top performers are saved to a CSV file for inspection.

Output
The final output is saved to:


Copy code
data/processed/output.csv
The file contains:

Player name

Minutes played (2022–23 season)

Salary (millions)

RAPTOR total

Value score

How to Run
1. Clone the repository

Copy code
git clone https://github.com/amarzullo-sketch/Undervalued-NBA-players
cd Undervalued-NBA-players
2. Install dependencies

Copy code
pip install -r requirements.txt
3. Run the analysis

Copy code
python src/main.py
4. View results
Open:


Copy code
data/processed/output.csv
Assumptions & Limitations
RAPTOR values reflect the 2022–23 season only

Salaries represent contract values, not performance-based incentives

Injuries, role changes, and team context are not explicitly modeled

This analysis is descriptive, not predictive

What You’ll Learn
Cleaning and merging multiple real-world datasets

Designing domain-informed metrics

Filtering data to reduce statistical noise

Building a reproducible analytics pipeline in Python

Future Improvements
Add data visualizations (e.g., top value players bar chart)

Incorporate additional impact metrics (BPM, EPM)

Adjust value scores by position or role

Extend analysis across multiple seasons

Automate data updates for future years

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
FiveThirtyEight for RAPTOR metrics

Basketball Reference for minutes data

Kaggle contributors for salary datasets

About
Built a Python-based NBA analytics pipeline using 2022–23 season data to merge RAPTOR impact metrics with salary and minutes played, ranking players by impact per dollar to identify undervalued contributors.
