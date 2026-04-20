# Retail Analytics Project

This project implements a scalable retail analytics pipeline using Spark and a medallion architecture (Bronze → Silver → Gold). It transforms raw transactional data into analysis-ready datasets that support customer behavior analysis, BI reporting, feature engineering, and machine learning workflows.

The pipeline ensures data quality, reproducibility, and efficient downstream analytics, and leverages distributed processing (Spark) to handle large transactional datasets.

---

## What has been done so far

### 1) Bronze ingestion (`01_data_loading.ipynb`)
- Configures Spark and Lakehouse-style paths  
- Reads source CSV files with inferred schema and headers  
- Performs initial validation checks after ingestion  
- Writes Bronze Delta tables  

---

### 2) Data validation + cleaning (`02_data_validation_and_cleaning.ipynb`)
- Loads Bronze tables and validates schemas  
- Fixes data type inconsistencies (e.g., product hierarchy keys)  
- Runs SQL-based data quality checks:
  - row counts  
  - null checks  
  - duplicate detection  
  - referential integrity  
  - range validation  
- Performs exploratory analysis to validate behavioral patterns:
  - orders per user  
  - basket size  
  - reorder behavior  
- Builds a denormalized product hierarchy table  
- Writes cleaned Silver tables  

---

### 3) Silver transaction modeling (`03_silver_order_lines.ipynb`)
- Builds `silver_order_lines_prior` (historical transaction dataset capturing prior user behavior)  
- Builds `silver_order_lines_train` (supervised learning dataset for modelling reorder behaviour, with binary target `reordered`)  
- Models transaction-level data in a fact-like structure suitable for aggregation and feature engineering  
- Applies join optimizations:
  - repartition by `order_id`  
  - broadcast small product dimension  
- Persists Silver datasets for downstream analytics and ML  
- Structures outputs for BI consumption and reporting workflows  

---

### 4) Gold marts (`04_gold_customer_features.ipynb`)
- Implements Gold-layer business marts derived from Silver datasets  
- Aggregates transactional data into business-facing analytical views  
- Produces structured datasets for reporting, KPI tracking, and downstream consumption  

---

### 5) In-depth EDA + visualization (`05_eda_and_visualization.ipynb`)
- Performs advanced exploratory data analysis and visualization  
- Extends beyond validation into behavioral profiling and trend analysis  
- Supports interpretation of customer patterns and communication of insights for analytics and BI use  

---

## Analytical use cases

The prepared datasets support the following analytical and modelling use cases:

- Customer behavior analysis (purchase frequency, basket size, reorder patterns)  
- Feature engineering for machine learning models (e.g., reorder prediction)  
- Customer segmentation and clustering  
- Downstream BI and dashboarding workflows  
- Evaluation of model performance on transaction-level data  

---

## EDA approach

Exploratory data analysis (EDA) is implemented at two levels:

- **Foundational EDA** in `02_data_validation_and_cleaning.ipynb` for data profiling and validation  
- **In-depth EDA** in `05_eda_and_visualization.ipynb` for deeper behavioral insights and visualization  

Foundational checks include:

- Orders per user distribution  
- Basket size distribution  
- Reorder behavior distribution  

These are used to validate data integrity and reasonableness prior to downstream modelling and reporting.

---

## Gold layer outputs

Gold-layer marts are implemented and structured as business-facing analytical datasets, including:

- **Customer-level marts** (order cadence, reorder propensity, lifetime metrics)  
- **Product-level marts** (reorder rates, category performance)  
- **Basket-level marts** (basket composition and size trends)  

These marts are designed for direct use in BI tools, reporting, and advanced analytics.

---

## Repository structure

- `01_data_loading.ipynb` — Bronze ingestion pipeline  
- `02_data_validation_and_cleaning.ipynb` — validation, cleaning, and Silver dimension tables  
- `03_silver_order_lines.ipynb` — transaction-level Silver fact datasets  
- `04_gold_customer_features.ipynb` — Gold-layer aggregated marts  
- `05_eda_and_visualization.ipynb` — in-depth EDA and visualization  
- `count_rows.py` — helper script to count CSV rows  
- `check_all_csv.sh` — batch script for CSV validation  

---

## Utility scripts

### Count rows in one CSV
```bash
python3 count_rows.py /path/to/file.csv