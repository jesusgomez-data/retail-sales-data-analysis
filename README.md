# Retail Sales & Customer Behavior Analysis

## 📊 Power BI Dashboard
This project includes an interactive Power BI dashboard built to analyze retail sales performance across multiple dimensions.

**Key metrics included:**
- Total Revenue
- Average Ticket Size
- Monthly Revenue Trend
- Revenue by Sales Channel
- Revenue by City
- Top 5 Products by Revenue
- Top 5 Customers by Revenue

📁 Dashboard file: `retail_sales_dashboard.pbix`

---

## 📌 Project Overview
This end-to-end data analysis project simulates a retail company operating across multiple cities and sales channels.  
The goal is to extract business insights from transactional sales data using SQL, Python and Power BI.

---

## 🛠 Tools & Technologies
- SQLite (relational database)
- SQL (data analysis & joins)
- Python (data generation & validation)
- Pandas (analysis & cross-validation)
- Power BI (data modeling, DAX & visualization)

---

## 🗂 Dataset Description
The dataset was fully generated for this project and contains:
- 500+ sales transactions
- Customer data
- Product catalog
- Multiple cities
- Online and physical store channels
- One full year of activity

---

## 🧱 Data Model
- Fact table: `ventas`
- Dimension tables: `clientes`, `productos`
- Relationships: Many-to-One
- Star schema design

---

## 📈 Key Business Questions Answered
- How much revenue did the company generate?
- How do sales evolve over time?
- Which sales channel performs better?
- Which cities generate the most revenue?
- Which products and customers contribute the most?

---

## 🧪 Data Quality & Validation
- SQL and Pandas cross-validation
- Null value checks
- Negative value checks
- Referential integrity validation

---

## ▶️ How to Run the Project
1. Clone the repository
2. Open `retail_sales.db` with DB Browser for SQLite
3. (Optional) Run `generate_sales.py` to regenerate the dataset
4. Open `analysis.ipynb` for Python analysis
5. Open `retail_sales_dashboard.pbix` with Power BI Desktop

---

## 👤 Author
**Jesus Gomez**  
Junior Data Analyst  
SQL | Python | Pandas | Power BI

├── analysis.ipynb          # Data analysis and insights
├── generate_sales.py       # Script to generate synthetic sales data
├── retail_sales.db         # SQLite database
├── README.md               # Project documentation


