# Retail Analytics & Customer Segmentation

End-to-end retail analytics project using the Instacart dataset. The project builds a Spark-based medallion pipeline from raw transactional files into curated Silver and Gold tables for customer analytics, Power BI reporting, customer segmentation, and LLM/RAG-based natural-language analytics.

## Tech Stack

- Microsoft Fabric / Spark / PySpark
- Bronze, Silver, and Gold medallion architecture
- Python, Pandas
- Power BI
- KMeans clustering
- Azure Machine Learning
- Azure AI Foundry
- LLM/RAG pipeline

## Pipeline

```text
Raw Instacart CSVs
        ↓
Bronze Layer
Raw ingested tables
        ↓
Silver Layer
Cleaned, validated, joined order-line tables
        ↓
Gold Layer
Customer and business-level analytical features
        ↓
Analytics Outputs
EDA, clustering, R analysis, Power BI dashboards
        ↓
Azure ML / Azure AI Foundry
RAG pipeline for natural-language querying over curated outputs
```

## Project Workflow

| Stage                 | File / Tooling                          | Purpose                                                                                            |
| --------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Bronze ingestion      | `01_data_loading.ipynb`                 | Loads raw CSV files, validates initial schemas, and writes Bronze tables                           |
| Silver validation     | `02_data_validation_and_cleaning.ipynb` | Cleans data, fixes type issues, checks nulls, duplicates, ranges, and table relationships          |
| Silver order lines    | `03_silver_order_lines.ipynb`           | Builds transaction-level order-line datasets for feature engineering, and downstream analytics |
| Gold features         | `04_gold_customer_features.ipynb`       | Creates customer and business-level analytical features                                            |
| EDA and visualisation | `05_eda_and_visualization.ipynb`        | Performs behavioural analysis, visualisation, and exploratory summaries                            |
| Power BI reporting    | Power BI                                | Presents curated analytics outputs through dashboard visuals and a semantic model                  |
| Applied AI / RAG      | Azure ML / Azure AI Foundry             | Enables natural-language querying over project context and curated analytics outputs               |

## Power BI Reporting Layer

Power BI is used to present the curated analytics outputs through business-facing dashboards. The report focuses on product demand, aisle and department performance, order timing behaviour, and the semantic model used to connect the reporting tables.

### Dashboard 1: Product, Aisle, and Department Analysis

This dashboard summarises which products, aisles, and departments dominate order volume. It supports retail questions such as which categories drive demand and which product groups appear most frequently in customer baskets.

![Power BI product, aisle and department dashboard](docs/powerbi-visual1.png)

### Dashboard 2: Order Timing Analysis

This dashboard analyses ordering behaviour across hours of the day and days of the week. It helps identify when customers are most active and how order volume changes across the weekly cycle.

![Power BI order timing dashboard](docs/powerbi-visual2.png)

### Power BI Semantic Model

The semantic model connects curated reporting tables so product hierarchy, order behaviour, and customer-level features can be analysed together. This makes the dashboard more than a set of isolated visuals: it provides a structured BI layer over the Silver and Gold outputs.

![Power BI data model](docs/powerbi-data-model.png)

## RAG Workflow

The implemented retrieval-augmented workflow uses customer-level analytical outputs generated from the Gold layer of the pipeline.

The workflow currently includes:

- Gold-layer customer analytical features
- semantic customer behaviour summaries generated from structured Gold tables
- sampled customer records prepared for embedding and retrieval

Gold-layer customer records are transformed into semantic text chunks describing behavioural characteristics such as:

- total orders
- average basket size
- reorder ratio
- customer loyalty classification
- shopping frequency

Embeddings are generated using Azure OpenAI embedding models and indexed in Azure AI Search for vector similarity retrieval.

For a user query, the retrieval step identifies the most semantically relevant customer chunks. These retrieved chunks are then provided to an LLM to generate a response grounded in the retrieved customer behaviour data.

This extends the project beyond static analysis by demonstrating a retrieval-based workflow for querying customer-level retail analytics outputs with LLM assistance.

## Current Status

Completed:

- Bronze ingestion
- Silver validation and order-line modelling
- Gold feature engineering
- EDA and visualisation
- customer segmentation
- Power BI dashboard basic
- Power BI semantic model basic
- Azure ML experimentation layer
- Azure AI Foundry LLM/RAG layer