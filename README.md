Undervalued NBA Players Analysis Overview

This project analyzes NBA player performance from the **2022–23 NBA season** to identify undervalued players—those who provide high on-court impact relative to their salary cost. By combining advanced impact metrics with contract and playing-time data, the analysis highlights players who may outperform the expectations implied by their contracts.

The goal is not to predict future performance, but to evaluate value efficiency: how much impact a player delivers per dollar spent.

Motivation

NBA teams operate under strict salary caps, making efficient allocation of payroll critical. Traditional box-score statistics often fail to capture a player’s full impact, while advanced metrics can be difficult to interpret in isolation.

This project bridges that gap by:

- Using RAPTOR (a well-known advanced metric) to measure impact  
- Normalizing impact by salary  
- Filtering by minutes played to avoid misleading small-sample results  

Data Sources (2022–23 Season)

This project combines multiple public datasets from the **2022–23 NBA season**:

- RAPTOR Metrics  
  Source: FiveThirtyEight  
  Provides advanced offensive, defensive, and total impact ratings.

- Player Salaries  
  Source: Kaggle  
  Contains NBA contract data (raw dollar amounts).

- Minutes Played  
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

Data Loading  
Each dataset is loaded using pandas, with columns renamed and standardized to enable reliable merging across sources.

Data Cleaning  
- Salaries are converted from raw dollars to millions for interpretability  
- Minutes played are converted to numeric values  
- Players with missing or invalid data are removed  

Filtering  
To avoid misleading results from small sample sizes, players must meet a minimum minutes threshold:

MIN_MINUTES = 800

This roughly corresponds to consistent rotational players across a full NBA season.

Value Metric  

value_score = RAPTOR_total / salary_millions

This metric measures impact per dollar spent, allowing fair comparison across contracts of different sizes.

Ranking  
Players are ranked by value score, and the top performers are saved to a CSV file for inspection.

Output

The final output is saved to:

data/processed/output.csv

This file contains:
- Player name  
- Minutes played (2022–23 season)  
- Salary (millions)  
- RAPTOR total  
- Value score  

How to Run

Clone the repository  
git clone https://github.com/amarzullo-sketch/Undervalued-NBA-players  
cd Undervalued-NBA-players  

Install dependencies  
pip install -r requirements.txt  

Run the analysis  
python src/main.py  

View results  
Open data/processed/output.csv

Assumptions & Limitations

- RAPTOR values reflect the 2022–23 season only  
- Salaries represent contract values, not performance-based incentives  
- Injuries, role changes, and team context are not explicitly modeled  
- This analysis is descriptive, not predictive  

Future Improvements

Possible extensions to this project include:
- Adding data visualizations (e.g., bar charts of top value players)  
- Incorporating additional metrics (BPM, EPM, etc.)  
- Adjusting for position or role-based expectations  
- Extending analysis to multiple seasons  
- Automating data updates for future seasons  

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

- FiveThirtyEight for RAPTOR metrics  
- Basketball Reference for minutes data  
- Kaggle contributors for salary datasets  

About

Built a data-driven NBA analysis pipeline in Python using **2022–23 season data**, merging RAPTOR
