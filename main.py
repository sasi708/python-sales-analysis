import numpy as np

# Load CSV
data = np.genfromtxt(
    "sales_data.csv",
    delimiter=",",
    dtype=None,
    encoding="utf-8",
    names=True
)

# Extract columns
quantity = data['Quantity']
total_sales = data['TotalSalesValue']
product = data['ProductID']
sales_person = data['SalesPersonID']

# KPIs
total_revenue = np.sum(total_sales)
avg_sale = np.mean(total_sales)
max_sale = np.max(total_sales)
min_sale = np.min(total_sales)

print("Total Revenue:", total_revenue)
print("Average Sale:", avg_sale)

# Product-wise revenue
unique_products = np.unique(product)
product_revenue = []

for p in unique_products:
    product_revenue.append([
        p,
        np.sum(total_sales[product == p])
    ])

product_revenue = np.array(product_revenue, dtype=object)

# SalesPerson-wise revenue
unique_salespersons = np.unique(sales_person)
salesperson_revenue = []

for sp in unique_salespersons:
    salesperson_revenue.append([
        sp,
        np.sum(total_sales[sales_person == sp])
    ])

salesperson_revenue = np.array(salesperson_revenue, dtype=object)

# Export product revenue
np.savetxt(
    "product_revenue.csv",
    product_revenue,
    delimiter=",",
    fmt="%s",
    header="ProductID,TotalRevenue",
    comments=""
)

# Export salesperson revenue
np.savetxt(
    "salesperson_revenue.csv",
    salesperson_revenue,
    delimiter=",",
    fmt="%s",
    header="SalesPersonID,TotalRevenue",
    comments=""
)

