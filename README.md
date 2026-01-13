# Sales Analysis using Python (NumPy) & Power BI

## Project Overview
This project demonstrates how Python (NumPy) can be used to preprocess and aggregate raw sales data, and how the processed data can be visualized using Power BI to generate business insights.

## Tools & Technologies
- Python 3
- NumPy
- Power BI
- CSV datasets
- Git & GitHub

## Project Structure
python_sales_analysis/
├── main.py
├── sales_data.csv
├── product_revenue.csv
├── salesperson_revenue.csv
├── README.md
└── .gitignore

## Data Processing (Python + NumPy)
- Loaded raw sales data from CSV
- Aggregated total revenue by Product ID
- Aggregated total revenue by Salesperson ID
- Exported cleaned KPI-level datasets as CSV files

## Power BI Dashboard
The Power BI dashboard includes:
- Total Revenue KPI
- Total Distinct Products Sold
- Average Revenue per Product
- Top Performing Products
- Product-wise Revenue Bar Chart
- Salesperson Performance Analysis

## Business Insights
- Identified top revenue-generating products
- Compared salesperson performance based on revenue
- Enabled KPI-driven decision making using clean datasets

## How to Run the Project
```bash
pip install numpy
python main.py
