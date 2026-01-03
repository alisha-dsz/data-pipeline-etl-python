# Data Pipeline Development (ETL)

## Overview
This project implements an automated ETL (Extract, Transform, Load) data pipeline using Python.  
The pipeline reads raw CSV data, performs preprocessing and feature engineering, and outputs a cleaned dataset ready for analysis.

## Tech Stack
- Python 3.10
- Pandas
- Scikit-learn

## Pipeline Stages
### Extract
- Reads raw student performance data from a CSV file.

### Transform
- Handles missing values using statistical imputation
- Performs feature engineering (Total & Average scores)
- Scales numerical features using StandardScaler

### Load
- Saves the cleaned and transformed dataset to a new CSV file.

## How to Run
```bash
pip install -r requirements.txt
python data_pipeline.py
